import os
import subprocess
import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector
from xml.etree import cElementTree as ET

#Checks and runs the setup.sh file for the first time if the folder ./ADS/ does not yet exist
def initial_setup():
    isExist = os.path.exists('./ADS/')
    if(isExist == False):
        subprocess.run(['bash', 'setup.sh'])
    else:
        pass

def extract_tag(tree, tag_name):
    """
    1. Read the XML file
    2. Get the namespace for specific tags
    3. Iter the needed tag name
    4. Print the content of that tag
    """
    #Print data from the specified tag
    for node in tree.iter(tag_name):
        for elem in node.iter():
            #print(f"{format_tag(elem)}: {elem.text}")
            
            #This will only print the data inside the tag, uncomment
            #the line above to add the tag title
            print(elem.text)

def extract_all_tags(tree, tag_dict):
    for tag in tag_dict:
        extract_tag(tree, tag_dict)

def format_tag(elem):
    return str(elem.tag.replace("{http://purl.org/dc/elements/1.1/}","")).capitalize()

def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)  # We use the seed 42

nlp_model = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp_model.add_pipe('language_detector', last=True)

def print_lang(data):
    # Document level language detection
    doc = nlp_model(data)
    language = doc._.language
    print(language)
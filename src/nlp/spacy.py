import nltk
import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector
#from langdetect import detect

lang_record =   {"de": 0, "fr": 0}

def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)  # We use the seed 42
# Start Spacy Components
nlp_model = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp_model.add_pipe('language_detector', last=True)

def get_lang(data):
    """
    Outputs a language dictionary from a parameter data, 
    which represents the extracted description from 
    the description tag of an XML file.
    """
    doc = nlp_model(data)
    lang = doc._.language
    update_lang_count(lang)
    return lang

def update_lang_count(lang):
    """
    Updates the language count list for a larger count of analysed XML files.
    Includes all positive and negative results, with an expectancy of a majority of positive results.
    """
    if lang["language"] not in lang_record.keys():
        lang_record[lang["language"]] = 1
    else:
        lang_record[lang["language"]] += 1
    
def print_lang_count():    
    print(lang_record)

"""
Gensim Part
"""
#Prerequisites
def gensim():
    nltk.download('stopwords')
    nlp = spacy.load('fr_core_web_md', disable=['parser', 'ner'])

    stopwords = set(nltk.corpus.stopwords.words('german')) | set(nltk.corpus.stopwords.words('french'))

import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector
from langdetect import detect

lang_record = ["de", 0, "fr", 0]

#Start Spacy Components
def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)  # We use the seed 42
nlp_model = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp_model.add_pipe('language_detector', last=True)

def get_lang(data):
    # Document level language detection
    doc = nlp_model(data)
    lang = doc._.language
    update_lang_count(lang)
    #print(lang)                #Uncomment for debugging purposes
    return lang

def update_lang_count(lang):
    if((lang["language"]) == "de"):
        lang_record[1] += 1
    elif((lang["language"]) == 'fr'):
        lang_record[3] += 1
    
def print_lang_count():    
    print(lang_record)
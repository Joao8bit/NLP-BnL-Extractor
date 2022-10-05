import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector
from langdetect import detect

def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42)  # We use the seed 42

def get_lang(data):
    # Document level language detection
    nlp_model = spacy.load("en_core_web_sm")
    Language.factory("language_detector", func=get_lang_detector)
    nlp_model.add_pipe('language_detector', last=True)
    doc = nlp_model(data)
    return doc._.language
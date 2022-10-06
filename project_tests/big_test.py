import os
from src.xml.xml_manipulation import *
from src.nlp.nlp import *

def description_extractor():
    root_dir = './ADS/'
    files = os.listdir(root_dir)
    
    for file in files[:5]:
        print(file)
        tree = ET.parse(f"{root_dir}/{file}")                               #Initialization of an XMl file
        data = extract_tag(tree, tag_dict["description"])   #Extract description tag data
        get_lang(data)     
    print_lang_count()                                      #Language displayer as a list
    
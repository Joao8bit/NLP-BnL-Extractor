import os
from src.xml.xml_manipulation import *
from src.nlp.spacy import *

def description_extractor():
    root_dir = './ADS/'
    files = os.listdir(root_dir)
    
    range = 10                                             #How many files do you want to check?  
    for file in files[:range]:
        #print(file)
        tree = ET.parse(f"{root_dir}/{file}")               #Initialization of an XMl file
        data = extract_tag(tree, tag_dict["description"])   #Extract description tag data
        get_lang(data)
    print(f'Out of {range} files, this is the result:')    
    print_lang_count()                                      #Language displayer as a list
    
import os
from src.xml.xml_manipulation import *
from src.nlp.nlp import *

def description_extractor():
    root_dir = './ADS/'
    file = os.listdir(root_dir)                         #Gets a list of files in root_dir
    tree = ET.parse(f"{root_dir}/{file[2]}")            #Initialization of the first XMl file
    print('\nPrinting description...\n')
    data = extract_tag(tree, tag_dict["description"])   #Extract description tag data
    print(data)                                         #Prints description data
    print('')
    print(get_lang(data))                               #Prints language detection output

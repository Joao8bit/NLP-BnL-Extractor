from src.xml.xml_manipulation import *
from src.nlp.nlp import *
import subprocess

def description_extractor():    
    subprocess.run(['cp', './ADS/257048-ADVERTISEMENT-DTL303.xml','./'])    #Copy a single file to work with
    tree = ET.parse('257048-ADVERTISEMENT-DTL303.xml')                      #Initialization of an XMl file for testing purposes
    print('\nPrinting description...\n')
    data = extract_tag(tree, tag_dict["description"])                       #Extract description tag data
    print_lang(data)                                                        #Language displayer

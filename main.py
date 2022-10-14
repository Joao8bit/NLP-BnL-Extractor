#!/usr/bin/python3

import os
#from src.xml.xml_manipulation import *
import src.csv.csv as csv
from src.xml.xml_manipulation import *
from src.nlp.spacy import *

def full_range_lang(root_dir, files):
    """
    This function will extract an XML file list, its description,
    and analyse its language using the text in the description.
    """
    for file in files:
        tree = ET.parse(f"{root_dir}/{file}")               #Initialization of an XMl file
        data = extract_tag(tree, tag_dict["description"])   #Extract description tag data
        get_lang(data)
    print_lang_count()



def main():    
    root_dir = './ADS/'
    files = os.listdir(root_dir)
    range = files[:10]
    print('Writing to CSV...')
    csv.write_to_csv(root_dir, range)
    print('Operation complete!')
    print('Analysing file language with SpaCy...')
    full_range_lang(root_dir, range)
    print(f'Out of {len(range)} files, {lang_record[1]} were written in German, while {lang_record[3]} were written in French.\nThis means that {len(range)-lang_record[1]-lang_record[3]} files were not recognised as either German or French.')

if __name__=="__main__":
    main()

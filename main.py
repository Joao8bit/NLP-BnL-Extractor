#!/usr/bin/python3

import os
import src.xml.xml_manipulation as xml
import src.csv.csv as csv
import src.nlp.spacy as spacy



def full_range_lang(root_dir, files):
    """
    This function will extract an XML file list, its description,
    and analyse its language using the text in the description.
    """
    for file in files:
        tree = xml.ET.parse(f"{root_dir}/{file}")         
        data = xml.extract_tag(tree, xml.tag_dict["description"])   
        spacy.get_lang(data)
        print(file)
    spacy.print_lang_count()

def main():    
    root_dir = './ADS/'
    files = os.listdir(root_dir)
    range = files[:20]

    print('Writing to CSV...')
    
    csv.write_to_csv(root_dir, range)
    
    print('Operation complete!')
    print('Analysing file language with SpaCy...')
    
    full_range_lang(root_dir, range)
    
    print(f'Out of {len(range)} files, {spacy.lang_record[1]} were written in German, while {spacy.lang_record[3]} were written in French.\nThis means that {len(range)-spacy.lang_record[1]-spacy.lang_record[3]} files were not recognised as either German or French.')

if __name__=="__main__":
    main()

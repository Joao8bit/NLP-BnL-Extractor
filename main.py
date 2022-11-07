#!/usr/bin/python3

import os
import src.xml.xml_manipulation as xml
import src.csv.csv as csv
import src.nlp.spacy as spacy
import pandas as pd
from multiprocessing import Process


"""
CSV CREATION STEPS
"""
def get_csv_data(root_dir, tree):
    """
    This function will gather all the information about a single XML file that will be written
    Inside the CSV file, along with the language detection data.
    """
    #This will be the full row data list
    full_data=[] 
    #This is the xml part of the data, only tag extraction
    xml_data = [xml.extract_tag(tree, xml.tag_dict["source"]),
                xml.extract_tag(tree, str(xml.tag_dict["date"])),
                xml.extract_tag(tree, xml.tag_dict["publisher"]),
                xml.extract_tag(tree, xml.tag_dict["description"])
                ]
    #This is the language detection data
    spacy_data = spacy.get_lang(xml.extract_tag(tree, xml.tag_dict["description"]))
    xml_data.append(spacy_data["language"])
    xml_data.append(spacy_data["score"])
    full_data = xml_data
    return full_data

def full_range_lang(root_dir, files):
    """
    This function will extract an XML file list, its description,
    and analyse its language using the text in the description.
    """
    for file in files:
        tree = xml.ET.parse(f"{root_dir}/{file}")         
        data = xml.extract_tag(tree, xml.tag_dict["description"])   
        spacy.get_lang(data)
    spacy.print_lang_count() 

def write_to_csv(root_dir, file_list, csv_name):
    """
    Opens a csv file, writes the header (Source, Date, Publisher and Description).
    Then, writes in a sequence all extracted tag data from XML files.
    """
    with open(csv_name, 'w', encoding='UTF8') as f:
        # Opens the CSV and writes the Header titles
        csv.writer(f).writerow(csv.header)
        # For each file, tag data will be extracted, and written into the CSV file
        for file in file_list:
            tree = xml.open_xml(root_dir, file)
            file_data = get_csv_data(root_dir, tree)
            csv.writer(f).writerow(file_data)
    f.close()

def main_csv():
    #Variables declaration
    root_dir = './ADS/'
    files = os.listdir(root_dir)
    range1 = files[:30000]
    range2 = files[30000:60000]
    range3 = files[60000:90000]
    #range4 = files[100000:100001]
    range_total = len(range1+range2+range3)

    process_1 = Process(target=write_to_csv, args=(root_dir,  range1, './advertisements1.csv'))
    process_2 = Process(target=write_to_csv, args=(root_dir,  range2, './advertisements2.csv'))
    process_3 = Process(target=write_to_csv, args=(root_dir,  range3, './advertisements3.csv'))
    print('Writing to CSV and analysing language...')

    process_1.start()
    process_2.start()
    process_3.start()
    process_1.join()
    process_2.join()
    process_3.join()
    
    #Template of main function
    #write_to_csv(root_dir, range1, './advertisements1.csv')
    
    print('Operation complete!')
    
    #full_range_lang(root_dir, range1)
    #full_range_lang(root_dir, range2)
    #full_range_lang(root_dir, range3)
    
    print(f'Out of {range_total} files, {spacy.lang_record["de"]} were written in German, while {spacy.lang_record["fr"]} were written in French.\nThis means that around {int((range_total-spacy.lang_record["de"]-spacy.lang_record["fr"])/range_total*100)}% of files were not recognised as either German or French.')

def replace():
    df = pd.read_csv('advertisements1.csv')        
    for row in df.iterrows():
        print(row[1])
        
if __name__=="__main__":
    #main_csv()
    df = pd.read_csv('advertisements1.csv')
    #for column in len(df.columns)
    print(df["Language"].dtype)
    print(df.columns[4])
    print(df.__dataframe__())
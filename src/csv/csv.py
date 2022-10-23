from  csv import writer
import src.xml.xml_manipulation as xml
import src.nlp.spacy as spacy

header = ['Source', 'Date', 'Publisher', 'Description']


def write_to_csv(root_dir, file_list):
    """
    Opens a csv file, writes the header (Source, Date, Publisher and Description).
    Then, writes in a sequence all extracted tag data from XML files.
    """
    with open('./advertisements.csv', 'w', encoding='UTF8') as f:
        # Opens the CSV and writes the Header titles
        writer(f).writerow(header)
        # For each file, tag data will be extracted, and written into the CSV file
        for file in file_list:
            tree = xml.open_xml(root_dir, file) 
            file_data = xml.get_xml_data(tree)
            writer(f).writerow(file_data)

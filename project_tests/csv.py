from  csv import writer
import src.xml.xml_manipulation as xml

header = ['Source', 'Date', 'Publisher', 'Description']


def get_xml_data(tree):    
    row_data = [xml.extract_tag(tree, xml.tag_dict["source"]),
                xml.extract_tag(tree, xml.tag_dict["date"]),
                xml.extract_tag(tree, xml.tag_dict["publisher"]),
                xml.extract_tag(tree, xml.tag_dict["description"])]
    return row_data

def write_to_csv(root_dir, file_list):
    """
    Opens a csv file, writes the header (Source, Date, Publisher and Description).
    Then, writes in a sequence all extracted tag data from XML files.
    """
    with open('./advertisements.csv', 'w', encoding='UTF8') as f:
        writer(f).writerow(header)
        for file in file_list:
            tree = xml.open_xml(root_dir, file) 
            file_data = get_xml_data(tree)
            writer(f).writerow(file_data)

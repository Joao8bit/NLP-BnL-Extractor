import os
import subprocess
from xml.etree import cElementTree as ET

#We want to keep track of the different tags that might interest us
#here from the XML files structure
tag_dict={
    "identifier": "{http://purl.org/dc/elements/1.1/}identifier",
    "source": "{http://purl.org/dc/elements/1.1/}source",
    "date": "{http://purl.org/dc/elements/1.1/}date",
    "publisher": "{http://purl.org/dc/elements/1.1/}publisher",
    "relation": "{http://purl.org/dc/elements/1.1/}relation",
    "description": "{http://purl.org/dc/elements/1.1/}description",
    "title": "{http://purl.org/dc/elements/1.1/}title",
    "type": "{http://purl.org/dc/elements/1.1/}type"
}
#Checks and runs the setup.sh file for the first time if the folder ./ADS/ does not yet exist
def initial_setup():
    isExist = os.path.exists('./ADS/')
    if(isExist == False):
        subprocess.run(['bash', 'setup.sh'])
    else:
        pass

def extract_tag(tag_name):
    """
    1. Read the XML file
    2. Get the namespace for specific tags
    3. Iter the needed tag name
    4. Print the content of that tag
    """
    
    #Read contents from XML file
    tree = ET.parse('257048-ADVERTISEMENT-DTL303.xml')
    root = tree.getroot()

    #Print data from the specified tag
    for node in tree.iter(tag_name):
        for elem in node.iter():
            print("{}: {}".format(format_tag(elem), elem.text))

def format_tag(elem):
    return elem.tag.replace("{http://purl.org/dc/elements/1.1/}","")

def main():
    initial_setup()
    extract_tag(tag_dict["description"])

if __name__=="__main__":
    main()


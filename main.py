#!/usr/bin/env python3

import utils as u
from utils import *
#Initialization of an XMl file for testing purposes
tree = ET.parse('257048-ADVERTISEMENT-DTL303.xml')

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


#Tags have ugly naming, this helps a bit

def main():
    initial_setup()
    extract_tag(tree, tag_dict["description"])
    print('\nLang = ')
    print_lang(extract_tag(tree, tag_dict))

if __name__=="__main__":
    main()


from xml.etree import cElementTree as ET

#Tag collection for target XML files
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

def open_xml(path, file):
    """
    Opens an XML file, allows for an open/close approach.
    """
    return ET.parse(f"{path}/{file}")               #Initialization of an XMl file

def extract_tag(tree, tag_name):
    """
    1. Read the XML file
    2. Provide the namespace for specific tags
    3. Iter the needed tag name
    4. Return the content of that tag
    """
    data=''
    for node in tree.iter(tag_name):
        data = data + node.text
        #for elem in node.iter():    #This helps with tags with multiple children, shouldn't be the case
            #This will only print the data inside the tag, uncomment
            #the line below to add the tag title
            #print(elem.text)
            #print(f"{format_tag(elem)}: {elem.text}")
    return data

#TODO: To fix
#def extract_childless_tag(tree, tag_name):
#    return tree.iter(tag_name)

def format_tag(elem):
    """
    Tags have ugly naming, this helps a bit.
    Mainly designed for printing purposes.
    """
    return str(elem.tag.replace("{http://purl.org/dc/elements/1.1/}","")).capitalize()


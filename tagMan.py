


#Tags have ugly naming, this helps a bit
def format_tag(elem):
    return str(elem.tag.replace("{http://purl.org/dc/elements/1.1/}","")).capitalize()

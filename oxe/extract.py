'''
finds a given tag and returns accompanying uuid
'''
import xml.etree.ElementTree as ET

INSTANCE_ID = 'instanceID'

def extract(input_file, tag):
    '''
    finds a given tag and returns accompanying uuid
    '''
    tree = ET.parse(input_file)
    vals = []
    for elem in tree.iter():
        if elem.tag == tag:
            vals.append(elem.text)
        if elem.tag == INSTANCE_ID:
            vals = [elem.text] + vals
    return vals

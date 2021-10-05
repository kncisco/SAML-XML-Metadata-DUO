import xml.etree.ElementTree as ET
import json

filename = 'Metadata.xml'

tree = ET.parse(filename)
root = tree.getroot()

xmldict = {}
nameidlist = []

xmldict['Entity ID'] = root.attrib['entityID']

for item in root.iter():
    if 'SingleLogoutService' in item.tag:
        if 'HTTP-POST' in item.attrib['Binding']:
            xmldict['Single Logout URL'] = item.attrib['Location']
    elif 'AssertionConsumerService' in item.tag:
        xmldict['ACS URL'] = item.attrib['Location']
    if 'NameIDFormat' in item.tag:
        nameidlist.append(item.text)

xmldict['NameID Format'] = nameidlist

with open('output.txt', 'w') as file:
    file.write(json.dumps(xmldict, indent=4, ensure_ascii=True))
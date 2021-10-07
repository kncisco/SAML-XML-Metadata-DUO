import xml.etree.ElementTree as ET
import re
import json

filename = 'Metadata.xml'

tree = ET.parse(filename)
root = tree.getroot()

xmldict = {}
nameidlist = []
signingoptiondict = {}

xmldict['Entity ID'] = root.attrib['entityID']

for item in root.iter():
    if 'SingleLogoutService' in item.tag:
        if 'HTTP-POST' in item.attrib['Binding']:
            xmldict['Single Logout URL'] = item.attrib['Location']
    elif 'AssertionConsumerService' in item.tag:
        xmldict['ACS URL'] = item.attrib['Location']
    elif 'NameIDFormat' in item.tag:
        nameidlist.append(item.text)
    elif 'SignatureMethod' in item.tag:
        signaturemethod = re.findall(r'sha.*', item.attrib['Algorithm'])
        xmldict['Signature Algorithms'] = signaturemethod
    elif 'SPSSODescriptor' in item.tag:
        if item.attrib['AuthnRequestsSigned'] == 'true':
            signingoptiondict['Sign Response'] = True
        else:
            signingoptiondict['Sign Response'] = False
        if item.attrib['WantAssertionsSigned'] == 'true':
            signingoptiondict['Sign Assertion'] = True
        else:
            signingoptiondict['Sign Assertion'] = False

xmldict['NameID Format'] = nameidlist
xmldict['Signing Options'] = signingoptiondict

with open('output.txt', 'w') as file:
    file.write(json.dumps(xmldict, indent=4, ensure_ascii=True))
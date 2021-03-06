import xml.etree.ElementTree as ET
import re
import os
import json

def metadataParser(metadata):
    ### Setup Relevant Objects ###
    xmldict = {}
    nameidlist = []
    signingoptiondict = {}
    acslist = []
    
    ### Parse Provided Metadata and Get XML Root ###
    tree = ET.parse(metadata)
    root = tree.getroot()
    
    ### Extract Relevant Data and store in Dict ###
    xmldict['Entity ID'] = root.attrib['entityID']

    for item in root.iter():
        if 'SingleLogoutService' in item.tag:
            if 'HTTP-POST' or "HTTP-Redirect" in item.attrib['Binding']:
                try:
                    xmldict['Single Logout URL'] = item.attrib['ResponseLocation']
                except KeyError:    
                    xmldict['Single Logout URL'] = item.attrib['Location']
        elif 'AssertionConsumerService' in item.tag:
            try:
                acsdict = { 'URL': item.attrib['Location'], 'Index': item.attrib['index'], 'isDefault': item.attrib['isDefault'] }
            except KeyError:
                acsdict = { 'URL': item.attrib['Location'], 'Index': item.attrib['index'] }
            acslist.append(acsdict)           
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
    xmldict['ACS URLs'] = acslist
    xmldict['Signing Options'] = signingoptiondict
    return xmldict

filename = 'Metadata.xml'

if __name__ == "__main__":

    ### Check to see if required file exists, if not - prompt for Filename"
    if os.path.isfile(filename) is False:
        filename = input('Metadata.xml not found, Please input the correct metadata filename: ')

    ### Submit file to metadataParser Function - extract relevant objects ###
    parseddata = metadataParser(filename)

    ### Write output ###
    with open('output.txt', 'w') as file:
        file.write(json.dumps(parseddata, indent=4, ensure_ascii=True))
# SAML-XML-Metadata-DUO

For all those SAML users out there (Specifically Cisco DUO), this script will allow for the easy creation of Generic SAML providers.

The script parses SAML Metadata (from the SAML SP) and writes a JSON formatted text file for the purposes of easy cut/paste into DUO's "Generic Service Provider" type of application.

The output contains the following:
- Entity ID
- Supported Signature Algorithms
- Assertion Consumer Service (ACS) URL
- Single Logout URL
- List of supported NameID Formats from the SAML SP
- True/False on whether Assertions and Responses require signing

Requirements:
- SAML Metadata from the Service Provider of choice (ie - Cisco vManage)
- Edit the "filename" variable in the script to reflect the name of the SAML Metadata file
- Alternativvely, the script will prompt for the correct filename if "Metadata.xml" is not found.

Usage:
- python3 app.py

and.... Voila!!!

You can use these outputs to configure the appropriate settings within your DUO Generic Service Provider application.
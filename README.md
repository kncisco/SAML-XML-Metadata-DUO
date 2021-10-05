# SAML-XML-Metadata-DUO

For all those SAML users out there (Specifically Cisco DUO), this script will allow for the easy creation of Generic SAML providers.

The script parses the provided SAML Metadata (from the SAML SP) and writes a JSON formatted text file for the purposes of easy cut/paste into DUO's "Generic Service Provider" type of application.

The output contains the following:
    - Entity ID
    - Assertion Consumer Service (ACS) URL
    - Single Logout URL
    - List of supported NameID Formats from the SAML SP

You can use these outputs to configure the appropriate settings within your DUO Generic Service Provider application.
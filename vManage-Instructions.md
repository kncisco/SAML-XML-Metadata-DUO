# Instrucitons for Configuring vManage/DUO SSO

These instructions assume that DUO SSO has already been setup in your environment.  For instructions on setting up DUO SSO see the DUO documentation.

1. Login to vManage GUI and obtain Metadata
2. Login to the DUO Admin Panel.  Navigate to Applications > Protect an Application
3. Select the "Generic Service Provider (2FA with SSO hosted by Duo)" appliction - click "Protect"
4. In the "Downloads" section, click the "Download XML" button to retrieve the SAML Metadata - this will be uploaded to vManage later.

![Metadata](/images/metadata.png)

5. Under the "Service Provider" section, use the output of the app to fill in the appropriate entries.
6. Under the "SAML Response" section, use the output of the app to fill in the appropriate entries and include the following additions.
    - In the "Map Attributes" section - select the appropriate DUO (iDP) attribute (example - Username) - map that attribute to the "SAML Response Attribute" Username.
        - NOTE - vManage expects to see the "Username" attribute - therefore, the SAML Response Attribute MUST be "Username"

![Map Attributes](/images/map.png)

    - In the "Role Attributes" section - Enter "Groups" under "Attribute Name".  You can associate the appropriate groups in Duo to the appropriate vManage groups here.
        - By Default - vManage includes the "netadmin" and "operator" roles, see the following image for an example of that mapping to the appropriate Duo groups.

![Role Attributes](/images/role.png)

7.  Ensure that the appropriate Policy and Settings are applied to the newly created application - click Save.
8.  Navigate to the vManage GUI, upload the Duo SAML Metadata that you gathered previously.
9.  Test Authenticating to vManage!

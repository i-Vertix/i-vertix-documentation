---
id: saml
title: Configuring connection via SAML
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Configure SAML authentication

Go to **Administration > Authentication > SAML Configuration**.

### Step 1: Enable authentication

Enable SAML authentication:

- **Enable SAMLv2 authentication**: enables or disables SAML authentication.
- **Authentication mode**: indicates if the authentication should be done using only SAML or using local
  authentication as well (**Mixed**). In mixed mode, users created manually in the i-Vertix Monitoring (and not identified via SAML)
  will also be able to log in.

> When setting the parameters, we recommend that you activate the "mixed" mode. This will allow you to retain access to
> the local `admin` account in the event of a misconfiguration.

### Step 2: Configure Identity Provider access credentials

Configure Identity Provider information:

- **Remote login URL**: defines the identity provider's login URL to identify users (mandatory).
- **Issuer (Entity ID) URL**: defines the URL representing the unique name for a SAML entity (mandatory).
- **Copy/paste x509 certificate**: add here the x509 certificate of the identity provider (mandatory).
- **User ID (login) attribute for Monitoring user**: defines which of the variables returned by the identity provider
  must be used to authenticate users. For example, **email**. (mandatory).
- Logout from:
  * **Centreon UI Only**: users will only be logged out from the i-Vertix Monitoring.
  * **Both Identity Provider and Centreon UI**:  users will be logged out from both i-Vertix Monitoring and the identity provider.
    > If you select **Both Identity Provider and Centreon UI**, you need to define a **Logout URL**.

### Step 3: Configure authentication conditions

You can define conditions according to which users will be allowed to log in or not, based on the data received by a
particular endpoint:
  - Activate **Enable conditions on identity provider**.
  - Define which attribute will be used to validate the conditions.
  - In **Define authorized conditions values**, define which will be the authorized values returned.
    If you enter several values, all will have to be met for the condition to be validated. All users who try to connect
    with another value will be unable to log in.

### Step 4: Manage user creation

<Tabs groupId="sync">
<TabItem value="Users automatic management" label="Automatic management">

If you turn on **Enable auto import**, users who log in to i-Vertix IT Monitoring for the first time will be created in the Monitoring
configuration.

:::warning

**Enable auto import** does not automatically import all users from your infrastructure, it only creates users automatically upon first login.

:::

- **Enable auto import**: enables or disables automatic user import.  If auto import is disabled, you will have to
  [create each user manually](../../managing-users-contacts/create-users-manually.md) before they can log in.
- **Contact template**: select a [contact template](../../managing-users-contacts/contact-templates.md) that will be
  applied to newly imported users. In particular, this allows you to manage the default configuration of the
  [notifications](../../events-alerts/managing-notifications/configuring-notification.md).
- **Email attribute path**: defines which of the variables returned by the identity provider must be used to get the
  user's email address.
- **Fullname attribute path**: defines which of the variables returned by the identity provider must be used to get the
  user's full name.

</TabItem>
<TabItem value="Users manual management" label="Manual management">

On the **Configuration > Users > Contacts/Users** page, [create the users](../../managing-users-contacts/create-users-manually.md)
who will log on to the i-Vertix Monitoring using SAML.

</TabItem>
</Tabs>

### Step 5: Manage Authorizations

<Tabs groupId="sync">
<TabItem value="Role automatic management" label="Automatic management">

If you turn on **Enable automatic management**, users who log in to the i-Vertix Monitoring will be automatically
  [granted rights](../../managing-users-contacts/acl.md#granting-rights-to-a-user), as they will be linked to
  [access groups](../../managing-users-contacts/acl.md#creating-an-access-group) according to the rules you have defined.
  
- **Apply only first role**: If several roles are found for a specific user in the identity provider's information, then
  only the first role will be applied. If the option is turned off, all roles will be applied.
- Define which attribute from which endpoint will be used to retrieve values to create relationships with access groups.
- Match the attributes retrieved from the identity provider with the contact groups you want the user to belong to.

> Each time the user logs in, authorization management is reinitialized to take into account any new information from the
> identity provider.

</TabItem>
<TabItem value="Role manual management" label="Manual management">

If you turn off **Enable automatic management**, you will need to [grant users rights](../../managing-users-contacts/acl.md)
manually by linking them to [access groups](../../managing-users-contacts/acl.md#creating-an-access-group).

</TabItem>
</Tabs>

### Step 6: Manage Contact groups

<Tabs groupId="sync">
<TabItem value="Groups automatic management" label="Automatic management">

If you turn on **Enable automatic management**, users who log in to the i-Vertix Monitoring will be attached to the
[contact groups](../../managing-users-contacts/contact-groups.md) you have defined.

- Define which attribute from the identity provider will be used to retrieve values to create relationships with access groups.
- Match the attributes retrieved from the identity provider with the contact groups you want the user to belong to.

> Each time the user logs in, group management is reinitialized to take into account any new information from the identity provider.

</TabItem>
<TabItem value="Groups manual management" label="Manual management">

If you turn off **Enable automatic management**, you will have to manage the relationship between contact and
[contact groups](../../managing-users-contacts/contact-groups.md) manually.

</TabItem>
</Tabs>

### Step 7: Configure your Identity Provider (IdP)

Configure your identity provider so that the i-Vertix Monitoring can use the SAML protocol to authenticate your
users. Here is an example of fields you may have to fill in:

| IdP option                           | Value                                                 |
|--------------------------------------|----------------------------------------------------------------|
| Client ID                            | https://<Monitoring_IP_address>                                  |
| Assertion Consumer Service (ACS) URL | https://<Monitoring_IP_address>/centreon/api/latest/saml/acs     |
| Redirect Binding URLs for SLO        | https://<Monitoring_IP_address>/centreon/api/latest/saml/sls     |

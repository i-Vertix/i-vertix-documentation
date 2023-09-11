---
id: openid-OPENID
title: Configuring connection via OpenId Connect
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

i-Vertix is compatible with OAuth 2.0/OpenId Connect authentication.

Usage of Identity Providers (IdP) is available, such as Microsoft Azure AD, Okta, Keycloak, LemonLDAP::NG or other IdP
which are compatible with the Authorization Code Flow.

## Configure OpenID Connect authentication

Go to **Administration > Authentication > OpenID Connect Configuration**.

### Step 1: Enable authentication

Enable OpenID Connect authentication:

- **Enable OpenId Connect authentication**: enables or disables OpenId Connect authentication.
- **Authentication mode**: indicates if the authentication should be done using only OpenId Connect or using local
  authentication as well (**Mixed**). In mixed mode, users created manually in i-Vertix (and not identified via Open ID) will also be able to log in.

:::note

When setting the parameters, it is recommended to activate the "mixed" mode. This will allow you to retain access to the local `admin` account in the event of a misconfiguration.


:::

### Step 2: Configure Identity Provider access credentials

Configure Identity Provider information:

- **Base URL***: defines the identity provider's base URL for OpenId Connect endpoints (mandatory)
- **Authorization Endpoint***: defines the authorization endpoint, for example `/authorize` (mandatory)
- **Token Endpoint***: defines the token endpoint, for example `/token` (mandatory)
- **Client ID***: defines the Client ID (mandatory)
- **Client Secret***: defines the Client secret (mandatory)
- **Scopes**: defines the scopes of the identity provider, for example `openid`. Separate scopes by spaces

:::note

  Depending on the identity provider, it is necessary to enter several scopes in order to retrieve the claim which will identify users.
  
  This is indicated in the provider's configuration documentation.

:::

- **Login attribute path**: defines which of the variables returned by **Introspection Token Endpoint** or **User Information Endpoint**
  must be used to authenticate users. For example `sub` or `email`.
- **End Session Endpoint**: defines the logout endpoint, for example `/logout`.

Depending on your identity provider, set either of the following two endpoints:

- **User Information Endpoint**: defines the user information endpoint, for example `/userinfo`.
- **Introspection Token Endpoint**: defines the introspection token endpoint, for example `/introspect` (mandatory).

You can also configure:

- **Use Basic Auth for Token Endpoint Authentication**: the `Authorization: Basic` method will be used. Enable this option if your identity provider requires it.
- **Disable verify peer**: allows you to disable SSL peer validation. The identity provider's certificate will not be checked: use this option for test purposes only.

:::note

You can define a full URL for the endpoints in case the base of the URL is different from the others.

You can enable **Authentication debug** through the **Administration > Parameters > Debug** menu to understand authentication failures and improve your setup.

:::

### Step 3: Configure authentication conditions

* You can whitelist or blacklist IP addresses. If you leave the first two fields empty, all IP addresses will be authorized to access the i-Vertix interface.

   - **Trusted client addresses**: If you enter IP addresses in this field, only these IP addresses will be allowed to access the i-Vertix interface. All other IP addresses will be blocked. IP addresses must be separated by commas.
   - **Blacklist client addresses**: These IP addresses will be blocked. All other IP addresses will be allowed to access the i-Vertix interface.

* You can also define conditions according to which users will be allowed to log in or not, based on the data received by a particular endpoint.
   - Activate **Enable conditions on identity provider**.
   - Define which attribute from which endpoint will be used to validate the conditions.
   - In **Define authorized conditions values**, define which will be the authorized values returned by this endpoint. If you enter several values, all will have to be met for the condition to be validated. All users that try to connect with another value will be unable to log in.

   In the example below, the **Conditions attribute path** is **status** and **Define authorized conditions values** is **activated**. If the **Introspection endpoint** gives you the following response, then the user is allowed to log in:

   ```json
   {
   	   ...
   	   "name": "OpenId Connect OIDC",
	   "given_name": "OpenId Connect",
	   "family_name": "OIDC",
	   "preferred_username": "oidc",
	   "email": "oidc@localhost",
	   "email_verified": false,
	   ...
	   "status": "activated"
   }
   ```

:::caution

Currently, only character string values can be used.

:::

### Step 4: Manage user creation

<Tabs groupId="sync">
<TabItem value="Users automatic management" label="Automatic management">

If you turn on **Enable auto import**, users that log in to i-Vertix for the first time will be created in the i-Vertix configuration. (Turning the option on does not import automatically all users in your infrastructure.)

- **Enable auto import**: enables or disables automatic users import.  If auto import is disabled, you will have to [create each user manually](../../managing-users-contacts/create-users-manually.md) before they can log in.
- **Contact template**: select a [contact template](../../managing-users-contacts/contact-templates.md) that will be applied to newly imported users.
  This allows in particular to manage the default configuration of the [notifications](../../events-alerts/managing-notifications/configuring-notification.md).
- **Email attribute path**: defines which of the variables returned by **Introspection Token Endpoint** or **User Information Endpoint**
  must be used to get the user's email address.
- **Fullname attribute path**: defines which of the variables returned by **Introspection Token Endpoint** or **User Information Endpoint**
  must be used to get the user's full name.

</TabItem>
<TabItem value="Users manual management" label="Manual management">

On page **Configuration > Users > Contacts/Users**, [create the users](../../managing-users-contacts/contacts-users.md) that will log on to i-Vertix using OpenID.

</TabItem>
</Tabs>

### Step 5: Manage Authorizations

<Tabs groupId="sync">
<TabItem value="Role automatic management" label="Automatic management">

If you turn on **Enable automatic management**, users that log in to i-Vertix will be automatically [granted rights](../../managing-users-contacts/acl.md), as they will be linked to [access groups](../../managing-users-contacts/acl.md#creating-an-access-group) according to the rules you have defined.

- Define which attribute from which endpoint will be used to retrieve values for enforcing relationships with access groups.
- **Apply only first role**: If several roles are found for a specific user in the identity provider's information, then only the first role will be applied. If the option is turned off, all roles will be applied.
- Match an attribute retrieved from the identity provider with the access group you want the user to belong to.

For example, the **Introspection endpoint** gives you the following response and **Apply only first role** is enabled. The **Roles attribute path** will
be **realm_access.roles** and **Define the relation between roles and ACL access groups** will establish a relationship
between the value **centreon-editor** and a defined access group in i-Vertix:

```json
{
	...
	"realm_access": {
		"roles": ["centreon-editor", "centreon-admin", "user"]
	},
	...
}
```

::note

Each time the user logs in, authorization management is reinitialized to take into account any new information from the identity provider.

:::

</TabItem>
<TabItem value="Role manual management" label="Manual management">

If you turn off **Enable automatic management**, you have to [grant users rights](../../managing-users-contacts/acl.md) manually by linking them to [access groups](../../managing-users-contacts/acl.md#creating-an-access-group).

</TabItem>
</Tabs>

### Step 6: Manage Contact groups

<Tabs groupId="sync">
<TabItem value="Groups automatic management" label="Automatic management">

If you turn on **Enable automatic management**, users that log in to i-Vertix will be attached to the [contact groups](../../managing-users-contacts/contact-groups.md#contact-groups) you have defined.

- Define which attribute from which endpoint will be used to retrieve values to create relationships with access groups.
- Match the attributes retrieved from the identity provider with the contact groups you want the user to belong to.

For example, if the **Introspection endpoint** gives you the following response, the **Groups attribute path** will
be **groups** and **Define the relation between roles and contact groups** will define a relationship
between the value **Windows** and a defined contact group in i-Vertix, then between **Linux** and another contact group, etc:

```json
{
	...
	"groups": ["Windows", "Linux", "DBA"],
	...
}
```

:::note

Each time the user logs in, groups management is reinitialized to take into account any new information from the identity provider.

:::

</TabItem>
<TabItem value="Groups manual management" label="Manual management">

If you turn off **Enable automatic management**, you have to manage manually relation between contact and [contact groups](../../managing-users-contacts/contact-groups.md#contact-groups).

</TabItem>
</Tabs>

### Step 7: Configure your Identity Provider (IdP)

Configure your IdP to add the i-Vertix application to use the OpenID Connect protocol to authenticate your users,
and to authorize the following `redirect URI` to forward your connected users to i-Vertix:

```shell
{protocol}://{server}:{port}/centreon/authentication/providers/configurations/openid
```

:::note

Replace `{protocol}`, `{server}` and `{port}` by the URI to access to your i-Vertix server.

For example: `https://i-vertix.domain.net/centreon/authentication/providers/configurations/openid`

:::

## Examples of configuration

<Tabs groupId="sync">
<TabItem value="Microsoft Azure AD" label="Microsoft Azure AD">

Here is an example configuration for Microsoft Azure Active Directory:

| Fields                       | Values                                                    |
|------------------------------|-----------------------------------------------------------|
| Base Url                     | https://login.microsoftonline.com/${tenantId}/oauth2/v2.0 |
| Authorization Endpoint       | /authorize                                                |
| Token Endpoint               | /token                                                    |
| User Information Endpoint    | https://graph.microsoft.com/oidc/userinfo                 |
| End Session Endpoint         |                                                           |
| Scope                        | openid                                                    |
| Login claim value            | email                                                     |
| Client ID                    | ${clientId}                                               |
| Client Secret                | ${clientSecret}                                           |


:::info

Please replace `${tenantId}`, `${clientId}` and `${clientSecret}` with your own values.

:::

</TabItem>
<TabItem value="Okta" label="Okta">

Here is an example configuration for Okta:

| Fields                       | Values                                   |
|------------------------------|------------------------------------------|
| Base Url                     | https://${theIdPdomain}/oauth2/v1        |
| Authorization Endpoint       | /authorize                               |
| Token Endpoint               | /token                                   |
| Introspection Token Endpoint | /introspect                              |
| User Information Endpoint    | /userinfo                                |
| End Session Endpoint         | /logout                                  |
| Scope                        | profile openid                           |
| Login claim value            | username                                 |
| Client ID                    | ${clientId}                              |
| Client Secret                | ${clientSecret}                          |


:::info

Please replace `${theIdPdomain}`, `${clientId}` and `${clientSecret}` with your own values.


:::

</TabItem>
<TabItem value="Keycloak" label="Keycloak">

Here is an example configuration for Keycloak:

| Fields                       | Values                                                                  |
|------------------------------|-------------------------------------------------------------------------|
| Base Url                     | https://${theIdPdomain}:8080/auth/realms/master/protocol/openid-connect |
| Authorization Endpoint       | /auth                                                                   |
| Token Endpoint               | /token                                                                  |
| Introspection Token Endpoint | /token/introspect                                                       |
| User Information Endpoint    |                                                                         |
| End Session Endpoint         | /logout                                                                 |
| Scope                        | openid                                                                  |
| Login claim value            | email                                                                   |
| Client ID                    | ${clientId}                                                             |
| Client Secret                | ${clientSecret}                                                         |


:::info

Please replace `${theIdPdomain}`, `${clientId}` and `${clientSecret}` with your own values.


:::

</TabItem>
<TabItem value="LemonLDAP::NG" label="LemonLDAP::NG">

Here is an example configuration for LemonLDAP::NG:

| Fields                       | Values                                   |
|------------------------------|------------------------------------------|
| Base Url                     | http://auth.example.com/oauth2           |
| Authorization Endpoint       | /authorize                               |
| Token Endpoint               | /token                                   |
| Introspection Token Endpoint | /introspect                              |
| User Information Endpoint    | /userinfo                                |
| End Session Endpoint         |                                          |
| Scope                        | openid                                   |
| Login claim value            | email                                    |
| Client ID                    | ${clientId}                              |
| Client Secret                | ${clientSecret}                          |


:::info
Please replace `auth.example.com`, `${clientId}` and `${clientSecret}` with your own values.


:::

</TabItem>
<TabItem value="Others" label="Others">

Most of the service providers have one URL presenting the configuration parameters configuration as defined by
[the protocol](https://openid.net/specs/openid-connect-discovery-1_0#ProviderConfig).

```json
{
	"issuer": "https://server.example.com",
	"authorization_endpoint": "https://server.example.com/connect/authorize",
	"token_endpoint": "https://server.example.com/connect/token",
	"token_endpoint_auth_methods_supported": ["client_secret_basic", "private_key_jwt"],
	"token_endpoint_auth_signing_alg_values_supported": ["RS256", "ES256"],
	"userinfo_endpoint": "https://server.example.com/connect/userinfo",
	"check_session_iframe": "https://server.example.com/connect/check_session",
	"end_session_endpoint": "https://server.example.com/connect/end_session",
	"jwks_uri": "https://server.example.com/jwks.json",
	"registration_endpoint": "https://server.example.com/connect/register",
	"scopes_supported": ["openid", "profile", "email", "address", "phone", "offline_access"],
	"response_types_supported": ["code", "code id_token", "id_token", "token id_token"],
	"acr_values_supported": ["urn:mace:incommon:iap:silver", "urn:mace:incommon:iap:bronze"],
	"subject_types_supported": ["public", "pairwise"],
	"userinfo_signing_alg_values_supported": ["RS256", "ES256", "HS256"],
	"userinfo_encryption_alg_values_supported": ["RSA1_5", "A128KW"],
	"userinfo_encryption_enc_values_supported": ["A128CBC-HS256", "A128GCM"],
	"id_token_signing_alg_values_supported": ["RS256", "ES256", "HS256"],
	"id_token_encryption_alg_values_supported": ["RSA1_5", "A128KW"],
	"id_token_encryption_enc_values_supported": ["A128CBC-HS256", "A128GCM"],
	"request_object_signing_alg_values_supported": ["none", "RS256", "ES256"],
	"display_values_supported": ["page", "popup"],
	"claim_types_supported": ["normal", "distributed"],
	"claims_supported": ["sub", "iss", "auth_time", "acr",
		"name", "given_name", "family_name", "nickname",
		"profile", "picture", "website",
		"email", "email_verified", "locale", "zoneinfo",
		"http://example.info/claims/groups"
	],
	"claims_parameter_supported": true,
	"service_documentation": "http://server.example.com/connect/service_documentation",
	"ui_locales_supported": ["en-US", "en-GB", "en-CA", "fr-FR", "fr-CA"]
}
```

Retrieve the following parameters to configure your i-Vertix:

- issuer (Base Url)
- authorization_endpoint
- token_endpoint
- userinfo_endpoint
- end_session_endpoint
- scopes_supported
- claims_supported (Login claim value)

</TabItem>
</Tabs>
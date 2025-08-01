---
id: other
title: Other
---

# Other external authentication methods

The integration of i-Vertix ITAM and authentication sources beyond internal,
LDAP, and IMAP is configured from the **Setup \> Authentication \> Other
authentication methods** menu.

## Central Authentication Service (CAS) 

The configuration of a CAS server is comprised on the address of the
server and its port (default 443). A base directory can be specified if
needed. The return web address parameter allows you to redirect the user
to a specific page after they log out from i-Vertix ITAM.

:::warning

Once the CAS authentication is activated, each authentication is
automatically redirected to the CAS server. In order to log into an
internal account or one authenticated through a different method, you
have to add "?noAUTO=1" to the login URL.

:::

:::info

The [php-curl] or [php-dom] extensions are
required to be enabled for CAS authentication to function.

:::

## x509 certificate 

The **Email attribute for x509 authentication** tells i-Vertix ITAM to look at
the value of this attribute in the SSL_CLIENT_S_DN HTTP request variable
passed by the authentication system.

It is possible to restrict the accepted values for the O, OR, and CN
fields of the client certificate. In order to specify multiple values
for each field, you may separate each value with the *\$* symbol.

## Other automatic authentications 

i-Vertix ITAM can rely on other external systems to authenticate users such as:

- Basic Apache authentication
- Windows domain authentication
- Authentication coming from an authentication server like
  LemonLDAP::NG, Shibboleth, etc

When the user wishes to reach i-Vertix ITAM, this one checks the presence of a
variable in the HTTP headers storing the login/username. If the variable
is present, the authentication is allowed to be done. We can map the
*data transmitted by the authentication system* with the *fields of the
user account of i-Vertix ITAM* (name, first name, email, language...). To
finish, the controls of authorizations are carried out. An option allows
to remove the domain of the user's login (Ex: testuser@example.com>
testuser).

:::info

The list of possible names for the headers is configurable, although
the most common ones are already provided by i-Vertix ITAM. See [Configuring headings](/modules/configuration/dropdowns/index).

:::

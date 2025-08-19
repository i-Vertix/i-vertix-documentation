---
id: index
title: Index
---

# Authentication

This is where i-Vertix ITAM manages the authentication and information of users.

i-Vertix ITAM uses its own internal database of users. These are either created
in i-Vertix ITAM itself or imported from one or more external sources. Depending
on the type of source, the import can be done in bulk or at the time of
login if the user is not yet known to i-Vertix ITAM but exists in an external
authentication server with matching credentials.

The general authentication configuration and the management of external
authentication servers can be done in the
[Setup > Authentication menu](../../../modules/configuration/authentication/configuration).

The attribution of authorizations is described in the
[Rules for assigning authorizations to a user](../../../modules/administration/rules/userauthorizations) documentation.

:::info

The authentication process is as follows:

1.  A user enters their login and password in i-Vertix ITAM
2.  i-Vertix ITAM checks if the user is already registered in its database and
if not:
1.  i-Vertix ITAM tries the configured methods of authentication one after
another (Internal \> LDAP \> IMAP \> Other)
2.  When the authentication is successful, the user is created in
the i-Vertix ITAM database and the method of authentication is stored
with it
3.  If no method of authentication is able to authenticate the
user, they are shown an error indicating that their username
or password is incorrect
3.  If the user already existed in the i-Vertix ITAM database or was imported
in the previous step:
1.  i-Vertix ITAM tries authenticating the user only with the last source
that was able to successfully authenticate them
2.  If the authentication fails, they are shown an error
indicating that their username or password is incorrect
4.  The authorization engine is launched with the user's information:
1.  If the engine has granted one or more authorizations to the
user, then that user has access to i-Vertix ITAM
2.  If the user is not granted any authorizations, then the user
will be known to i-Vertix ITAM but will not be able to login

:::

In order to use an external source of authentication you may need to
enable the relevant PHP extension(s). For example, LDAP sources will
require the [php-ldap] extension.

There is no limit to the number of authentication sources that can be
configured.

To allow i-Vertix ITAM to create users automatically from external authentication
sources as they try to log in, it must be enabled in the **Setup \>
Authentication \> Setup** form. When using LDAP directories, it is
possible to configure the action that i-Vertix ITAM takes when a user is no
longer present in the LDAP directory from this same form.

- [Configuration](./configuration/)
- [Ldap](./ldap/)
- [Imap](./imap/)
- [Other](./other/)

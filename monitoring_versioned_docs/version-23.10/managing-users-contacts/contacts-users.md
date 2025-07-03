---
id: contacts-users
title: Contacts/Users
---

In i-Vertix IT Monitoring, users can:

* Receive [notifications](../events-alerts/managing-notifications/configuring-notification.md).
* Log in to the i-Vertix Central Manager web interface: each user has their own [rights](acl.md) to connect to the web interface.

You can:

* [Create users manually](create-users-manually.md)
* [Connect your i-Vertix IT Monitoring to an LDAP directory](../administration/authentication/ldap)
* [Connect your i-Vertix IT Monitoring to an IDP using SAML](../administration/authentication/saml)
* Make customizations:
  * Switch to dark mode
  * Change the user interface language
  * Change the timezone
  * Reset the password
  * Define a default page after login

## Unblock users

The access to the monitoring interface is blocked for a user failing several times to log in (the number of attempts is set by the administrator). As soon as a user is blocked, a new column named **Unblock** appears in the **Configuration > Users > Contacts / Users** page, and you can see a red padlock at the blocked user's level.

1. Click on the red padlock.
2. Confirm you action.

The user is now unblocked and can connect to Centreon again.

:::note

It is also possible, that the user was blocked by the Fail2Ban service.
Please refer to the [Fail2Ban documentation](../installation/security-aspects/fail2ban.md) for further information.

:::

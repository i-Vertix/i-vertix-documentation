---
id: access-glpi
title: Access Glpi
---

# Administering access controls

This section describes how to administer the access control system that
allows each user to access a specific context of use.

In i-Vertix ITAM each user does not have access to the same interface nor to the
same same functionalities. For each user, a specific context of use is
determined, which grants them access only to the functionalities and
information that is needed. Access to identity information about the
user allows us to determine his or her authorizations.

The first step is to configure the desired authentication method(s).
i-Vertix ITAM is able to manage user authentication and information completely
locally in its database, however it is recommended to delegate the
authentication to an external service like LDAP. See
[Configuring authentication methods](/asset-management/modules/configuration/authentication) for more information.

The import or creation of new users and management of users known to
i-Vertix ITAM including deletion, syncronization, activation/deactivation and
management of information such as email, phone, etc is covered in
[the user administration documentation](/asset-management/modules/administration/users).

A user can associated with groups, entities, and profiles which are the
means of determining usage contexts.

Groups allow users to be grouped according to similarities in skills or
organizational units. See
[Administering groups](/asset-management/modules/administration/groups) for more information.

Entities allow you to segment your asset fleet, help desk, etc into
departments that are isolated from each other. See
[Administering entities](/asset-management/modules/administration/entities) for more information.

Profiles are sets of permissions that can be granted to users. Multiple
profiles can be given to a user but only one can be active at a time.
See
[Administering profiles](/asset-management/modules/administration/profiles) for more information.

Finally, you can configure
[Rules for assigning authorizations to a user](/asset-management/modules/administration/rules/userauthorizations) to dynamically assign entities, groups and profiles to
users.

---
id: actors
title: Actors
---

# Defining actors and roles

An assistance service usually defines the following roles:

- **Requester** : user or group of users known to i-Vertix ITAM and affected by
  the ticket;
- **Technician**: ticket processing is done by a technician, by a group
  or by a supplier;
- **Watcher** : user who can follow a ticket but without modifying it;
  follow-up can be done from i-Vertix ITAM interface or by receiving
  notifications.

Visible information and possible actions are defined by i-Vertix ITAM based on
the user's role, which is defined in user's profile:

- Technicians are the actors having the most complete information on a
  ticket and the widest possible actions
- Requester and watcher will only view the information needed to fulfill
  request.

For multiple users or groups, only the first user or group is defined
when creating the ticket, more actors are added later. A user who cannot
modify actors but able to see the ticket can become a watcher.

When associating a new actor to a ticket, the number of tickets assigned
to this actor is visible; this eases for instance task partitioning
between technicians.
:::note

- for users who are not known to i-Vertix ITAM, mail address can be associated to
  a ticket. Default choice for requester and watcher (no selected user)
  allows to add a mail address in these fields; for this to be
  available, notifications must be activated (see
  [notification management](configure_notifications))
- Role attribution is done in user's authorization management (see
  [Attribute authorizations to a user](/asset-management/modules/administration/rules/userauthorizations))
:::

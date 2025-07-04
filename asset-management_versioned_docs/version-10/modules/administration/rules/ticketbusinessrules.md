---
id: ticketbusinessrules
title: Ticketbusinessrules
---

orphan

:   

# Business rules for tickets

A mechanism is available to modify the attributes of the ticket
automatically when a ticket is opened or updated.

The available criteria are all the attributes of the ticket (title,
description, status, category, urgency, impact, priority, source of the
request, type of asset, group/user/location requesters, assigned to
supplier/group/technician, type of asset, entity) as well as others
related to email collectors (headers ...).

The possible actions are to modify certain attributes of the ticket
(status, category, urgency, impact, priority, requesters
group/user/location, assigned to supplier/group/ technician). It is also
possible to assign a ticket to a device according to data present in the
ticket (attribution on the IP address, the full name and the domain, the
MAC address) or even send a validation request.

When using i-Vertix ITAM in multi-entities, the business rules for the tickets
can be recursive, i.e. they can be defined on an entity with an
application on the entity itself and on the sub-entities.

Three tabs are available:

- **applied rules (entity name)**: all the rules of the parent entities
  played (only if you have the authorization *Business rules (parent)*
  on the authorization *Business rules for tickets (entity)*;
- **local rules**: the list of rules defined for the current entity;
- **rules applicable in sub-entities**: all the rules applied after
  those of the current entity.

:::warning

Special case for the Emergency and Impact fields

If you define an emergency and/or an impact via a business rule, you
should also consider adding the *Recalculate priority* action so that
it is based on the fields you have just defined.

:::

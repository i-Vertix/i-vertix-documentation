---
id: ticketadvanced
title: Ticketadvanced
---

# To go further

## Tickets categories

See [Categories](/asset-management/modules/assistance/categories)

## Tickets templates

Using ticket templates, it is possible to customize ticket creation form
by masking, pre-defining or making mandatory some fields.

See [Ticket templates](/asset-management/modules/overview/templates)

## Collectors

External tools can interact with assistance module using mail
collectors.

Email is used to create tickets and add follow-up to existing tickets. A
i-Vertix ITAM internal task will connect to a mailbox and fetch messages.

:::info

The solution or closure of a ticket are not available via collectors.

:::

A mail message will go through the following steps:

- Mail box;
- Collector, configured using
  [Configure collectors](/asset-management/modules/configuration/collectors);
- Rules, see Assigned a ticked opened by mail to an entity
- Business rules, see
  [Business rules for tickets](/asset-management/modules/administration/rules/ticketbusinessrules)
- Ticket is created

An answer to a mail coming from i-Vertix ITAM will go through the following
steps:

- Mail box;
- Collector ;
- Creation of a follow-up for concerned ticket.

## Recurrent tickets

See
[Recurrent tickets](/asset-management/modules/assistance/tickets/recurrentticket)

## Attached costs

See
[Attached costs](/asset-management/modules/assistance/tickets/ticketmanagement)

## Links between tickets

It is possible to define links between tickets or to mark tickets as
duplicates.

See
[Links between tickets](/asset-management/modules/assistance/tickets/ticketmanagement)

## Processing time

Incidents resolution delays or SLA can be configured.

See
[Configure SLAs](/asset-management/modules/assistance/tickets/modules/configuration/service_levels).

## Business rules

Business rules can be defined to modify and assign tickets.

See
[Business rules for tickets](/asset-management/modules/administration/rules/ticketbusinessrules).

## Administrative closure

Administrative closure moves the status of a ticket from *Solved* to
*Closed*.

ITIL best practices recommends a validation of the solution by the
ticket requester, who validates that the answer provided by the
technician corresponds to the demand. However, if the requester does not
fulfill this validation, it is possible to parameterize an
administrative closure after a delay which can be configured at entity
level (see
[Assistance tab](/asset-management/modules/administration/entities)). If this delay is set to zero, the ticket is automatically
closed.

## Satisfaction

(I can't get no)

A satisfaction survey is triggered when the ticket status is set to
*Closed* and the triggering delay is elapsed. This triggering delay is
parameterized at entity level (see
[Delegate administration at entity level](/asset-management/modules/administration/entities)).

:::info

The automatic task that triggers the survey must be activated.

:::

When ticket is closed, a notification that includes a link to the
satisfaction survey can be sent to the requester. The requester will
also have access to the survey from the ticket form in tab
[Satisfaction].

The requester can then select the satisfaction level (from 0 to 5, given
as stars) about the ticket solution. A comment can also be added.

Statistics on surveys are available in
[statistics](/asset-management/modules/assistance/statistics).
:::note

- the requester can change the answer to the satisfaction survey within
  a delay of 12 hours after first answer
- a notification can be sent when satisfaction survey is generated, but
  also on each answer to this survey
:::

## See also

See
[Advanced configuration](/asset-management/modules/assistance/categories).

---
id: ticketlifecycle
title: Ticketlifecycle
---

# Ticket life cycle

Ticket life cycle is defined at *profile* level in a
[life cycle matrix](../../../modules/assistance/lifecyclematrix.md). To display a life cycle and modify it, it is therefore done
in profile management form (menu **Administration \> Profiles**).

## Ticket types

i-Vertix ITAM tickets are either incidents or requests, this type being stored in
field *Type* of the ticket. This type field allows to perform actions
based on ticket type (see
[business rules for tickets modification and assignment](../../../modules/administration/rules/ticketbusinessrules.md),
[ticket templates](../../../modules/overview/templates.md) and
[problem management](../../../modules/assistance/problems.md)) and to customize the list of available categories.

## Status

ITIL defines a standard for ticket status life cycle. This status life
cycle is implemented in i-Vertix ITAM by defining the following status:

- New
- Processing (assigned)
- Processing (planned)
- Pending
- Solved
- Closed

These status can neither be parameterized nor modified.

:::info

It is therefore possible to hide some status according to profile (see
[Life cycle matrix](../../../modules/assistance/lifecyclematrix.md)).\*

:::

To go further in status management, refer to
[ticket templates](../../../modules/overview/templates.md) and
[business rules for tickets modification and assignment](../../../modules/administration/rules/ticketbusinessrules.md).

## Scheduling

Ticket scheduling is done according to data provided by the requester
and the technician:

- Requester defines urgency
- Technician appreciates the impact

Priority results from these two values. It is computed automatically
using a matrix and provides the true importance of the ticket.

:::info

To go further on this matrix configuration, see
[Define the matrix of calculus for priority](../../../modules/assistance/prioritymatrix.md).

:::

## Management rules

The ticket status follows the following process:

- upon creation, the ticket has status **New**
- when a technician assigns ticket processing to a group, a technician
  or a supplier, the ticket goes to status **Processing (assigned)**
- when a new task is added to the ticket and is planned, ticket status
  become then **Processing (planned)**
- when a solution is found for the ticket, its status become **Solved**
- at last, then requester or writer validates the proposed solution, the
  ticket status is **Closed**
:::note

- Technician can change ticket status at every moment, in particular to
  put the ticket to **Pending**. Following ITIL recommendations, a
  ticket must be made **Pending** only by the requester, for example if
  request is not complete or if requester is not available for an
  intervention
- Requester can delete the ticket as long as the ticket status is
  **New** and no action has been done on the ticket
:::

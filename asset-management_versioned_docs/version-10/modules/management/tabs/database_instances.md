---
id: database_instances
title: Database Instances
---

# Database instances

A database instance groups together all the databases retrieved from the
same server (for example, all the databases in a MySQL instance).

![Bdd instances - global view](../../../assets/modules/management/images/bdd_instances_view.png)

:::info

These instances can be added using the automatic inventory or manually

:::

:::tip

Note that if you modify a field manually, it will be considered
locked. This will prevent it from being modified the next time the
automatic inventory is uploaded.

For more information, see
[lock](../../../modules/assets/tabs/locks)

:::

In a database instance form, the following information is available:

![Bdd instances - details view](../../../assets/modules/management/images/bdd_instances_details_view.png)

- Item type : defines the **type of item** on which the database is
  installed
- Item : Defines the **item** on which the database installed
- Name
- [Status](../../../tabs/common_fields/status.md)
- Associable to a ticket : Yes / Note
- [Location](../../../tabs/common_fields/location.md)
- [Database instance type](../../../tabs/common_fields/asset_type.md) (MySQL, PostgreSQL, MariaDB, etc.)
- [Technician in charge](../../../tabs/common_fields/technician_in_charge.md)
- [Manufacturer](../../../tabs/common_fields/manufacturer.md)
- [User](../../../tabs/common_fields/user.md)
- Version
- [Comments](../../../tabs/common_fields/comments.md)
- [Update source](../../../tabs/common_fields/update_source.md)
- Active : Yes / No
- Database instance category
- Has backup : Yes/No
- Last backup date :\*date\*
- Port
- Path

## Impact Analysis

[Impact analysis](../../../tabs/impact_analysis.md) enables an infrastructure diagram to be drawn up, showing
the dependencies and impacts in the event of equipment loss. This can be
saved and exported

## Databases

[Databases](../../../modules/management/databases.md) lists all the
databases present on the instance

## Management

[Management](../../../modules/tabs/management.md) of
financial and administrative information, this information is visible in
the 'Management' tab on the current item's form.

## Contracts

i-Vertix ITAM supports [contracts](../../../modules/management/contract.md)
management, in order to manage contract types such as loan, maintenance,
support...

Contracts management allows to:

- make an inventory of all contracts related to the organization assets
- integrate contracts in i-Vertix ITAM financial management
- anticipate and follow contract renewal.

## Documents

The [document](../../../modules/management/documents.md) tab lets you
link different types of file to the current item (PDF, txt, png, etc.)

You can attach a document already uploaded to i-Vertix ITAM or add a new one
directly from this tab.

## Knowledge Base

Lists all the articles in the
[knowledge base](../../../tabs/knowledgebase.md) relating to the current item.

## Tickets

View all [tickets](../../../modules/tabs/tickets.md)
linked to the current item

## Problems

This tab refers to all hardware-related
[problems](../../../modules/assistance/problems.md).
Problems can also be linked to tickets, projects, etc. This allows you
to have a complete scenario when necessary.

## Changes

[Changes](../../../modules/assistance/changes.md) lists
all changes related to the current item. From this tab, you can't link
a change directly, you can do it from **Assistance** \> **Changes** \>
**Items**.

You can create a new change from this page, which will be linked to the
current item you have selected.

## Links

[Links](../../../modules/configuration/external_links.md) offer several possibilities. Send the i-Vertix ITAM object file to
another URL of your choice, or generate an RDP file, for example.

## Certificates

Link a
[certificate](../../../modules/management/certificates.md) to your registration. You can manage certificates in
**Management** \> **Certificates**

## Locks

[Locks](../../../modules/assets/tabs/locks.md) are
used to prevent a field from being modified when the inventory is
uploaded. You can lock/unlock the fields you wish in a i-Vertix ITAM item.

## Notes

[Note](../../../modules/tabs/notes.md) lets you add
rich-text text and attach a document.

## Domains

You can attach [Domains](../../../modules/management/domains.md) to the current item. Domains are also linked to other items
such as records, problems, etc.

## Appliances

[Appliances](../../../modules/management/appliance.md) includes all business applications managed within i-Vertix ITAM. They
can be linked to another i-Vertix ITAM item (computer, application, etc.) as well
as to another appliance.

## History

The *History* tab is used to show any changes made to an item. The
following information about the changes is available:

- ID of the change.
- Date and time the change was made.
- User who made the change. If this field is not filled, it means that
  the action was done automatically (For example: automatic inventory
  update).
- Field that was changed.
- Description of the change that was made.

The description of the change represents either the difference between
the old and the new value (For example with location field: Change HQ to
Remote Office A), or the explanation of the action which was carried out
(For example: Uninstallation of a software: "Gimp 2.0").

:::info

For dropdowns or objects with a parent/child relationship, the
modification of a child will appear in the history of the parent
element.

:::

## All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

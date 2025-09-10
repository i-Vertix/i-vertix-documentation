---
id: databases
title: Databases
---

# Databases

Databases list databases discovered by automatic inventory and those
entered manually.

![General view databases](../../assets/modules/management/images/databases-view.png)

Databases can be grouped into
[instances](../../modules/management/tabs/database_instances.md). An
instance groups together all the databases retrieved from the same
server (for example, all the databases in a MySQL instance). This data
can also be retrieved by automatic inventory or entered manually

## Database

![Edit database](../../assets/modules/management/images/databases-edit.png)

- **Name**
- **Active** : Yes/No
- **Database instance** : determines the database instance
- Size (Mio)
- Has backup: Yes/No
- Last backup date: *date*

## Management

[Management](../../modules/tabs/management.md) of
financial and administrative information, this information is visible in
the 'Management' tab on the item's form.

## Documents

The [document](../../modules/management/documents.md) tab lets you link different types of file to the current
item (PDF, txt, png, etc.)

You can attach a document already uploaded to i-Vertix ITAM or add a new one
directly from this tab.

## Knowledge Base

Lists all the articles in the
[knowledge base](../../tabs/knowledgebase.md)
relating to the current item.

## Tickets

View all [tickets](../../modules/tabs/tickets.md)
linked to the current item.

## Problems

This tab refers to all related
[problems](../../modules/assistance/problems.md).

Problems can also be linked to tickets, projects, etc. This allows you
to have a complete scenario when necessary.

## Changes

[Changes](../../modules/assistance/changes.md)
lists all changes related to the current item. From this tab, you can't
link a change directly, you can do it from **Assistance** \> **Changes**
\> **Items**.

You can create a new change from this page, which will be linked to the
current item you have selected.

## Notes

[Note](../../modules/tabs/notes.md) lets you add
rich-text and attach a document.

## Domains

You can attach [Domains](../../modules/management/domains.md) to the current item. Domains are also linked to other items
such as records, problems, etc.

## Appliances

[Appliances](../../modules/management/appliance.md) include all business applications managed within i-Vertix ITAM and
linked with the current item.

to them. They can also be linked to another i-Vertix ITAM object (computer,
application, etc.) as well as to another appliance.

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

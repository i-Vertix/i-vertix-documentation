---
id: domains_records
title: Domains Records
---

# Domains records

![List of attached records](../../assets/modules/management/images/domains-records.png)

# The different tabs

## Impact Analysis

[Impact analysis](../../tabs/impact_analysis.md)
enables an infrastructure diagram to be drawn up, showing the
dependencies and impacts in the event of equipment loss. This can be
saved and exported

## Records

A Record object stores all record types that can be found in a DNS zone
or DNS configuration file: TXT, A, PTR, SDA, CNAME...

This object must be associated to a Domain object.

You can add an existing record (in Link a record field) or create a new
one.

- To add a new record, click on **+Add**
- Enter the differents fields
  - Name
  - Record type
  - Technician in charge
  - Group in charge
  - Creation date
  - TTL
  - Data
- Click on **+Add**

:::info

Record types are not limited to the default ones and can be customized
using drop-down management.

:::

## Tickets

View all [tickets](../../modules/assistance/tickets.md) linked to the computer

## Problems

This tab refers to all hardware-related
[problems](../../modules/assistance/problems.md).
Problems can also be linked to tickets, projects, etc. This allows you
to have a complete scenario when necessary.

## Documents

The [document](../../modules/management/documents.md) tab lets you link different types of file to a material
(PDF, txt, png, etc.) You can attach a document already uploaded to i-Vertix ITAM
or add a new one directly from this tab.

## Links

[Links](../../modules/configuration/external_links.md)
offer several possibilities. Send the i-Vertix ITAM object file to another URL of
your choice, or generate an RDP file, for example.

## Note

The [Notes](../../modules/tabs/notes.md) tab
provides a free text field for storing additional information. Notes are
displayed in the order of their creation. You can also add a document

# History

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

# All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

---
id: enclosures
title: Enclosures
---

# Enclosures

An enclosure is a type of equipment used to manage modular
infrastructures, such as blade servers, storage bays or certain network
equipment.

It enables several physical elements to be grouped together in the same
box, while retaining individual management of the components.

:::info

It is possible to use
[templates with enclosure](../../modules/overview/templates.md).

:::

![Global view enclosure](../../assets/modules/assets/images/enclosure_global_view.png)

When you add an enclosure (by **+ Add** at the top of the screen), you
can add certain information:

- Name
- [Location](../../tabs/common_fields/location.md)
- [Technician in charge](../../tabs/common_fields/technician_in_charge.md)
- [Manufacturer](../../tabs/common_fields/manufacturer.md)
- [Serial number](../../tabs/common_fields/serial_number.md)
- [User](../../tabs/common_fields/user.md)
- Power Supplies (number of power supplies)
- [Status](../../tabs/common_fields/status.md)
- [Technician in charge](../../tabs/common_fields/technician_in_charge.md)
- [Model](../../tabs/common_fields/model.md)
- [Inventory number](../../tabs/common_fields/inventory_number.md)
- [Comments](../../tabs/common_fields/comments.md)

## Impact Analysis

[Impact analysis](../../tabs/impact_analysis.md) enables an infrastructure diagram to be drawn up, showing
the dependencies and impacts in the event of equipment loss. This can be
saved and exported

## Items

[Items](../../modules/assets/tabs/enclosures_items.md) lists all
the elements present in the chassis. This operation must be carried out
manually.

## Components

Enclosure has specific
[Setup > Components](../../modules/configuration/components) compared with other equipment since this is rather passive
equipment that contains no software, firmware, etc.

You can add a :

- Generic device
- PCI device
- Power supply.

## Network Ports

This tab allows to manage the
[network ports](../../tabs/network_ports.md)
attached to an equipment. The information that can be viewed is:

- Name
- Port number
- MTU
- Speed
- Internal status
- Last change
- Number of I/O bytes
- Number of I/O errors
- Duplex
- VLAN
- Connected to
- Connection
- Deleted

## Management

[Management](../../modules/tabs/management.md) of financial and administrative information, this
information is visible in the 'Management' tab on the enclosure's
form.

## Contracts

i-Vertix ITAM supports [contracts](../../modules/management/contract.md) management, in order to manage contract types such as loan,
maintenance, support...

Contracts management allows to:

- make an inventory of all contracts related to the organization assets
- integrate contracts in i-Vertix ITAM financial management
- anticipate and follow contract renewal.

## Documents

The [document](../../modules/management/documents.md)
tab lets you link different types of file to current item (PDF, txt,
png, etc.)

You can attach a document already uploaded to i-Vertix ITAM or add a new one
directly from this tab.

## Tickets

View all [tickets](../../modules/tabs/tickets.md)
linked to the enclosure

## Problems

This tab refers to all hardware-related
[problems](../../modules/assistance/problems.md).
Problems can also be linked to tickets, projects, etc. This allows you
to have a complete scenario when necessary.

## Changes

[Changes](../../modules/assistance/changes.md) lists
all changes related to a material. From this tab, you can't link a
change directly, you can do it from **Assistance** \> **Changes** \>
**Items**. You can create a new change from this page, which will be
linked to current item.

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

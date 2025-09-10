---
id: monitors
title: Monitors
---

# Monitors

Each monitor has its own information (connections, contrats, network
ports, etc.). All this information is divided into tabs. You can find
your computers in **Assets \> Monitors**:

![module assets - monitor](../../assets/modules/assets/images/global_view.png)

:::tip

Note that if you modify a field manually, it will be considered
locked. This will prevent it from being modified the next time the
automatic inventory is uploaded.

For more information, see
[lock](../../modules/assets/tabs/locks)

:::

In a display form, the following information is available:

- Name
- [Location](../../tabs/common_fields/location.md)
- [Technician in charge](../../tabs/common_fields/technician_in_charge.md)
- [Group in charge](../../tabs/common_fields/group_in_charge.md)
- [Alternate usernmame number](../../tabs/common_fields/alternate_username.md)
- [Alternate usernmame](../../tabs/common_fields/alternate_user.md)
- [User](../../tabs/common_fields/user.md)
- [Group](../../tabs/common_fields/group.md)
- Size
- [UUID](../../tabs/common_fields/uuid.md)
- [Update source](../../tabs/common_fields/update_source.md)
- [Status](../../tabs/common_fields/status.md)
- [Monitor type](../../tabs/common_fields/asset_type.md)
- [Manufacturer](../../tabs/common_fields/manufacturer.md)
- [Model](../../tabs/common_fields/model.md)
- [Serial number](../../tabs/common_fields/serial_number.md)
- [Inventory number](../../tabs/common_fields/inventory_number.md)
- [Network](../../tabs/common_fields/network.md)
- [Management type](../../tabs/common_fields/management_type.md)
- [Comments](../../tabs/common_fields/comments.md)
- [Ports](../../tabs/common_fields/ports.md)

**Management type:**

It is possible to manage displays either unitary or globally.

Unitary management corresponds to one display per computer while global
management make the printer a virtual global element that will be
connected to several computers.

Global management allows to limit the number of elements to manage when
these elements are not a strategic data in the assets management.

It is possible to use
[templates with displays](../../modules/overview/templates.md).

## Impact Analysis

[Impact analysis](../../tabs/impact_analysis.md) enables an infrastructure diagram to be drawn up, showing
the dependencies and impacts in the event of equipment loss. This can be
saved and exported

## Operating systems

[Operating systems](../../tabs/operating_systems.md) includes information about your machine's OS :

- Name
- Version
- Architecture
- Service Pack
- Kernel
- Edition
- Product ID
- Serial number
- Company
- Owner
- Host ID
- Installation date

## Software

Lists all the [software](../../tabs/software.md) brought up during the inventory and those added manually

It is possible to install (in the logical sense) software on a PC
manually.

To add new [software](../../modules/assets/softwares.md) to the list of applications, you need to go to the Assets \>
Software tab, which will then be visible from the software tab of the
various elements of the installed base.

## Connections

The [connections](../../tabs/connections.md)
are all the other hardware connected to the machine :

- [Computer](computer.html)
- Other asset you have created

These items can be updated by the automatic inventory, but you can also
connect them manually.

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
information is visible in the 'Management' tab on the computer's
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
tab lets you link different types of file to a material (PDF, txt, png,
etc.) You can attach a document already uploaded to i-Vertix ITAM or add a new
one directly from this tab.

## Knowledge Base

Lists all the articles in the
[knowledge base](../../tabs/knowledgebase.md) relating to the material.

## Tickets

View all [tickets](../../modules/tabs/tickets.md)
linked to the computer

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
linked to the material you have selected.

## Links

[Links](../../modules/configuration/external_links.md)
offer several possibilities. Send the i-Vertix ITAM object file to another URL of
your choice, or generate an RDP file, for example.

## Locks

[Locks](../../modules/assets/tabs/locks.md) are
used to prevent a field from being modified when the inventory is
uploaded. You can lock/unlock the fields you wish in a i-Vertix ITAM object.

## Notes

[Note](../../modules/tabs/notes.md) lets you add
enriched text and attach a document.

## Reservations

The [reservation](../../modules/tools/reservations.md) tab lets you reserve equipment, view the reservation
schedule, or cancel the possibility of reserving this equipment. By
default, equipment cannot be reserved; you must first authorize this
action manually.

## Domains

You can attach [Domains](../../modules/management/domains.md) to your computer. Domains are also linked to other objects
such as records, problems, etc.

## Appliances

[Appliances](../../modules/management/appliance.md) includes all business applications managed within i-Vertix ITAM. They
can be linked to another i-Vertix ITAM object (computer, application, etc.) as
well as to another appliance.

## Databases

Databases list databases discovered by automatic inventory and those
entered manually

## Import information

Import information is information that is uploaded and governed by
equipment import rules (administration \> rules \> Rules for import and
link equipments)

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

## The different actions

Apart from [common actions](../../modules/overview/actions.md), some actions are specific to displays:

- connect a display to a monitor

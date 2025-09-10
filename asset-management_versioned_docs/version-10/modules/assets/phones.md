---
id: phones
title: Phones
---

# Phones

Phones can be registered manually or uploaded using the Android agent
(no agent is currently compatible with iPadOS/iOS devices).

:::tip

Note that if you modify a field manually, it will be considered
locked. This will prevent it from being modified the next time the
automatic inventory is uploaded.

For more information, see
[lock](../../modules/assets/tabs/locks)

:::

![module assets - global view Phones](../../assets/modules/assets/images/phones_global_view.png)

In a phone form, the following information is available:

- Name
- [Location](../../tabs/common_fields/location.md)
- [Technician in charge](../../tabs/common_fields/technician_in_charge.md)
- [Group in charge](../../tabs/common_fields/group_in_charge.md)
- [Alternate usernmame number](../../tabs/common_fields/alternate_username.md)
- [Alternate usernmame](../../tabs/common_fields/alternate_user.md)
- [User](../../tabs/common_fields/user.md)
- [Group](../../tabs/common_fields/group.md)
- [Comments](../../tabs/common_fields/comments.md)
- [Status](../../tabs/common_fields/status.md)
- Phone type
- [Manufacturer](../../tabs/common_fields/manufacturer.md)
- [Model](../../tabs/common_fields/model.md)
- [Serial number](../../tabs/common_fields/serial_number.md)
- [Inventory number](../../tabs/common_fields/inventory_number.md)
- [Management type](../../tabs/common_fields/management_type.md)
- [UUID](../../tabs/common_fields/uuid.md)
- Brand
- Number of lines
- [Update source](../../tabs/common_fields/update_source.md)
- [Ports](../../tabs/common_fields/ports.md)

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

## Components

This tab lists the phone's
[components](../../tabs/components.md) :

- BIOS
- Processor
- Memory
- Hard Drive
- Network card
- Drive
- Battery
- Graphics card
- Soundcard
- Controller

Each item has its
[own information](../../tabs/components.md)
(name, model, brand, memory capacity, number of cores/threads, etc.).

## Lines

You can add telephone lines created in [Lines](../management/lines.html)

## Volumes

Summarises all of the [volumes](../../tabs/volume.md) present (hard disk, DVD) as well as the partitions present
on the workstation (virtual disks such as Google Cloud may appear if
they are installed as a network drive).

- Name
- Automatic inventory (Yes /No)
- partition
- Mount point
- File system
- Global size
- Free size
- Free percentage
- Encryption (if the disk is encrypted, a padlock will be displayed)

## Connections

It is possible to create a
[connections](../../tabs/connections.md)
with a telephone using the following element:

- [Computer](computers.html)

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

## Sockets

[Sockets](../../tabs/sockets.md) are the
list of physical sockets present on the hardware. These sockets can be
Ethernet, USB, HDMI, etc. This information cannot be returned by the
automatic inventory, so you have to add it manually.

It enables hardware to be linked by cables. Socket is also linked to the
[cables](../../modules/assets/cables) object

## Remote management

[Remote management](../../tabs/remote-management.md) is used to reference the remote access software installed on
the phone, such as Teamviewer, Anydesk, etc. It is possible to add
software manually if required, but the information can be fed back via
the automatic inventory.

## Management

[Management](../../modules/tabs/management.md) of financial and administrative information, this
information is visible in the 'Management' tab on the phone's form.

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

## Antiviruses

[Antiviruses](../../modules/assets/tabs/antivirus.md) lists all
the antivirus programs detected on the phone.

## Knowledge Base

Lists all the articles in the
[knowledge base](../../modules/tabs/knowledgebase.md)
relating to the material.

## Tickets

View all [tickets](../../modules/tabs/tickets.md)
linked to the phone

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
linked to the phone you have selected.

## Links

[Links](../../modules/configuration/external_links.md)
offer several possibilities. Send the i-Vertix ITAM object file to another URL of
your choice, or generate an RDP file, for example.

## Notes

[Note](../../modules/tabs/notes.md) lets you add
enriched text and attach a document.

## Reservations

The [reservation](../../modules/tools/reservations.md) tab lets you reserve equipment, view the reservation
schedule, or cancel the possibility of reserving this equipment. By
default, equipment cannot be reserved; you must first authorize this
action manually.

## Domains

You can attach [Domains](../../modules/management/domains.md) to your phone. Domains are also linked to other objects such
as records, problems, etc.

## Appliances

[Appliances](../../modules/management/appliance.md) includes all business applications managed within i-Vertix ITAM. They
can be linked to another i-Vertix ITAM object (computer, application, etc.) as
well as to another appliance.

## Historical

[Historical](../../modules/tabs/historical.md) lists
all the actions carried out on the object in question

## All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

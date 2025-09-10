---
id: racks
title: Racks
---

# Racks

A rack is a piece of equipment such as a patch bay or computer cabinet
used to organize, host and physically connect different network
equipments and servers in a datacenter or technical room.

A rack is a dedicated object in i-Vertix ITAM that virtually represents the
physical structure of a rack or cabinet. It is designed to :

- **Organize equipment**: A rack is used to visualize and manage the
  physical equipment (servers, switches, routers, UPS, etc.)
- installed in it.
- **Facilitate physical management**: It enables you to track where
  equipment is installed in a physical space (technical room,
  datacenter, etc.).
- **Optimize space**: Racks help ensure that space is used efficiently,
  and that there's still room for new equipment.

![module assets - global view racks](../../assets/modules/assets/images/rack.png)

When you add a rack (by **+ Add** at the top of the screen), you can add
certain information:

- Name
- [Data center position](../../tabs/common_fields/data_center_position.md)
- [Location](../../tabs/common_fields/location.md)
- [Technician in charge](../../tabs/common_fields/technician_in_charge.md)
- [Group in charge](../../tabs/common_fields/group_in_charge.md)
- [Serial number](../../tabs/common_fields/serial_number.md)
- [User](../../tabs/common_fields/user.md)
- [Comments](../../tabs/common_fields/comments.md)
- Position in room
- Number of units
- Height
- Max. Power (in watts)
- Max. weight
- [Status](../../tabs/common_fields/status.md)
- [Rack type](../../tabs/common_fields/asset_type.md)
- [Manufacturer](../../tabs/common_fields/manufacturer.md)
- [Model](../../tabs/common_fields/model.md)
- [Inventory number](../../tabs/common_fields/inventory_number.md)
- [Group](../../tabs/common_fields/group.md)
- [Server room](/modules/management/data-centers.html#server-room)
- Door orientation in room (North, East, South, West)
- Width
- Depth
- Measured power (in watts)
- Background color

## Items

The [Item](../../modules/assets/tabs/rack_items.md) tab shows the
position of each element in the rack. You can modify, add or remove an
item from your park to your rack.

## Impact Analysis

[Impact analysis](../../tabs/impact_analysis.md) enables an infrastructure diagram to be drawn up, showing
the dependencies and impacts in the event of equipment loss. This can be
saved and exported

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

## Reservations

The [reservation](../../modules/tools/reservations.md) tab lets you reserve equipment, view the reservation
schedule, or cancel the possibility of reserving this equipment. By
default, equipment cannot be reserved; you must first authorize this
action manually.

## Historical

[Historical](../../modules/tabs/historical.md) lists
all the actions carried out on the object in question

## All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

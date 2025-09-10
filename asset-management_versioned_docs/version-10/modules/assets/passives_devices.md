---
id: passives_devices
title: Passives Devices
---

# Passive devices

Passive devices list equipment that do not actively process data but
still play an essential role in the IT infrastructure. They are often
used for connectivity or signal transmission (like a patch panel, a
non-manageable switch, etc.)

:::info

Passive devices cannot be added to the automatic inventory.

:::

:::info

It is possible to use
[templates with passive devices](../../modules/overview/templates.md).

:::

![Passives devices global view](../../assets/modules/assets/images/passives_devices.png)

In a passive device form, the following information is available:

- Name
- [Location](../../tabs/common_fields/location.md)
- [Technician in charge](../../tabs/common_fields/technician_in_charge.md)
- [Model](../../tabs/common_fields/model.md)
- [Inventory number](../../tabs/common_fields/inventory_number.md)
- [Comments](../../tabs/common_fields/comments.md)
- [Status](../../tabs/common_fields/status.md)
- [Passive device type](../../tabs/common_fields/asset_type.md)
- [Manufacturer](../../tabs/common_fields/manufacturer.md)
- [Serial number](../../tabs/common_fields/serial_number.md)
- [User](../../tabs/common_fields/user.md)

![Passive devices details view](../../assets/modules/assets/images/passives_devices_details.png)

## Sockets

[Sockets](../../tabs/sockets.md) are the
list of physical sockets present on the hardware. These sockets can be
Ethernet, USB, HDMI, etc.

It enables hardware to be linked by cables. Socket is also linked to the
[cables](../../modules/assets/cables) object

## Management

[Management](../../modules/tabs/management.md) of financial and administrative information, this
information is visible in the 'Management' tab on the items's form.

## Contracts

i-Vertix ITAM supports [contracts](../../modules/management/contract.md) management, in order to manage contract types such as loan,
maintenance, support...

Contracts management allows to:

- make an inventory of all contracts related to the organization assets
- integrate contracts in i-Vertix ITAM financial management
- anticipate and follow contract renewal.

## Documents

The [document](../../modules/management/documents.md)
tab lets you link different types of files to the current item (PDF,
txt, png, etc.) You can attach a document already uploaded to i-Vertix ITAM or
add a new one directly from this tab.

## Tickets

View all [tickets](../../modules/tabs/tickets.md)
linked to the current item.

## Problems

This tab refers to all hardware-related
[problems](../../modules/assistance/problems.md).
Problems can also be linked to tickets, projects, etc. This allows you
to have a complete scenario when necessary.

## Changes

[Changes](../../modules/assistance/changes.md) lists
all changes related to the current item. From this tab, you can't link
a change directly, you can do it from **Assistance** \> **Changes** \>
**Items**.

You can create a new change from this page, which will be linked to the
item you have selected.

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

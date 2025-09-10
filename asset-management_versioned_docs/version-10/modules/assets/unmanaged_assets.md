---
id: unmanaged_assets
title: Unmanaged Assets
---

# Unmanaged assets

Unmanaged equipment is equipment that is not directly administered by a
i-Vertix ITAM agent or a protocol such as SNMP, WMI, etc. Unlike managed
equipment, it does not automatically report information and must be
manually updated in the inventory. These devices have been detected
during a network discovery and can be converted into another type of
object, either manually or via SNMP feedback.

![module assets - unmanaged assets](../../assets/modules/assets/images/unmanaged_assets_global_view.png)

:::tip

Note that if you modify a field manually, it will be considered
locked. This will prevent it from being modified the next time the
automatic inventory is uploaded.

For more information, see
[lock](../../modules/assets/tabs/locks)

:::

In a unmanaged asset form, the following information is available:

![module assets - unmanaged assets details](../../assets/modules/assets/images/unmanaged_assets_details_view.png)

- Name
- [Location](../../tabs/common_fields/location.md)
- [Manufacturer](../../tabs/common_fields/manufacturer.md)
- [Serial number](../../tabs/common_fields/serial_number.md)
- [Inventory number](../../tabs/common_fields/inventory_number.md)
- [SNMP Credentials](../../tabs/common_fields/SNMP_credentials.md)
- [Network](../../tabs/common_fields/network.md)
- [Update source](../../tabs/common_fields/update_source.md)
- Approved device: Yes / No
- [Status](../../tabs/common_fields/status.md)
- [Technician in charge](../../tabs/common_fields/technician_in_charge.md)
- [Alternate usernmame number](../../tabs/common_fields/alternate_username.md)
- [Alternate usernmame](../../tabs/common_fields/alternate_user.md)
- [Sysdescr](../../tabs/common_fields/sysdescr.md)
- [User](../../tabs/common_fields/user.md)
- [Comments](../../tabs/common_fields/comments.md)
- IP
- Network hub: Yes/No

## Network Ports

This tab allows to manage the
[network ports](../../tabs/network_ports.md)
attached to the item. The information that can be viewed is:

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

## Domains

You can attach [Domains](../../modules/management/domains.md) to the current item. Domains are also linked to other
objects such as records, problems, etc.

## Locks

[Locks](../../modules/assets/tabs/locks.md) are
used to prevent a field from being modified when the inventory is
uploaded. You can lock/unlock the fields you wish in a i-Vertix ITAM object.

## Import information

Import information is information that is uploaded and governed by
equipment import rules (Administration \> Rules \> Rules for import and
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

## Particularity

### Massive actions

This item has a specific massive action which allows it to be converted
into another type of object (computer, printer, etc.).

You can convert it manually via this massive action, or report it via
SNMP, WMI, etc.

![module assets - Convert unmanged asset](../../assets/modules/assets/images/unmanaged_assets_massive_action.png)

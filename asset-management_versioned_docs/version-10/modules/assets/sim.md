---
id: sim
title: Sim
---

# SIM

A `SIM (Subscriber Identity Module)`
represents a SIM card used in mobile equipment such as telephones,
tablets, 4G/5G modems, etc. You can manage these SIM cards as specific
objects to track their use and allocation.

:::tip

Note that if you modify a field manually, it will be considered
locked. This will prevent it from being modified the next time the
automatic inventory is uploaded.

For more information, see
[lock](../../modules/assets/tabs/locks)

:::

In a display form, the following information is available:

![Detail view SIM](../../assets/modules/assets/images/sim_detail_view.png)

- Code PIN
- Code PIN2
- Code PUK
- Code PUK2
- [Line](../../modules/management/lines.md)
- Mobile Subscriber Identification Number (MSIN is last 8 or 10 digits
  of IMSI)
- [Serial number](../../tabs/common_fields/serial_number.md)
- [Inventory number](../../tabs/common_fields/inventory_number.md)
- [Location](../../tabs/common_fields/location.md)
- [Status](../../tabs/common_fields/status.md)
- [User](../../tabs/common_fields/user.md)
- [Group](../../tabs/common_fields/group.md)
- [Comments](../../tabs/common_fields/comments.md)

## Management

[Management](../../modules/tabs/management.md) of financial and administrative information, this
information is visible in the 'Management' tab on the current item's
form.

## Documents

The [document](../../modules/management/documents.md)
tab lets you link different types of files to this item (PDF, txt, png,
etc.) You can attach a document already uploaded to i-Vertix ITAM or add a new
one directly from this tab.

## Locks

[Locks](../../modules/assets/tabs/locks.md) are
used to prevent a field from being modified when the inventory is
uploaded. You can lock/unlock the fields you wish in a i-Vertix ITAM object.

## Contracts

i-Vertix ITAM supports [contracts](../../modules/management/contract.md) management, in order to manage contract types such as loan,
maintenance, support...

Contracts management allows to:

- make an inventory of all contracts related to the organization assets
- integrate contracts in i-Vertix ITAM financial management
- anticipate and follow contract renewal.

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

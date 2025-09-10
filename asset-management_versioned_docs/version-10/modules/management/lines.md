---
id: lines
title: Lines
---

# Phone lines

Phone lines management in i-Vertix ITAM allows to:

- Create an inventory of all organization's phone lines;
- Follow information on each phone line;
- Include phone lines in i-Vertix ITAM financial management.

![A phone line in i-Vertix ITAM](../../assets/modules/management/images/lines.png)

## Basic fields

- Name
- [Status](../../tabs/common_fields/status.md)
- [Location](../../tabs/common_fields/location.md)
- [User](../../tabs/common_fields/user.md)
- [Group](../../tabs/common_fields/group.md)
- [Comments](../../tabs/common_fields/comments.md)
- Line type :
  - You can add an existing line type or add a new one by clicking on +.

## Specific fields

- Caller number : telephone number attached to the line
- Caller name : user attached to the line
- Line operator :
  - You can add an existing operator or add a new one by clicking on +.

## The different tabs

### Items

List of all other linked i-Vertix ITAM [Items](../../tabs/item.md). You can manually add an item by selecting it from the
drop-down list.

### Management

[Management](../../modules/tabs/management.md) of
financial and administrative information, this information is visible in
the 'Management' tab on the object form.

### Contracts

i-Vertix ITAM supports
[contracts management](../../modules/management/contract.md), in order to manage contract types such as loan,
maintenance, support...

Contracts management allows to:

- make an inventory of all contracts related to the organization assets
- integrate contracts in i-Vertix ITAM financial management
- anticipate and follow contract renewal.

### Documents

The [document](../../modules/management/documents.md) tab lets you link different types of file to a material
(PDF, txt, png, etc.) You can attach a document already uploaded to i-Vertix ITAM
or add a new one directly from this tab.

### Note

The [Notes](../../modules/tabs/notes.md) tab
provides a free text field for storing additional information. Notes are
displayed in the order of their creation. You can also add a document

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

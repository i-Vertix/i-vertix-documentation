---
id: appliance
title: Appliance
---

# Appliances

The Appliances in i-Vertix ITAM refer to the software and applications managed
within the i-Vertix ITAM tool. This includes all software solutions installed on
users' machines, servers and other devices within the organisation.
Applications can include office applications, business software,
operating systems, utilities, etc.

![General view appliance](../../assets/modules/management/images/appliance.png)

## The basics fields

- Name
- [Status](../../tabs/common_fields/status.md)
- [Location](../../tabs/common_fields/location.md)
- [Technician in charge](../../tabs/common_fields/technician_in_charge.md)
- [Group in charge](../../tabs/common_fields/group_in_charge.md)
- [Manufacturer](../../tabs/common_fields/manufacturer.md)
- [Alternate username number](../../tabs/common_fields/alternate_username.md)
- [Alternate username](../../tabs/common_fields/alternate_user.md)
- [Serial number](../../tabs/common_fields/serial_number.md)
- [Inventory number](../../tabs/common_fields/inventory_number.md)
- [User](../../tabs/common_fields/user.md)
- [Group](../../tabs/common_fields/group.md)
- [Comments](../../tabs/common_fields/comments.md)

## The specifics fields

### Appliance type

The appliance type is used to define the appliance context (VOIP, EDM,
etc.). You can select the type of application from the drop-down list,
or add a new one directly by clicking on the **+**.

![Add a new type of appliance](../../assets/modules/management/images/appliance-add-type.png)

### Appliance environment

The application environment designates whether the application is in
production, acceptance, pre-production, etc. This field can of course be
adapted to suit your needs.

### Pictures

You can add a picture for your appliance.

## The differents tab

### Impact Analysis

[Impact analysis](../../tabs/impact_analysis.md)
enables an infrastructure diagram to be drawn up, showing the
dependencies and impacts in the event of equipment loss. This can be
saved and exported

### Items

List of all other linked i-Vertix ITAM [Items](../../tabs/item.md). You can manually add an item by selecting it from the
drop-down list. An appliance can also be linked to another appliance

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

### Management

[Management](../../modules/tabs/management.md) of
financial and administrative information, this information is visible in
the 'Management' tab on the object form.

### Certificates

Link a
[certificate](../../modules/management/certificates.md) to your registration. You can manage certificates in
**Management** \> **Certificates**

### Domains

[Domains](../../modules/management/domains.md)
represents an Internet domain, with its name, expiration date... This
object can itself be linked to other objects in i-Vertix ITAM support (tickets,
problems, changes).

### Knowledge Base

Lists all the articles in the
[knowledge base](../../modules/tabs/knowledgebase.md)
relating to the appliance.

### Links

[Links](../../modules/configuration/external_links.md)
offer several possibilities. Send the i-Vertix ITAM object file to another URL of
your choice, or generate an RDP file, for example.

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

---
id: softwares
title: Softwares
---

# Software

i-Vertix ITAM allows management of software and their versions as well as
licenses, associated or not to software versions.

A software is by default associated with an entity.

Financial management is done at the level of licenses; the financial
management at software level is only a model for the licenses associated
with this software.

Software can be imported automatically using a third-party inventory
tool; in this case a dictionary can be used to filter or clean the
import data (see \[Configure data
dictionaries\](07_Module_Administration/06_Dictionnaires.rst "The
dictionaries are managed from menu entry Administration \>
Dictionaries")).

Some fields are specific in the software form:

- **Update** is an information, with no processing associated and which
  tells whether the software is an update of another software
- **Category** allows to group software in the list of software of an
  asset
- **Can be associated with a ticket** defines whether the software can
  be seen in the drop-down list "Hardware" of a ticket

It is recommended to first create the software without a version number
in the name, then to create the versions and last to create the
licenses.

:::info

In multi-entity mode, the list of software can rapidly become long
because of double entries (one software per entity). A better approach
can consist in grouping identical software in the same entity (see tab
*Grouping* below), then to make recursive the elements that can be
made recursive.

:::

It is possible to use
[templates with software](/asset-management/modules/overview/templates).

## The different tabs

### Versions 

A version of a software is the element that can be installed on a asset;
see also *Installations* tab.

The main view lists the number of installations of the version.

Specific fields:

- **Name**: the version number
- **Status**: in ITIL recommendations, it allows to follow the DSL
  (library storing authorized versions)
- **Operating system**: the operating system on which this software
  version runs
- **Installations**: the number of installations of the version
- **Comment**: some comments

### Licenses

### Installations

The installation of a software on a computer is visualized through a
version and can be consulted on a software form (list of computers
having at least one version installed), on a version form (computers
having this version installed) and finally on a computer form (list of
versions of installed software, sorted by category).
:::note

- Column [license] is filled only when the license is
  affected to the concerned computer
- The initial display of different categories depend upon user
  preferences (see \[manage   preferences\](01-premiers-pas/03_Utiliser_i-Vertix ITAM/04_Gérer_ses_préférences.rst").
:::

Two options are available on the list of installations of software on a
computer. Above the list, **Install** allows to install manually a
version of a software on the computer, by selecting first the software
and its version; if a license is associated with this software, the use
version of the license is automatically selected.

To **Uninstall** a version of a software, mass actions must be used:
first select the versions to be uninstalled, then select **Suppress
definitively**. If a license is affected to the computer, it remains
affected but its use version is erased.

Following the list of installed versions, the list of affected but non
installed licenses is displayed. It is possible to add a new license to
the computer. Mass actions allow, via the action **Install**, to install
a use version of selected licenses.

### Management

Management of financial and administrative information, this information
is visible in the 'Management' tab on the computer's form.

![Management screen](../../assets/modules/tabs/images/management.png)

By default this management is disabled. It is possible to activate the
financial information on any type of object in the inventory by using
the link in the *Management* tab of the material detail.

![Enable management](../../assets/modules/tabs/images/management_enable.png)

:::info

It is possible to activate the administrative and financial
information from the massive actions on a set of elements (computer,
monitor, ...)

:::

:::info

It is possible to activate the administrative and financial
information as soon as an element is created. See "Enable default
administrative and financial information" option in Setup \> General
\> Asset tab.

:::

Financial information consists of the following items:

#### Lifecycle

- Order date
- Date of purchase
- Delivery date
- Date of implementation
- Date of last physical inventory
- Date of reform

#### Financial and administrative information

- Supplier: Third party who sold the equipment. See
  [Managing suppliers](/asset-management/modules/management/suppliers). Suppliers are managed from the menu **Management \>
  Suppliers**.
- Order number : number of the order of the equipment.
- Asset number.
- Invoice number: equipment invoice number.
- Delivery note: delivery note for the equipment.
- Value: cost of the equipment.
- Warranty extension value: cost of the warranty extension, but
  preferably use contracts.
- Account net value: this is the automatic calculation of the gross
  value of a piece of equipment minus the amount of depreciation.
- Type of depreciation: choice of the type of depreciation between
  linear and declining balance.
- Depreciation period: depreciation period expressed in years.
- Depreciation coefficient: coefficient applied to a straight-line
  depreciation type in order to obtain the values of the declining
  balance type. It is therefore only used if the type of depreciation is
  declining balance.
- TCO (value+amount of interventions): the total cost of ownership which
  includes all the constituent elements of an invoiced product.
- Budget: the budget on which this equipment was purchased See
  [Managing the budget](/asset-management/modules/management/budgets).
- Order date: date on which the material was ordered.
- Purchase date: date on which the equipment was purchased.
- Delivery date: date on which the equipment was delivered.
- Startup date: date on which the equipment was put into service.
- Date of last physical inventory: date of the last physical inventory
  of the equipment.
- Comments.
- Monthly TCO: TCO divided by the number of months between today's date
  and the date of purchase of the equipment.

#### Warranty information

- Warranty start date: date on which the warranty of the equipment
  starts

- Warranty information: text qualifying the warranty

- Warranty period: duration of the warranty expressed in months

  :   If a warranty start date and a warranty period are set, the
      information "Expires on" will appear with a date in red if it is
      earlier than the current date

All the dates defined can be managed automatically according to changes
in the status of the equipment. Some dates can also be copied from
another date. All this configuration is done by
\[entity\](administration_entity_delegation.dita).

#### Tips

i-Vertix ITAM allows you to configure a notification on the expiry of the
hardware warranty. This is configurable by entity in notification
management to define the models and recipients used and in
[the administration of entities](/asset-management/modules/administration/entities) to enable or disable this feature, define the default values
and anticipate the sending of the notification if necessary.

i-Vertix ITAM can perform a simple net book value calculation based on
straight-line or declining balance depreciation. To do so, a certain
amount of information (value, date, etc.) must be entered. The user must
also enter the date of the financial year the general configuration.

The display of financial information for each type of equipment depends
on the profile of the user logged in.

### Associated Contracts

The *Contracts* tab is used to show or add linked contracts.

![Contract display screen](../../assets/modules/tabs/images/contract.png)

For each associated contract, the name, number, contract type, supplier,
start date and initial duration of the contract are listed. In the last
field, the end date of the contract is also shown with a red display if
the date is earlier than the current date.

Refer to
[contract management](/asset-management/modules/management/contract) for more information.

### Documents

Additional information is stored in the form of external documents which
are files uploaded into i-Vertix ITAM. In the *Documents* tab, documents can be
associated and unlinked with the selected item. The
[management of the documents themselves](/asset-management/modules/management/documents) is dealt with in another chapter.

It is also possible to quickly create a document via this tab by
specifying the desired file and optionally the field in which the new
document is to be placed. The name of the created document will be based
on the name of the added file.

![Document creation screen](../../assets/modules/tabs/images/documents.png)

:::info

When you delete a document from this tab via mass actions, you only
remove the link between the object and the document; the document
itself is still present.

:::

### Tickets

The *Tickets* tab is used to create a ticket associated with the current
object. It also lists the tickets already linked to the object.

![Image of the ticket list](../../assets/modules/tabs/images/tickets.png)

:::info

A second table lists the tickets attached to the linked elements

:::

:::info

Any deletion or addition of a ticket is recorded in the history.

:::

### Problems

The *Problems* tab is used to create a problem associated with the
current object. It also lists the changes already linked to the object.

This summary table includes for each object:

- Status
- Date (opening or expiry date, resolution or closing date depending on
  the status of the problem)
- Priority
- Requestor(s) and assigned technician(s)
- Associated elements
- Category
- Name
- Column indicating the number of scheduled tasks

![Creation and list of associated problems](../../assets/modules/tabs/images/problems.png)

:::info

A second table lists the problems attached to the related elements

:::

:::info

Any deletion or addition of a problem is recorded in the history.

:::

### Associated External Links

The *External links* tab is used to show associated external links.

For some items, external links are managed from the menu **Setup \>
External links**.

These links can use object fields such as IP, name, etc. See
[Configure protocol external links](/asset-management/modules/configuration/external_links).

Examples:

- A web link: [http://192.168.0.1](http://192.168.0.1) (IP retrieved from the network port
  of the hardware) ;
- A RDP link for remote access: glpi://MSTSC.EXE,pc001 (name "pc001"
  retrieved from the hardware).

### Notes

The *Notes* tab provides a free text field for storing additional
information. Notes are displayed in the order of their creation.

![View and enter a note](../../assets/modules/tabs/images/notes.png)


### History

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

### Grouping

This section describes how to group software having same names in
sub-entities, allowing to group software of child entities into mother
entity.

:::info

This is only available for multi-entities platforms.

:::

How to realize a grouping:

1.  If the software does not exist in mother entity, create in this
    mother entity a software whose name is strictly identical to the
    name of software in child entities
2.  Open the form of the software of the mother entity
3.  Activate recursivity (sub-entities to Yes at top right); this will
    make a new tab [Grouping] appear after tab
    [History]
4.  Open this tab; a list displays software having same names in child
    entities
5.  Select appropriate lines and validate grouping

:::warning

This operation cannot be undone

:::

This grouping have the following effects:

- Licenses are attached to the software in mother entity, but stay in
  origin sub-entities
- Versions are merged, no more doubles in mother entity
- Old software are moved to the trash

:::info

When using a third-party inventory tool, some extra steps are
mandatory:

- Empty trash after grouping, otherwise synchronization will restore
the old software in case of new version
- Associate the same vendor to the new software; as the
synchronization checks vendor name, a new software would then be
created

:::

### Debugging information

If you have [Debug] mode enabled in your preferences, a
*Debug* tab will appear before the *All* tab. This tab offers
information to help you resolve an issue.

For example, for a computer, you have one or more tables depending on
the affected object (financial information, reservations...) listing
the notifications that will be triggered on this computer with:

- Triggering event
- Recipient(s)
- Notification model used
- Recipient(s) email address

![Debugging page](../../assets/modules/tabs/images/debug.png)

### All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

## The different actions

Apart from [common actions](/asset-management/modules/overview/actions), some actions are specific to software:

- Add a version to a software
- **\[Manage   licenses\](03_Module_Parc/04_Logiciels/Onglet_Licences.rst)** From
  menu **\*Assets \> Softwares**\* click on license name in tab
  *Licenses*.

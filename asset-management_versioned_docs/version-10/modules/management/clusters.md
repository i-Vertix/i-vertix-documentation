---
id: clusters
title: Clusters
---

# Clusters

A i-Vertix ITAM cluster is a grouping of several assets, which can be computers
or network equipments.

:::info

i-Vertix ITAM clusters are taken into account when performing an impact
analysis.

:::


![A i-Vertix ITAM cluster](../../assets/modules/management/images/clusters.png)

## Description of specific fields

- **UUID**: Unique identifier of the cluster
- **Version**: In the case of a software cluster, the version number can
  be entered
- **Update Source**: How the cluster's data were updated

## The different tabs

### Elements

This tab lists the cluster's elements and allow to add new assets to
the cluster.

![List of cluster's elements](../../assets/modules/management/images/elements-clusters.png)

### Network ports

This tab list cluster's network interfaces and allows to create new
ones.

Possible interfaces are:

- Ethernet port
- WiFi port
- FiberChannel port
- Port aggregate
- Port alias
- Dial up line connection
- Local loop-back

![List of cluster's network interfaces](../../assets/modules/management/images/networks-clusters.png)

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

### Changes

The *Changes* tab is used to create a change associated with the current
object. It also lists the changes already linked to the object.

This summary table includes the following fields for each object:

- Status
- Date (opening or expiry date, resolution or closing date depending on
  the status of the change)
- Priority
- Requestor(s) and assigned technician(s)
- Associated elements
- Category
- Name
- Number of scheduled tasks

![Creation and list of associated changes](../../assets/modules/tabs/images/changes.png)

:::info

A second table lists the changes attached to the related elements

:::

:::info

Any deletion or addition of a change is recorded in the history.

:::

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

### All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

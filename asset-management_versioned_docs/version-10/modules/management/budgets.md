---
id: budgets
title: Budgets
---

# Budgets

A budget in i-Vertix ITAM is defined by an amount and a time period. Other i-Vertix ITAM
items can be attached to this budget and will then, by providing their
value, modify the budget available amount.

Creating a budget in i-Vertix ITAM enables the administrative and financial
management functionality for all other i-Vertix ITAM items.

It is possible to follow the evolution of a budget by tracing the value
of each attached item.

:::info

Attaching a i-Vertix ITAM item to a budget is done via tab
[Management] of the item!

:::

![Main fields of a budget](images/budgets.png)

:::info

When displaying a budget from a sub-entity, the budget remaining total
amount is not visible.

The budget remaining total amount can be negative if the sum of the
values of attached items is greater than the budget amount.

:::

:::info

It is possible to use
`templates to generate this object \<../overview/templates>`.

:::

## The different tabs

### Main tab

This tab provides a summary table giving the expended amount of the
budget, sorted by item type, as well as total remaining amount.

![Budget summary table](images/main-budgets.png)

### Items

This tab displays i-Vertix ITAM items attached to this budget as well as their
value.

![Budget attached elements](images/elements-budgets.png)

:::info

Attaching a i-Vertix ITAM item to a budget is done via tab
[Management] of the item!

:::

### Documents

Additional information is stored in the form of external documents which
are files uploaded into i-Vertix ITAM. In the *Documents* tab, documents can be
associated and unlinked with the selected item. The
[management of the documents themselves](/asset-management/modules/management/documents) is dealt with in another chapter.

It is also possible to quickly create a document via this tab by
specifying the desired file and optionally the field in which the new
document is to be placed. The name of the created document will be based
on the name of the added file.

![Document creation screen](/modules/tabs/images/documents.png)

:::info

When you delete a document from this tab via mass actions, you only
remove the link between the object and the document; the document
itself is still present.

:::

### Knowledge base

The *Knowledge base* tab is used to show or add linked knowledge base
articles.

![Viewing or adding a knowledge base entry](/modules/tabs/images/knowledgebase.png)

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

![View and enter a note](/modules/tabs/images/notes.png)

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

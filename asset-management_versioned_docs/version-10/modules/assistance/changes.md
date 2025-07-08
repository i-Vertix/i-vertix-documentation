---
id: changes
title: Changes
---

# Manage changes

A change is a modification of the information system's infrastructure.

A change can be created either from a ticket form or a problem form, in
tab **Changes**, or from menu **Assistance \> Changes**.

The form to create a change is similar to the ticket creation form and
shares with it many terms: *requester*, *watcher*, *assigned to*,
*status*, *urgency*, *impact*, *priority*, *category*. For more
information see
[Manage tickets](/asset-management/modules/assistance/tickets/ticketmanagement). The validation process is also the same as tickets in order
to allow preliminary validation of the change (tab *Validations*).

Once the change is created, it is possible to attach tickets but also
impacted items (tab *Items*). An analysis phase (tab *Analysis*)
consists in describing impacts and controls list in order to implement
this change through a deployment plan, a backup plan and a checklist
(tab *Plans*).

Same as tickets, task, costs and solution allow to follow and solve the
change. For complex changes management, a change can be linked with one
or several projects allowing a mode detailed management
([Manage projects](/asset-management/modules/tools/projects)).

Changes use their own notifications (see
[configuration of email follow-ups](email_notifications)).

## The different tabs

### Analysis

This tab contains impacts and check-lists in order to implement the
change.

### Plans

This plan contains deployment plans, backup plans and check-lists.

### Projects

This tab allows to attach a project to the change and displays already
attached projects.

The summary table contains for each project status, opening or closing
dates, priority and supervisors.

### Solutions

This tab allows to describe the resolution of the change. See
[Solutions](/asset-management/Les_différents_onglets/Onglet_Solution)

### Statistics

Statistics similar to tickets are available for changes. See
[Statistics](/asset-management/Les_différents_onglets/Onglet_Statistiques)

### Approvals

See
[Approvals](/asset-management/Les_différents_onglets/Onglet_Validations)

### Tasks

A task is an action linked with a change, usually a technical
intervention. See
[Tasks](/asset-management/Les_différents_onglets/Onglet_Tâches)

### Costs

This tab defines the costs applicable to this change. See
[Costs](/asset-management/Les_différents_onglets/Onglet_Coûts)

### Elements

This tab allows to attach an item to the change by choosing the type and
the selected item. See
[Items](/asset-management/Les_différents_onglets/Onglet_Eléments)

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

### All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

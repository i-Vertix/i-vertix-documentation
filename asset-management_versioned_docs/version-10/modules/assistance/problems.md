---
id: problems
title: Problems
---

# Manage problems

A problem is the cause of potential incidents and, once identified, can
be managed in i-Vertix ITAM.

Creating a problem object can be done either from the ticket form, in
tab *Problem*, or directly from menu *Assistance \> Problems*.

The problem creation form is very similar to the ticket creation form
and shares with it many concepts: *Requester*,
*Watcher*, *Assigned to*, *Status*,
*Urgency*, *Impact*, *Priority*,
*Category*. For more information, see
[Manage tickets](../../modules/assistance/tickets/ticketmanagement.md).


Problems use their own notifications, see
[configuration of email follow-ups](../../modules/configuration/notifications/email_notifications).

Statistics similar to tickets are available for problems, see
[Display statistics](../../modules/assistance/statistics.md).

## The different tabs

### Analysis

This tab contains problem analysis.

It consists of 3 inserts:

- Impacts
- Causes
- Symptoms

![View analysis](../../assets/modules/assistance/tabs/images/analysis-view.png)

### Statistics

Statistics similar to tickets are available for problems.

![statistics tab for problems](../../assets/modules/assistance/images/problems-statistics.png)

### Tickets

List all [tickets](../../modules/assistance/tickets.md) are linked to
the problem. You can add a new ticket or link an existing ticket

![Ticket linked on problems](../../assets/modules/assistance/tabs/images/problem-view-ticket.png)

![add tickets exists](../../assets/modules/assistance/tabs/images/problem-add-ticket.png)

![View ticket in problem body](../../assets/modules/assistance/tabs/images/problem-view-ticket-body.png)

### Changes

This tab allows to display changes associated with the problem and add
new changes. See [changes](../../modules/assistance/changes.md)

![changes tab for problems](../../assets/modules/assistance/images/problems-changes.png)

### Costs

The cost represents the financial impact of the problem encountered. It
can be human, material or fixed.

:::warning

A cost cannot be added once the problem has been closed or resolved.

:::

![view cost](../../assets/modules/assistance/tabs/images/problem-cost.png)

![add cost for problem](../../assets/modules/assistance/tabs/images/problem-add-cost.png)

### Projects

You can attach or add one or more
[projects](../../modules/tools/projects.md) to your
problem.

![add project for problem](../../assets/modules/assistance/tabs/images/problem-project.png)

### Tasks

A task is an action linked with a problem, usually a technical
intervention. See
Tasks

### Items

This tab allows to attach an item to the problem by choosing the type
and the selected item. See [Items](../../modules/tabs/items.md)

### Impact analisys

[Impact analysis](../../tabs/impact_analysis.md) enables you to visualise the impact of failures on an entire
infrastructure

### Notes

The *Notes* tab provides a free text field for storing additional
information. Notes are displayed in the order of their creation. You can
also add a document

![View and enter a note](../../assets/modules/tabs/images/notes.png)

#### Add a note

- To add a note, click on **+Add**
- You can add text and format it to suit your needs
- You can add a document to this note

![Edit a note](../../assets/modules/tabs/images/notes-add.png)

#### Delete a note

- To delete a note, you need to click on **delete**
- You can delete only the attachment by clicking on delete (the option
  appears when you move your mouse over the attachment)

![delete a note](../../assets/modules/tabs/images/notes-delete.png)

:::tip

When you delete an attachment, it is not completely deleted, you can
find it in **Management** \> **Documents**

:::

### Knowledge Base

You can link an article from the
[knowledge base](../../modules/tabs/knowledgebase.md).
It is possible to add a new article by clicking on **i**

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

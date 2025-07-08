---
id: assistance
title: Assistance
---

# Assistance

## Ticket categories

The list of ticket categories is tree-like: each element can have
sub-elements. It can be delegated by entity.

In the form of a ticket category, you can find some information about
this category including but not limited to:

- Responsible and technical group for the automatic assignment of
  tickets
- Default category of the knowledgebase when you want to add a solution
  of a ticket
- Visibility of the category depending on the interface
  (simplified/standard) or object
- Ticket template to use for this category
- Parent category

If a template is chosen, it will be assigned to the choice of the
category and will therefore override the one that would have been
defined in the entity or via a business rule.

A link with the categories of the knowledge base is possible. If a
category is chosen, clicking on the ticket category help in a ticket
leads directly to all the articles in the knowledge base for this
category.

### Ticket categories

Displays a list of child ticket categories and allows adding new ones.

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

## Task categories

The list of task categories is tree-like: each element can have
sub-elements. It can be delegated by entity.

In the form of a task category, you can find some information about this
category including but not limited to:

- Name
- Parent category

### Task categories

Displays a list of child task categories and allows adding new ones.

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

## Solution types

This list is a list of valid flat values. It can be delegated by entity.

## Request sources

This list is a list of valid flat values for all entities.

It specifies if this source should be defined by default for tickets
and/or collectors.

## Solution templates

This list is a list of valid flat values. It can be delegated by entity.

It allows to predefine the content as well as the type of a solution and
can be visible or not from the sub-entity.

:::info

Solution templates cannot be translated

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

## Project states

This list is a flat value list valid for all entities.

It allows to define the statuses applied to a project as well as its
state.

## Project types

This list is a list of flat values valid for all entities.

It is used to define the types applied to a project.

## Project task types

This list is a flat value list valid for all entities.

It is used to define the types of tasks applied to a project.

## The common tabs

### Translation

This tab is reserved for names and only appears if the translation of
dropdown names has been enabled in the general configuration.

![Dropdown translation tab](../../../assets/modules/configuration/dropdowns/images/dropdown_translation.png)

This tab lists all current translations of the dropdown name and allows
you to add new ones.

### All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

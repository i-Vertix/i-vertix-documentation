---
id: actions
title: Actions
---

# Actions

The different actions that are available on an object depend on the
permissions assigned in user profile.

Likewise, some actions in the tab depend on profile permission, such as
mass actions.

This page describes only main actions that can apply to different types
of objects. If an action is specific to an object, it will be described
in the documentation of this object.

## Creation 

The permission to create an object depend on defined permission in user
profile.

For all inventory objects, creation is realized in the same way:

1.  Connect to i-Vertix ITAM ;
2.  Go to the object page, for example *Assets \> Computers*
    to add a computer ;
3.  Click on the "+" button located in horizontal menu ;
4.  If the inventory object has a template management, choose the
    template to be applied ;
5.  Fill in the different fields of the empty form ;
6.  Validate.

An option located in user preferences, *After creation, go to created
element*, allows to choose, after creating an object, if the newly
created object is displayed or if a new empty form is displayed in order
to create another object.

## Modification

The permission to modify an object depend on defined permission in user
profile.

For all inventory objects, creation is realized in the same way:

1.  Connect to i-Vertix ITAM ;
2.  Go to the object page, for example, to modify a computer, go to
    *Assets \> Computers* ;
3.  Or alternatively: search the object in the search engine available
    on top of objects list ;
4.  Two choices of modification are then possible:

> - Unitary modification:
>
>   > 1.  Click on object name ;
>   > 2.  Modify fields ;
>   > 3.  Click on button **Update**.
>
> - Mass modification:
>
>   > 1.  Select the checkbox located on the left of the object name ;
>   > 2.  Click on button **Actions** ;
>   > 3.  Choose field to be modified ;
>   > 4.  Enter new field value ;
>   > 5.  Click on button **Post**.

## Display

The permission to display an object depend on *read*
permission in user profile.

If the permission to display an object is not granted, the name of this
object will not appear in i-Vertix ITAM different menus. For example, if the
permission to read a *Computer* type object is not granted
in the user's profile, the sub-menu *Computer* will not
appear in menu *Assets*, even if the permission to modify a
*Computer* is granted.

For all inventory objects, displaying an object is realized in the same
way:

1.  Connect to i-Vertix ITAM ;
2.  Go to the object page, for example, to display a computer, go to
    *Assets \> Computers* ;
3.  Or alternatively: search the object in the search engine available
    on top of objects list ;
4.  Click on object name..

## Attaching a document

When available for the item type, attaching a document is realized in
the same way:

1.  Connect to i-Vertix ITAM ;
2.  Go to the object menu, for example, to attach to a computer, go to
    *Assets \> Computers* ;
3.  Or alternatively: search the object in the search engine available
    on top of objects list ;

Two possibilities are available:

- Unitary attachment :

  > 1.  Click on the object name ;
  > 2.  Select tab **Documents** ;
  > 3.  Select a document or click button **Choose** to add a new
  >     document ;
  > 4.  Click on button **Add**.

- Mass attachment :

  > 1.  Select the checkbox located on the left of the object name ;
  > 2.  Click on button **Actions** and choose **Add a Document**

i-Vertix ITAM will then display the object form with newly attached document.

## Attaching a contract

When available for the item type, attaching a contract is realized in
the same way:

1.  Connect to i-Vertix ITAM ;
2.  Go to the object menu, for example, to attach to a computer, go to
    *Assets \> Computers* ;
3.  Or alternatively: search the object in the search engine available
    on top of objects list ;

Two possibilities are available:

- Unitary attachment :

  > 1.  Click on the object name ;
  > 2.  Select tab **Contracts** ;
  > 3.  Select a contract ;
  > 4.  Click on button **Add**.

- Mass attachment :

  > 1.  Select the checkbox located on the left of the object name ;
  > 2.  Click on button **Actions** and choose **Add a Contract**

i-Vertix ITAM will then display the object form with newly attached contract.

## Transfer between entities

Entities open the possibility to define transfer profiles in order to
move elements between entities. This allows in particular to switch from
a single entity i-Vertix ITAM to a i-Vertix ITAM with multiple entities.

To make a transfer, it is first necessary to check that the used profile
has permission to make transfers ([Administration \> Profiles \>
Administration \--\> Transfer read permission]).

In order to make a transfer:

1.  Configure the actions performed by the transfer
    [Administration Rules Transfer](../../modules/administration/rules/rulesmanagement.md) ;
2.  Check that profile performing transfer has permission on the origin
    entity and on the destination entity (simplest solution is to use a
    recursive profile from root entity) ;
3.  Go to root entity (*See all*) ;
4.  From objects list, select the element to be transferred ;
5.  Choose **Add to transfer list** then **Validate** ;
6.  In **Transfer mode**, select a transfer configuration profile that
    has been created at step 2 ;
7.  Select destination entity, where object will be transferred to ;
8.  Click on **Transfer** ;
9.  Check in destination entity that object is effectively there.

:::info

If a linked element does not exist in destination entity, it will be
automatically created if transfer profile asks to keep it.

Example : transfer of a *Computer* with a provider defined
in accounting informations: if this provider exists only in origin
entity, it will be created in destination entity; however, a provider
defined in root entity with recursivity enable will not be recreated.

:::

:::warning

Location and group must be updated for destination entity.

:::

## Deletion

The permission to delete an object depend on *delete*
permission in user profile.

For all inventory objects, deleting an object is realized in the same
way:

1.  Connect to i-Vertix ITAM ;
2.  Go to the object page, for example, to delete a computer, go to
    *Assets \> Computers* ;
3.  Or alternatively: search the object in the search engine available
    on top of objects list ;
4.  Two choices of deletion are then possible:
    - Unitary deletion:

      > 1.  Click on object name ;
      > 2.  Click on button **Delete** ;

    - Mass deletion:

      1.  Select the checkbox located on the left of the object name ;
      2.  Click on button **Actions** ;

In both cases, a choice will have to be made between:

- *Move to trash bin* if object has an associated trash bin. In this
  case, object may be restored later on ;
- *Delete permanently* if object does not have an associated trash bin.
  In this case, i-Vertix ITAM will ask for confirmation before real deletion of
  the object in the database.

---
id: fields-unicity
title: Fields-Unicity
---

# Fields unicity

i-Vertix ITAM has a mechanism to perform uniqueness checks before the creation of
an object in the database.

This allows you to track and/or block the presence of duplicate objects
based on matching certain fields. For example, you can configure a
fields unicity rule for computers using the serial number field. This
applies to manual additions and additions made from an external source
such as an inventory tool.

Uniqueness is defined by a name, an object type, and one or more fields.
When multiple fields are specified, all of them are checked together
instead of individually (Ex: serial number AND UUID match another
computer. Uniqueness checks for fields only apply if the field is not
empty. For example, multiple computers with a blank serial number would
be allowed. Each uniqueness rule has options to refuse the addition of
the object and/or send a notification if it is determined to not be
unique.

Th criteria added in the
[blacklists](intitules/general) will be
ignored when calculating uniqueness.

## The different tabs

### Duplicates

The duplicates tab lists all the values corresponding to the criteria
that are currently duplicated.

#### History

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

#### Debugging information

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

![Debugging page](/modules/tabs/images/debug.png)

#### All Information

For an item, all information is displayed on one page from the *All*
tab. This shows all of the tabs of an object's form in one view, one
below the other.

---
id: group
title: Group
---

# Group

This field, like the user field, corresponds to the membership of the
i-Vertix ITAM object You can add a group manually or create a group directly by
this field.

For groups created from an AD/LDAP(S) or SCIM, please refer to your
internal procedures.

![user](../../assets/tabs/common_fields/images/group.png)

## Create a group

- To create a group, click on **+ Add**
- If it's necessary, check the box **Child entities** (this group will
  be visible in the sub-entity of the one you are in)
- Enter a **Name**
- A **Code** (optional)
- Choose if this group is **Child of**
- Select yes or no to **Recursive membership** (if enabled, members of
  this group will also become implicit members of its children groups)
- You can define whether this group can be **visible in a ticket** (as a
  requester, observer, assigned to, task, can be notified)
- Define if the group can be a **manager in a project**
- Select if this group **can contain** **Items** and/or **Users**
- Click **+ Add**

![user](../../assets/tabs/common_fields/images/add-group-1.png)

![user](../../assets/tabs/common_fields/images/add-group-2.png)

- In this window, you need to add users. In **Users** tab, select those
  you wish to associate with the group (prefer users with a technical or
  higher profile)

![add user in group in charge](../../assets/tabs/common_fields/images/add-users-in-group.png)

1.  Select **user**
2.  Define it this user can be **Manage** group (add/modify members,
    name, etc.)
3.  whether or not to authorise **Delegatee** rights (can open ticket
    for the group)
4.  **Add** your group

Once you have created a group, you can either create another or select
the one you have just created from the drop-down list.

## Delete a group

To delete a group, use the massive action with **Actions** button

![delete location](../../assets/tabs/common_fields/images/delete-location.png)

Or enter in the group you want and click on **Delete permanently**

![delete location](../../assets/tabs/common_fields/images/delete-individual-group.png)

:::info

For more information, see
[groups](../../modules/administration/groups.md)

:::

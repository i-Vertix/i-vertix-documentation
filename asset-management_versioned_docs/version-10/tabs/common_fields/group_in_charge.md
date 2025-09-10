---
id: group_in_charge
title: Group In Charge
---

# Group in charge

A group in charge can modify the information of the computer and his
elements (status, computer type, etc.)

![group in charge](../../assets/tabs/common_fields/images/group-in-charge.png)

For groups created from an AD/LDAP(S) or SCIM, please refer to your
internal procedures.

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

![group in charge](../../assets/tabs/common_fields/images/add-group-in-charge-1.png)

![group in charge](../../assets/tabs/common_fields/images/add-group-in-charge-2.png)

- In this window, you need to add users. In **Users** tab, select those
  you wish to associate with the group (prefer users with a technical or
  higher profile)

![add user in group in charge](../../assets/tabs/common_fields/images/add-users-in-group-charge.png)

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

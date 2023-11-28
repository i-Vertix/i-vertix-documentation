---
id: vault
title: Vault
---


i-Vertix Vault, is a complete internal credential manager (not just passwords), with functionality to be extended in the future.
For now, the i-Vertix Vault can be used for the following 4 types of access:

- **SNMP**
- **SSH**
- **I-VERTIX AGENT** (vmware o.s. discovery only)
- **WSMAN** (vmware o.s. discovery only)

The stored credentials can be used for various utilities such as:

- **NEDI Discovery**
- **Network Discovery**
- **VMware OS Discovery**
- **Meraki**

To access the i-Vertix Vault, you must edit a job configuration such as VMware or Nedi. The i-Vertix Vault is not actually accessible from a dedicated menu item.

In the example configuration below (NEDI Discovery) we have created a new entry (under **Configuration > Hosts > NEDI Configuration**):

![vault](../../version-22.10/assets/vault/vault.gif)

or we can use an entry already present on i-Vertix Vault:

![vault](../../version-22.10/assets/vault/vault_2.gif)

When credentials are changed, these changes will affect ***all*** hosts/configurations where these credentials are used.

To see if credentials have been used check Usage:

![vault](../../version-22.10/assets/vault/usage.png)

to check where they are used click on Edit

![vault](../../version-22.10/assets/vault/edit.png)

this menu will open:

![vault](../../version-22.10/assets/vault/new-menu.png)

In the above example, the credentials selected, are also in use in the NEDI Discovery Job 

:::info

Currently, it is not currently possible to use (make link) of the users/passwords created on the i-Vertix Vault to add them to the host configuration.

:::

One important use of the i-Vertix Vault is to use it to retrieve credentials without using a personal credential store (e.g. keepass); remember that this functionality is subject to ACLs.

:::info

There is a **Master Key** which encrypts all credentials (for Admin users only), it will be randomly generated the first time and can then be changed as required.

You can find the **Master Key** in **Administration > i-Vertix > Vault**:

![vault](../../version-22.10/assets/vault/masterkey.png)

![vault](../../version-22.10/assets/vault/masterkey2.png)

**Master Key is used by the system to decrypt the credentials stored in the db.**

:::

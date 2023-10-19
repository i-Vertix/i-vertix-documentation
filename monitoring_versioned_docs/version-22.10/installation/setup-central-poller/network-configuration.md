---
id: network-configuration
title: Network configuration
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Network configuration

:::caution

Before you start, please be careful to meet the technical requirement (see [Technical Information](../before-you-start/technical-information.md))

Before proceeding to modify the network, be sure to operate from the hypervisor console to avoid loss of connectivity.

:::

<Tabs>
<TabItem value="i-Vertix3" label="i-Vertix3 (Central & Poller)" default>

To configure network settings on **i-Vertix3**:
1. Select option **6** Network settings>
2. Select option **1** Change network settings> (NTUI configuration manager starts up)
3. Select Edit Connection
4. Select the proper NIC (by default **ens192**) and then **Modify** followed by your network settings:
5. IPv4 Configuration: **Manual**
6. Addresses: IP address you want to assign to the Central Manager
7. Gateway: your default gateway IP address
8. DNS server: your DNS Server IP Address
9. Search domain: Insert the domain (if necessary)
10. IPv6 Configuration: **Ignore**

Confirm the settings with **OK**

![NMTUI](../../assets/setup-startup-central-poller/nmtui.png)


---

Get back to main menu NMTUI (on the left-hand side)

1. To activate the new settings, select **Activate a connection** from the NMTUI menu
2. Select the **NIC** (ens192 by default ), then
3. **Deactivate**
4. **Activate**
5. Finally select **Back**

---

Get back to the main NTUI menu
1. Select **Set a system hostname** to configure the system hostname then select **OK**
2. Select **Quit** to quit the **NMTUI** menu and get back to the **i-Vertix menu**

![NMTUI2](../../assets/setup-startup-central-poller/nmtui2.png)

---

Now network configuration is complete (restart the vm if necessary) and the system is accessible via network connection (for example using **Putty**)

You can go to [First login](first-login.md)

</TabItem>
<TabItem value="i-Vertix4" label="i-Vertix4 (Poller)">

To configure network settings on **i-Vertix4**:

1. Select option **6** Network settings>
2. Select Edit Connection
3. Select the proper NIC (by default **ens192**) and then **Modify** followed by your network settings:
4. IPv4 Configuration: **Manual**
5. Addresses: IP address you want to assign to the Central Manager
6. Gateway: your default gateway IP address
7. DNS server: your DNS Server IP Address
8. Search domain: Insert the domain (if necessary)
9. IPv6 Configuration: **Ignore**

Confirm the settings with **OK**

![NMTUI](../../assets/setup-startup-central-poller/nmtui.png)


---

Get back to main menu NMTUI (on the left-hand side)

1. To activate the new settings, select **Activate a connection** from the NMTUI menu
2. Select the **NIC** (ens192 by default ), then
3. **Deactivate**
4. **Activate**
5. Finally select **Back**

---

Get back to the main NTUI menu
1. Select **Set a system hostname** to configure the system hostname then select **OK**
2. Select **Quit** to quit the **NMTUI** menu and get back to the **i-Vertix menu**

![NMTUI2](../../assets/setup-startup-central-poller/nmtui2.png)

---

Now network configuration is complete (restart the vm if necessary) and the system is accessible via network connection (for example using **Putty**)

You can go to [First login](first-login.md)

</TabItem>
</Tabs>
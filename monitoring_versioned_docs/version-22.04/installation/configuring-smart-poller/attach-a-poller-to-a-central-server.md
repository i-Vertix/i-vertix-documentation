---
id: attach-a-poller-to-a-central-server
title: How to attach a Smart Poller to the Central Management
---

# Smart Poller Configuration

## Poller configuration

To attach a Smart Poller to a Central Management, please follow these instructions:

1. go to Configuration -> Pollers -> Pollers

![Poller configuration](../../assets/configuring-smart-poller/poller-attach-1.png)

2. Click on Poller1 **Poller1**
3. Rename **Poller1** with a new name, according to your internal naming convention
4. Enter the IP address of the Smart Poller

![Change IP address](../../assets/configuring-smart-poller/poller-attach-2.png)

5. Save this configuration by clicking **Save** at the top right corner

![Save](../../assets/configuring-smart-poller/save.png)

---

## Broker configuration

1. go to Configuration -> Pollers -> Broker configuration

![Brocker configuration](../../assets/configuring-smart-poller/poller-attach-3.png)

2. Click on Poller1 **Poller1**
3. In the **General** tab rename **Poller1** with a new name, according to your internal naming convention
4. Set the field **"Event queue max size"** to **250000**

![Event queue](../../assets/configuring-smart-poller/poller-attach-4.png)

5. Select **Output** tab and enter the Central Manager IP **"Host to connect to"** filed

![Host to connect to](../../assets/configuring-smart-poller/poller-attach-5.png)

6. Save this configuration by clicking **Save** at the top right corner

![Save](../../assets/configuring-smart-poller/save.png)

---

## Engine configuration

1. go to Configuration -> Pollers -> Engine configuration

![Engine configuration](../../assets/configuring-smart-poller/poller-attach-6.png)

2. Click on Poller1 **Poller1**

3. In **Files** tab configuration Name: replace "Poller1" with a new poller name, as
per your naming convention

![Rename](../../assets/configuring-smart-poller/poller-attach-7.png)

4. Go to **Data** tab and click on **+Add a new entry**

![Add data entry](../../assets/configuring-smart-poller/poller-attach-8.png)

5. Enter these two brocker directive:

![Add data entry empty](../../assets/configuring-smart-poller/poller-attach-9.png)

    1 - */usr/lib64/centreon-engine/externalcmd.so*

    2 - */usr/lib64/nagios/cbmod.so /etc/centreon-broker/poller-module.json*

![Add data entry directive](../../assets/configuring-smart-poller/poller-attach-10.png)

---

## Pollers restart

1. Go to Configuration -> Pollers -> Pollers

![Poller](../../assets/configuring-smart-poller/poller-attach-1.png)

2. Select the Smart Poller that is being configured

![Select Poller](../../assets/configuring-smart-poller/poller-attach-11.png)

3. Click on **Export configuration**

![Export configuration 1](../../assets/configuring-smart-poller/poller-attach-12.png)

4. Select the first 4 options (at left) , then select **Method -> Restart** in the drop down menu

![Export configuration 2](../../assets/configuring-smart-poller/poller-attach-13.png)

:::warning[Mandatory]

The following steps are mandatory

:::

5. Log on to the Central Management (SSH) do a sudo bash and enter the password
6. Launch the following commands:

    1 - *scripts*

    2 - *cd i-vertix/*

    3 - *./sync_poller.sh*
7. In case the system asks for a **yes/no** confirmation answer yes, the CLI will show as many "ok" as the number of Pollers that are being synchronized

:::info

Central Manager performs such a synchronization every 4 hours

:::


8. Final check, select: Configuration -> Pollers -> Pollers

![Configuration](../../assets/configuring-smart-poller/poller-attach-13.png)

Check the configuration is like the one shown
in the picture.

![Final check](../../assets/configuring-smart-poller/poller-attach-14.png)
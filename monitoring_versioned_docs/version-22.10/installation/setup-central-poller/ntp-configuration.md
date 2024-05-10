---
id: ntp-configuration
title: NTP Configuration
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

:::info

Here you can find a list of all usable timezones:

<https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>

:::

<Tabs>
<TabItem value="i-Vertix4" label="i-Vertix4 (Central & Poller)" default>

## Modifying NTP settings on i-Vertix4 Poller

After logging in run the **menu** command

![ivertix-menu](../../assets/setup-startup-central-poller/ivertix-menu-v4.png)

and choose option **5** (i-Vertix Poller Settings)

![ivertix-menu-opt5](../../assets/setup-startup-central-poller/ivertix-menu-opt5-v4.png)

The options will be displayed:

1. NTP time settigs

2. change timezone

By choosing option **2**, you will be able to change the default timezone (Europe/Rome)

![ivertix-default-tz](../../assets/setup-startup-central-poller/change-default-ntp-v4.png)

to the one you want (e.g. Europe/London) you will be prompted to answer yes if you want to change the timezone.

![ivertix-london-2](../../assets/setup-startup-central-poller/change-default-ntp_2-v4.png)

![ivertix-london-3](../../assets/setup-startup-central-poller/change-default-ntp_3-v4.png)

The system will confirm this choice.

![ivertix-london-4](../../assets/setup-startup-central-poller/change-default-ntp_4-v4.png)

And finally

![ivertix-london-4](../../assets/setup-startup-central-poller/change-default-ntp_5-v4.png)

It is preferable, then, to return to the previous menu and choose 1 to set the system time according to the new timezone.

:::note

View the commands below (Example 1-3) for diagnosing any problems

:::

### Examples i-Vertix4

Below are some examples of commands to run to diagnose any problems

#### Example 1 `chronyc tracking`

![chronyc tracking](../../assets/setup-startup-central-poller/chronyc-tracking.png)

#### Example 2 `chronyc sources`

![chronyc sources](../../assets/setup-startup-central-poller/chronyc-sources.png)

#### Example 3 `vi /etc/chrony.conf`

![chrony.conf](../../assets/setup-startup-central-poller/chrony-conf.png)

</TabItem>
<TabItem value="i-Vertix3" label="i-Vertix3 (Central & Poller)">

## Modifying NTP settings on i-Vertix3 Poller

In the system shell follow this procedure:

1. Run the command (root password is required):

    ```bash
    sudo bash
    ```

2. Run the command (to check synchronization, see [Example 1](#example-1-chronyc-tracking)):

    ```bash
    chronyc tracking
    ```

3. Run the command (to che NTP source, see [Example 2](#example-2-chronyc-sources)):

    ```bash
    chronyc sources
    ```

---

## Modifying NTP settings

1. Run the command (root password is required):

    ```bash
    sudo bash
    ```

2. Run the command (see [Example 3](#example-3-vi-etcchronyconf)):

    ```bash
    vi /etc/chrony.conf
    ```

3. Comment (using the *#*) servers 0, 1, 2, 3 and insert the NTP Server address that fit your necessities (if
requested)

4. Save the file

5. Run the command:

    ```bash
    systemctl restart chronyd.service
    ```

### Examples i-Vertix3

Below are some examples of commands to run to diagnose any problems

#### Example 1: `chronyc tracking`

![chronyc tracking](../../assets/setup-startup-central-poller/chronyc-tracking.png)

#### Example 2: `chronyc sources`

![chronyc sources](../../assets/setup-startup-central-poller/chronyc-sources.png)

#### Example 3: `vi /etc/chrony.conf`

![chrony.conf](../../assets/setup-startup-central-poller/chrony-conf.png)

</TabItem>
</Tabs>

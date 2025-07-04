---
id: other
title: Other actions
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


## Management of checks

### Principle

It is possible to temporarily enable or disable check on a host or a service.

> Changes to settings checks do not affect the configuration of the
> object in the database. These changes are made on the supervision in
> real time, they are canceled if the scheduler is restarted.

### Practice

<Tabs groupId="sync">
<TabItem value="From the detailed sheet of an object" label="From the detailed sheet of an object">

1.  Access the details page of the object
2.  In the category: **Options** go to the line: **Active checks** to
    check the state of the checks.

To:

-   Enable the check, click on ![image](../../assets/managing-alarms/enabled.png)
-   Disable the check, click on ![image](../../assets/managing-alarms/disabled.png)

</TabItem>
<TabItem value="From real time monitoring" label="From real time monitoring">

1.  Go into the **Monitoring > Status Details > Hosts** (or **Services**)
    menu
2.  Select the object(s) on which you want to enable or disable the
    check
3.  In the menu: **More actions…** click on:

-   **Hosts : Disable Check** or **Services: Disable Check** to stop the
    check on a host or a service
-   **Hosts: Enable Check** or **Services: Enable Check** to enable the
    check of a host or of a service

</TabItem>
</Tabs>


## Management of notifications

### Principle

It is possible to temporarily enable or disable the notification of a
host or a service.

> Changes the notifications settings do not affect the configuration of
> the object in the database. These changes are made on the real time
> monitoring, they are canceled if the scheduler is restarted.

### Practice

There are two ways of managing the notifications:

<Tabs groupId="sync">
<TabItem value="From the detailed sheet of an object" label="From the detailed sheet of an object">

1.  Access the details page of the object
2.  In the category: **Options** go to the line: **Service
    Notifications**

To:

-   Enable the notification, click on ![image](../../assets/managing-alarms/enabled.png)
-   Disable the notification, click on ![image](../../assets/managing-alarms/disabled.png)

</TabItem>
<TabItem value="From real time monitoring" label="From real time monitoring">

1.  Go into the **Monitoring > Status Details > Hosts** (or **Services**)
    menu
2.  Select the host(s) / service(s) you want enable or disable the
    notification
3.  In the menu: **More actions…** click on:

-   **Hosts: Disable Notification** or **Services: Disable
    Notification** to stop the notification of a host or of a service
-   **Hosts: Enable Notification** or **Services: Enable Notification**
    to enable the notification of a host or a service

</TabItem>
</Tabs>

## Reprogramming checks

### Principle

By default, the checks (checks on a service) are executed at regular
intervals following the configuration defined by the user. It is
possible to interact on the check scheduling pile to change the
programming of the checks.

There are two types of programming:

-   Normal programming: the service check is given priority in the
    scheduler queue (asap).
-   Forced programming: the service check is given priority in the
    scheduler queue (asap) even if the time of the execution request is
    outside the check period or if the service is not of the active
    type.

### Practice

There are two ways of forcing the check of a service:

<Tabs groupId="sync">
<TabItem value="From the detailed sheet of an object" label="From the detailed sheet of an object">

1.  Access the detail page of the object
2.  In the category **Host Commands** (or **Service Commands**), click
    on **Re-schedule the next check for this host / service** or
    **Re-schedule the next check for this host / service (forced)**

</TabItem>
<TabItem value="From real time monitoring" label="From real time monitoring">

1.  Go into the menu: **Monitoring > Status Details > Hosts** (or
    **Services**)
2.  Select the objects to for which you want to force the check
3.  In the menu: **More actions…** click on **Schedule immediate check**
    or **Schedule immediate check (Forced)**

</TabItem>
</Tabs>
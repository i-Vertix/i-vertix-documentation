---
id: acknowledge
title: Acknowledging a problem
---

### Concept

Once an incident is reported and confirmed by a host or service, the notification process is initiated, which may result in sending a notification to a designated contact. If the issue persists, additional alerts may be sent based on the configuration settings, such as periodic resending of notifications or escalating the level of urgency in the notifications.

The acknowledgment of an incident has the ability to halt the notification process (sending of notifications) until the host or service restores its normal status.

Example of use:

A service is charged with checking the health of the hard disks in a disc array. A hard disk goes down on a disk array, a notification is sent. The monitoring operator acknowledges the service specifying that a team is in the process of dealing with the problem. Notifications are no longer sent. The service will return to its nominal state after a change of disk.

:::note

The acknowledgment of an incident indicates that the issue has been acknowledged by a monitoring user, without necessarily implying the resolution of the incident. The actual resolution can only be achieved when the check returns to its normal state.

:::

### Practice

To acknowledge an incident, there are several solutions:

**Resources Status page**

1. Go to **Monitoring > Resources Status**.
2. Use one of the following methods:
    - Select the object(s) that you want to acknowledge, then click the **Acknowledge** button above the list of resources.
    - Hover over the resource you want to acknowledge, then click the **Acknowledge** icon that appears on the left.

        ![image](../../assets/managing-alarms/acknowledge.gif)

    The following window appears:

    ![image](../../assets/managing-alarms/acknowledge_popup.png)

    -   **Comment** is generally used to provide the reason of the acknowledgment. It is mandatory.
    
    -   If the **Notify** box is checked, a notification is sent to the contacts linked to the object to warn that the incident on the resource has been acknowledged (in the situation the contact possesses the activity acknowledgment notification filter).

    -   If the **Persistent** box is checked, the acknowledgment will be maintained even if the monitoring engine is restarted. Otherwise, the acknowledgment disappears and the notification process is reactivated.

    -   If the **Sticky** box is checked, the acknowledgment will be  maintained in case of a change of Not-OK status (E.g.: DOWN to UNREACHABLE or WARNING to CRITICAL). Otherwise, the acknowledgment disappears and the notification process is reactivated.

**Status detail page (host or service)**

1.  Go to **Monitoring > Status Details > Hosts** (or **Services**).
2.  Select the object(s) that you want to acknowledge.
3.  In the menu: **More actions** click on **Hosts: Acknowledge** or on
    **Services: Acknowledge**.

    The following window appears:

![image](../../assets/managing-alarms/set_acknowledge.png)

-   If the **Sticky** box is checked, the acknowledgment will be maintained in case of a change of Not-OK status (E.g.: DOWN to UNREACHABLE or WARNING to CRITICAL). Otherwise, the acknowledgment disappears and the notification process is reactivated.
-   If the **Notify** box is checked, a notification is sent to the contacts linked to the object to warn that the incident on the resource has been acknowledged (in the situation the contact possesses the activity acknowledgment notification filter).
-   If the **Persistent** box is checked, the acknowledgment will be  maintained in the case of a restart of the scheduler. Otherwise, the acknowledgment disappears and the notification process is reactivated.
-   **Comment** is generally used to provide the reason of the acknowledgment, it is mandatory
-   If the **Acknowledge services attached to hosts** box is checked, all the services linked to the host will be acknowledged (option visible only if we acknowledge a host).
-   If the **Force active checks** box is checked, a command will be sent to the scheduler to recheck the resource as soon as possible.

From of the detail page of an object, click on the icon |enabled| associated with the **Acknowledged** field in the **Options** frame.

The following window appears:

![image](../../assets/managing-alarms/set_acknowledge.png)

-   If the **Sticky** box is checked, the acknowledgment will be maintained in case of a change of Not-OK status (E.g.: DOWN to UNREACHABLE or WARNING to CRITICAL). Otherwise, the acknowledgment disappears and the notification process is reactivated.
-   If the **Notify** box is checked, a notification is sent to the contacts linked to the object to warn that the incident on the resource has been acknowledged (in the situation the contact possesses the activity acknowledgment notification filter).
-   If the **Persistent** box is checked, the acknowledgment will be  maintained in the case of a restart of the scheduler. Otherwise, the acknowledgment disappears and the notification process is reactivated.
-   The **Comment** field is generally used to provide the reason of the acknowledgment, it is mandatory
-   If the **Acknowledge services attached to hosts** box is checked, all the services linked to the host will be acknowledged (option visible only if we acknowledge a host).
-   If the **Force active checks** box is checked, a command will be sent to the scheduler to recheck the resource as soon as possible.


### Disacknowledging resources

To delete the acknowledgment on an object:

1. Go to **Monitoring > Resources Status**.
2. Select the objects you want to disacknowledge.
3. On the **More actions** menu, click **Disacknowledge**.

or

1.  Go to **Monitoring > Status Details > Hosts** (or **Services**).
2.  Select the objects you want to disacknowledge.
3.  In the **More actions** menu, click on **Hosts: Disacknowledge** or
    on **Services: Disacknowledge**

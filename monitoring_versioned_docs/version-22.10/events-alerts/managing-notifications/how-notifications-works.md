---
id: how-notifications-works
title: How notification works
---

IT Monitoring checks Hosts and Services status every polling cycle; if the Service is "passive", IT Monitoring listens to incoming messages.

If an issue is detected, the Host or the Service goes into **SOFT Non-OK** status. (see “Host and service states and status types“ slide)

After the number of polls set in “Max Check Attempts“, if the Host or the Service is still in Non-OK status, it goes into **HARD Non-OK** status and notifications can be triggered.
 
**Notifications are sent**, using the relevant notification action/script, **if**:

1. They are enabled on the Host or Service
2. At least 1 contact is configured to receive the notification(s) about the specific Host or Service status
3. A notification period (period of time during which notifications are to be sent) has been defined and current time is within it

:::note 

“Max Check Attempts“ setting is applicable only to Non-OK status. OK status is always HARD.

:::

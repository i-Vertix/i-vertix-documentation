---
id: ntp-configuration
title: NTP configuration
---

# Configuration of NTP (CLI)

In the system shell follow this procedure:

1. Run the command *sudo bash* (root password is required)
2. Launch the command *chronyc tracking* (to check synchronization, see ex. 1)
3. Run the command *chronyc sources* (to che NTP source, see ex. 2)

---

## Modifying NTP settings

1. Run the command *sudo bash* (root password is required)
2. Run the command *vi /etc/chrony.conf* (see ex. 3)
3. Comment (using the *#*) servers 0, 1, 2, 3 and insert the NTP Server address that fit your necessities (if
requested)
4. Save the file
5. Run the command:
```bash
systemctl restart chronyd.service
```

---
### Examples

#### Example 1

![chronyc tracking](../../assets/setup-startup-central-poller/chronyc-tracking.png)

#### Example 2

![chronyc sources](../../assets/setup-startup-central-poller/chronyc-sources.png)

#### Example 3

![chrony.conf](../../assets/setup-startup-central-poller/chrony-conf.png)
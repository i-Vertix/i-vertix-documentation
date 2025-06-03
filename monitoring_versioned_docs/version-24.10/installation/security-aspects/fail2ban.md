---
id: fail2ban
title: Fail2ban
---

### Fail2ban

Fail2Ban is an intrusion prevention software framework that protects computer servers from brute-force attacks.

This framework is already installed on Central Management and Smart Poller.

These are some command line examples (launch these command as admin):

Please use the following procedure to unban a blocked IP address:

1. Check fail2ban status

```

sudo fail2ban-client status
Status
|- Number of jail:      2
`- Jail list:   centreon, sshd

```

2. Check details of a file2ban jail

```

sudo fail2ban-client status sshd
Status for the jail: sshd
|- Filter
|  |- Currently failed: 0
|  |- Total failed:     52975
|  `- Journal matches:  _SYSTEMD_UNIT=sshd.service + _COMM=sshd
`- Actions
   |- Currently banned: 0
   |- Total banned:     11211
   `- Banned IP list: 89.43.23.14

```

3. Unban a banned IP

```

sudo fail2ban-client set sshd unbanip 89.43.23.14

```
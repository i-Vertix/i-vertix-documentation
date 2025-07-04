---
id: fail2ban
title: Fail2ban
---

### Fail2ban

Fail2Ban is an intrusion prevention software framework that protects computer servers from brute-force attacks.

This framework is already installed on Central Management and Smart Poller.

These are some command line examples (launch these command as root):

1. fail2ban-client status centreon  \<-- this check the banned ip
2. fail2ban-client set centreon unbanip \<IP\> \<-- this unban the ip

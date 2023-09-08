---
id: technical-information
title: Tables of network flows
---

## Network flows to integrate monitoring platform to IT

### Central server

| From           | To             | Protocol   | Port               | Application                                                                        |
|----------------|----------------|------------|--------------------|------------------------------------------------------------------------------------|
| Central  | NTP server     | NTP        | UDP 123            | Synchronization of the system clock                                                |
| Central  | DNS server     | DNS        | UDP 53             | Domain name resolution                                                             |
| Central  | SMTP server    | SMTP       | TCP 25             | Notification via email                                                             |
| Central  | LDAP(s) server | LDAP, LDAPS    | TCP 389, 636      | Authentication to access the Centreon web interface                                |
| Central  | HTTP     | HTTP, HTTPS    | TCP 80, 443 | System uptades, Push Notification |

### Poller

| From   | To          | Protocol   | Port               | Application                                    |
|--------|-------------|------------|--------------------|------------------------------------------------|
| Poller | NTP server  | NTP        | UDP 123            | Synchronization of the system clock            |
| Poller | DNS server  | DNS        | UDP 53             | Domain name resolution                         |
| Poller | SMTP server | SMTP       | TCP 25             | Notification via email                         |
| Poller | HTTP     | HTTP, HTTPS    | TCP 80, 443 | System uptades, Push Notification, SSL VPN * |

:::note

If you are using a **SSL VPN** connection between Smart Poller and Central Manager you don’t need to configure any specific firewall settings.

:::

### Tables of platform flows (Central/Poller)

| From           | To             | Protocol     | Port         | Application                                                        |
|----------------|----------------|--------------|--------------|--------------------------------------------------------------------|
| Central  | Poller         | ZMQ          | TCP 5666     | Export of configuration |
| Central  | Poller         | SSH  | TCP 22       | Export of configuration (legacy), NCB, Sync Job |
| Poller         | Central  | BBDO         | TCP 5669     | Transfer of collected data                                         |

---

### Monitoring protocols

| From              | To                               | Protocol   | Port      | Application |
|-------------------|----------------------------------|------------|-----------|-------------|
| Poller            | Network equipment, servers, etc. | SNMP       | UDP 161   | Monitoring  |
| Network device | Poller                           | Trap SNMP  | UDP 162   | Monitoring  |
| Poller            | Servers                          | NSClient++ | HTTPS 8443 | Monitoring  |

:::note

Other flows can be necessary to monitor databases, access to API, or application ports.

:::

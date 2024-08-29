---
id: network-ports
title: Network Ports
---

### Tables of platform flows (Central/Poller)


| From           | To             | Protocol     | Port         | Application                                                        |
|----------------|----------------|--------------|--------------|--------------------------------------------------------------------|
| Central  | Poller         | ZMQ          | TCP 5666     | Export of configuration |
| Central  | Poller         | SSH  | TCP 22       | Export of configuration (legacy), NCB, Sync Job |
| Poller         | Central  | BBDO         | TCP 5669     | Transfer of collected data                                         |

---

:::note

See the complete [tables of network flows](../../installation/before-you-start/technical-information.md)

:::
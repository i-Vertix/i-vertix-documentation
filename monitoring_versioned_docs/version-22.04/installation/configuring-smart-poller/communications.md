---
id: communications
title: Communications
---

## Communication between Central Manager and Smart Poller

Even though Gorgone is being installed on Pollers, it is
allowed to communicate with them (from Central server and a Poller) using SSH protocol.

Although the SSH communication type is allowed, it must be used for
transitioning from older platform that were using Centcore to a full-ZMQ
platform.

> Pollers that will not use ZMQ as communication type
> between Central's Gorgone and theirs will not benefit from all i-Vertix
> and i-Vertix's extensions features.



<Tabs groupId="sync">
<TabItem value="Modern (recommended)" label="Modern (recommended)">

| Communications                        | Allowed actions                                                           |
|---------------------------------------|---------------------------------------------------------------------------|
| **Central** <-- *ZMQ* --\> **Poller** | Monitoring actions\*, Engine/Broker statistics collection, Host Discovery |

</TabItem>
<TabItem value="Legacy (ex-Centcore)" label="Legacy (ex-Centcore)">

| Communications                        | Allowed actions                                                           |
|---------------------------------------|---------------------------------------------------------------------------|
| **Central** <-- *SSH* --\> **Poller** | Monitoring actions\*, Engine/Broker statistics collection, Host Discovery |

</TabItem>
</Tabs>

\* Monitoring actions are all actions provided by Centreon UI like downtimes,
acknowledgements, etc and configuration export.


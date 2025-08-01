---
id: requirements
title: i-Vertix Requirements
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Virtualization compatibility

i-Vertix Central and Pollers support multiple virtualisation and hyperscaling platforms including

| **Platform**   | **i-Vertix 4** |
|-----------------|----------------|
| **VMware**      | 6.7 or higher  |
| **Hyper-V**     | yes            |
| **KVM**         | yes            |
| **Nutanix**     | yes            |
| **Sangfor**     | yes            |
| **AWS EC2**     | yes            |
| **Azure VM**    | yes            |

## Sizing recommendations

The resources needed for optimal performance depend on the product configuration. Adding more hosts, services and other
configuration options may increase the server and database workload. Therefore, server configuration adjustments may be
necessary to optimize performance for your specific environment.

<Tabs>
<TabItem value="1000" label="1.000 Hosts" default>

Architecture: Distributed

* 1 i-Vertix Central server
* 2 i-Vertix Poller (one Poller for every 500 hosts)

**i-Vertix Central server**

| **Resource** | **Value** |
|---------------|-------------------|
| CPU           | 4 vCPU            |
| RAM           | 8 GB              |
| HDD           | 150 GB or greater |

**i-Vertix Poller**

To handle production environments (up to 7.000 services with checks every 5 minutes)

| **Resource** | **Value** |
|---------------|-----------|
| CPU           | 4 vCPU    |
| RAM           | 4 GB      |
| HDD           | 60        |

</TabItem>
<TabItem value="2500" label="2.500 Hosts">

Architecture: Distributed

* 1 i-Vertix Central server
* 5 i-Vertix Poller (one Poller for every 500 hosts)

**i-Vertix Central server**

| **Resource** | **Value** |
|---------------|-----------|
| CPU           | 4 vCPU    |
| RAM           | 8 GB      |
| HDD           | 750 GB    |

**i-Vertix Poller**

To handle production environments (up to 7.000 services with checks every 5 minutes)

| **Resource** | **Value** |
|---------------|-----------|
| CPU           | 4 vCPU    |
| RAM           | 4 GB      |

</TabItem>
<TabItem value="5000" label="5.000 Hosts">

Architecture: Distributed

* 1 i-Vertix Central server without database
* 1 Database server
* 10 i-Vertix Poller (one Poller for every 500 hosts)

**i-Vertix Central server**

| **Resource** | **Value** |
|---------------|-----------|
| CPU           | 4 vCPU    |
| RAM           | 8 GB      |
| HDD           | 750 GB    |

**Database server**

| **Resource** | **Value** |
|---------------|-----------|
| CPU           | 4 vCPU    |
| RAM           | 12 GB     |
| HDD           | 500 GB    |

**i-Vertix Poller**
To handle production environments (up to 7.000 services with checks every 5 minutes)

| **Resource** | **Value** |
|---------------|-----------|
| CPU           | 4 vCPU    |
| RAM           | 4 GB      |

</TabItem>
<TabItem value="10000" label="10.000 Hosts">

Architecture: Distributed

* 1 i-Vertix Central server without database
* 1 Database server
* 20 i-Vertix Poller (one Poller for every 500 hosts)

**i-Vertix Central server**

| **Resource** | **Value** |
|---------------|-----------|
| CPU           | 4 vCPU    |
| RAM           | 8 GB      |
| HDD           | 750 GB    |

**Database server**

| **Resource** | **Value** |
|---------------|-----------|
| CPU           | 8 vCPU    |
| RAM           | 16 GB     |
| HDD           | 1 TB      |

**i-Vertix Poller**
To handle production environments (up to 7.000 services with checks every 5 minutes)

| **Resource** | **Value** |
|---------------|-----------|
| CPU           | 4 vCPU    |
| RAM           | 4 GB      |

</TabItem>
<TabItem value="over-10000" label="Over 10.000 Hosts">

For large amounts of data, contact us directly and our experts will help you.

</TabItem>
</Tabs>

:::tip

**Database server**

The database can also be installed in a **high available** (cluster) configuration upon request. This effectively
prevents potential data loss.

**i-Vertix Poller**

To effectively handle the load of monitoring, it is recommended to have a **dedicated Poller** for every 500 hosts or
7.000 services.

:::

See also [Prerequisites](../../installation/before-you-start/prerequisites.md)
and [Architecture](../../installation/before-you-start/architecture.md)

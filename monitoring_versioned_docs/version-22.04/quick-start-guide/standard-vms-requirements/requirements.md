---
id: requirements
title: i-Vertix Requirements
---

The resources needed for optimal performance depend on the product configuration. Adding more devices, monitors/services and other configuration options may increase the server and database workload. Therefore, server configuration adjustments may be necessary to optimize performance for your specific environment.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="central" label="i-Vertix Central Manager" default>
    Recommended specifications
    * Hypervisor: VMware, Hyper-V, KVM, Nutanix
    * CPU: 2+ vCPU (logical core at 3Ghz)
    * RAM: 8 GB 
    * HDD: 250GB or greater

    :::note
    The **disk space** requirements on i-Vertix Central are primarily influenced by the following factors:
     * The number of metrics (a service can have multiple metrics)
     * The monitoring frequency
     * The database retention period
     Additionally, the **number of CPUs** required also depends on the number of users connected to the interface simultaneously.
    :::

  </TabItem>
  <TabItem value="poller" label="i-Vertix Poller">
    Recommended specifications
    * Hypervisor: VMware, Hyper-V, KVM, Nutanix 
    * CPU: 2+ vCPU (logical core at 3Ghz)
    * RAM: 4GB
    * HDD: 60GB

    :::note
    The **number of CPUs** needed for a i-Vertix Poller varies based on the quantity and frequency of services being used. In order to effectively manage production environments, where there are up to 7.000 services with checks occurring every 5 minutes, it is recommended to have a minimum of 4 vCPUs.
    :::

  </TabItem>
</Tabs>

:::tip
To effectively handle the load of monitoring, it is recommended to have a **dedicated Poller** for every 500 hosts or 7.000 services.
:::

See also [Prerequisites](../../installation/before-you-start/prerequisites.md) and [Architecture](../../installation/before-you-start/architecture.md)

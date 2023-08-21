---
id: monitoring-host
title: Monitoring Host
---

> The list of hosts is shown on page **Configuration > Hosts > Hosts**.

How to create host:

- [create hosts manually](create-host-automatically.md), using [host templates](host-templates.md)
- use the [discovery feature](../discovery/description.md)

## Requirements

Before you run automatic network scans and start monitoring hosts/services, make sure that:

* you configured the devices that are to be monitored so that they can be queried by i-Vertix IT Monitoring and monitoring protocols are allowed on any Firewalls that are in the middle 
* you have all the **required credentials**:

> * Network devices: SNMP communities (required for Host Discovery and Network Discovery)
> * Linux OS devices: SNMP communities and/or SSH credentials (required for Host Discovery)
> * Windows systems: SNMP communities and/or WinRM credentials (you can also deploy an Agent)
> * VMware: a read-only vCenter user
> * Meraki: token API

Also, download from the [Plugin Store](../monitoring-basics/plugin-packs.md) and install any **plugins** you need to monitor your IT environment.

> Select: **Administration -> i-Vertix -> Plugin Store**.

![PluginStore](../../assets/monitoring-resources/monitoring-host/plugin-store.png)

## Installation procedure
1. Search for the required plugins by using the filters
2. Click on plugin icon to see which application/DB/device/device family/etc. the plugin applies to, which monitoring protocol/technology it uses to collect monitoring information, which status parameters and performance metrics it monitors, which discovery types can apply plugin components automatically

![APC](../../assets/monitoring-resources/monitoring-host/apc-example.png)

3. Select required plugins and click on "+ INSTALL"

![APC](../../assets/monitoring-resources/monitoring-host/plugin-install.png)




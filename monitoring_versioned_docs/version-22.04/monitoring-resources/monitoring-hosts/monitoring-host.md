## Overview

Monitoring a host refers to the process of continuously observing and gathering data about the performance, availability, and health of device (server, network device, host esxi, APC, UPS, etc.). The main objectives of monitoring a host are:

**Performance Monitoring**: It involves tracking various metrics related to the host's performance, such as CPU usage, memory utilization, disk activity, network traffic, and response times. This helps identify any performance bottlenecks, resource constraints, or abnormal behavior that may affect the overall system performance.

**Availability Monitoring**: It focuses on ensuring that the host is accessible and operational. This includes monitoring network connectivity, checking if the host is online or offline, and detecting any network or system failures. Monitoring tools often use ping or heartbeat checks to verify the availability of a host.

**Health and Resource Monitoring**: This involves monitoring the health and status of hardware components, software services, and critical resources on the host. It may include monitoring temperature, voltage levels, storage capacity, system logs, and the status of critical processes or services. By tracking these indicators, potential issues can be detected early on and preventive measures can be taken.

> The list of hosts is shown on page **Configuration > Hosts > Hosts**.

How to create host:

- [create hosts manually](./create-host-automatically.md), using [host templates](./host-templates.md)
- use the [hosts discovery feature](../discovery/description.md)

## Requirements

Before you run automatic network scans and start monitoring hosts/services, make sure that:

* you configured the devices that are to be monitored so that they can be queried by i-Vertix IT Monitoring and monitoring protocols are allowed on any Firewalls that are in the middle 
* you have all the **required credentials**:

> * Network devices: SNMP communities (required for Host Discovery and Network Discovery)
> * Linux OS devices: SNMP communities and/or SSH credentials (required for Host Discovery)
> * Windows systems: SNMP communities and/or WinRM credentials (you can also deploy an Agent)
> * VMware: a read-only vCenter user
> * Meraki: token API

Also, download from the [Plugin Store](../monitoring-basics/plugin_packs.md) and install any **plugins** you need to monitor your IT environment.

> Select: **Administration -> i-Vertix -> Plugin Store**.

[//]: # (![PluginStore]&#40;./assets/plugin-store.png&#41;)

## Installation procedure
1. Search for the required plugins by using the filters
2. Click on **«i»** to see which application/DB/device/device family/etc. the plugin applies to, which monitoring protocol/technology it uses to collect monitoring information, which status parameters and performance metrics it monitors, which discovery types can apply plugin components automatically

[//]: # (![APC]&#40;./assets/apc-example.png&#41;)

3. Select required plugins and click on "+ INSTALL"

[//]: # (![APC]&#40;./assets/plugin-install.png&#41;)




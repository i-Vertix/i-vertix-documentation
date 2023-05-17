---
id: prerequisites
title: Prerequisites
---

## Solution Sizing Questionnaire (long version)

Total number of devices that are to be monitored (network devices, servers, virtual hosts and guests, UPSs, cloud hosts, web server hosts/URLs, storages, etc.). This is required to determine the proper license tier.

* Approximate number of monitors/services/sensors that are to be monitored. This is useful to size HW specs and the number of Smart Pollers. Note: a monitor/service/sensor is a single monitoring element: a status parameter or a performance metric. E.g.: PING, Interface, CPU load, etc.

* IT Environment architecture: is the infrastructure centralized (single site) or distributed across multiple network sites/Datacenters? In case of geographically distributed network, are remote site “well-connected” to the Datacenter? In other words, are they connected via a fast, always-up network connection? This is useful to determine the number of Smart Pollers and which type of deployment is required according to Customer’s datacenter and networking specification and constraints.

* Total number of network devices (switches, routers, firewalls, etc.) requiring configuration file backup (if any). This is required to determine if Network Configuration Backup addon is necessary and its tier.

* If “Total number of devices that are to be monitored” < 1000: Do you need layer 2 network topology discovery and mapping? If yes, how many network devices require configuration backup? This is necessary to determine if Network topology discovery and mapping addon is necessary and its tier. 

It’s also good to know: type of network devices, servers and their Operating Systems, applications, databases, storage systems, cloud environments, virtual environments, etc. that are to be monitored. This is useful to check if all monitoring profiles are already available or new ones would have to be developed. 

## i-Vertix IT Monitoring Server Requirements
The resources needed for optimal performance depend on the product configuration. Addingmore devices, monitors/services and other configuration options may increase the server and database workload. Therefore, server configuration adjustments may be necessary to optimize performance for your specific environment.

### i-Vertix Central Manager
**Recommended specifications**
* Hypervisor: VMware
* CPU: 4 3+GHz vCPU *
* RAM: 8+GB
* HDD: 250GB or greater **

**Notes**:

*: exact number of required CPUs depends on frequency and type of monitors
**: Disk space required to store collected status and performance data depends on several factors, such as: polling interval, number and type of monitors and data retention period

### i-Vertix Smart Poller
* Hypervisor: VMware
* CPU: 2 vCPU
* RAM: 8GB
* HDD: 60GB

A poller can monitor on average 10.000 services/monitors.

The table below describes requirements for i-Vertix IT Monitoring Server:

| Number of Services | Estimated number of hosts | Number of pollers | Central | Poller |
| --- | --- | --- | --- | --- |
| <500 | 50 | 1 central | 1 vCPU 4 GB | - |
| 500 – 2.000 | 50 – 200 | 1 central | 2 vCPU 4 GB | - |
| 2.000 – 7.000 | 200 – 700 | 1 central, 1 poller | 4 vCPU 4 GB | 2 vCPU 4 GB |
| 7.000 – 14.000 | 700 – 1.400 | 1 central, 2 poller | 4 vCPU 8 GB | 2 vCPU 4 GB |
| 21.000 – 28.000 | 2.100 – 2.800 | 1 central, 3 poller | 4 vCPU 8 GB | 2 vCPU 4 GB |

### Define disk space
The space used to store collected performance data depends on several criteria:
* Frequency of controls
* Number of controls
* Retention time

The following table provides an estimate of disk space required for your platform assuming:

* Data is collected every 5 minutes
* The retention period is 6 months
* Each performance graph has 2 curves

| Number of Services | /var/lib/mysql (in GB) | /var/lib/centreon (in GB) |
| --- | --- | --- |
| 500 | 10 | 2,5 |
| 2.000 | 42 | 10 |
| 10.000 | 93 | 27 |
| 20.000| 186 | 54 |
| 50.000| 465 | 135 |
| 100.000| 930 | 270 |
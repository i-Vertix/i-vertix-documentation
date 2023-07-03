---
id: poller-requirements
title: Smart Poller requirements
---

The resources needed for optimal performance depend on the product configuration. Adding more devices, monitors/services and other configuration options may increase the server and database workload. Therefore, server configuration adjustments may be necessary to optimize performance for your specific environment.

### i-Vertix Smart Poller
**Recommended specifications**
* Hypervisor: VMware 
* CPU: 2 vCPU 
* RAM: 8GB
* HDD: 60GB
 
A poller can monitor on average 10.000 services/monitors.


Notes:

*: exact number of required CPUs depends on frequency and type of monitors
**: Disk space required to store collected status and performance data depends on several factors, such as: polling interval, number and type of monitors and data retention period

See also [Prerequisites](../../installation/before-you-start/prerequisites.md) and [Architecture](../../installation/before-you-start/architecture.md)
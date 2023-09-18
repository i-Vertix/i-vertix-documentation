---
id: windows-snmp
title: Windows SNMP
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Pack assets

### Templates

The Plugin Pack **Windows SNMP** brings a host template:

* **Windows-Server-SNMP**

The Plugin Pack brings the following service templates (sorted by the host template they are attached to):

<Tabs groupId="sync">
<TabItem value="Windows-Server-SNMP" label="Windows-Server-SNMP">

| Service Alias                 | Service Template                             | Service Description                                                                                                                                     |
|:------------------------------|:---------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU                           | os-windows-snmp-cpu                          | Check the rate of utilization of the CPU for the machine. This check can give the average CPU utilization rate and the rate per CPU for multi-core CPUs |
| Disk C                        | os-windows-snmp-storage-C                    | Check the rate of used space on a disk                                                                                                                  |
| Memory usage                  | os-windows-snmp-memory                       | Check the rate of the utilization of memory                                                                                                             |
| Ntp                           | os-windows-snmp-time                         | Check the synchronization with an NTP server                                                                                                            |
| Service DHCP Client           | os-windows-snmp-service-dhcp-client          | Check if Windows service **DHCP Client** is started                                                                                                     |
| Service DNS Client            | os-windows-snmp-service-dns-client           | Check if Windows service **DNS Client** is started                                                                                                      |
| Service Plug and Play         | os-windows-snmp-service-plug-and-play        | Check if Windows service **Plug and Play** is started                                                                                                   |
| Service Server                | os-windows-snmp-service-server               | Check if Windows service **Server** is started                                                                                                          |
| Service TCP/IP NetBIOS Helper | os-windows-snmp-service-tcpip-netbios-helper | Check if Windows service **TCP/IP NetBIOS Helper** is started                                                                                           |
| Service Windows Event Log     | os-windows-snmp-service-windows-event-log    | Check if Windows service **Windows Eventlog** is started                                                                                                |
| Service Workstation           | os-windows-snmp-service-workstation          | Check if Windows service **Workstation** is started                                                                                                     |
| Swap usage                    | os-windows-snmp-swap                         | Check the rate of the utilization of virtual memory                                                                                                     |
| Uptime                        | os-windows-snmp-uptime                       | Check the uptime of the Windows server since the last reboot                                                                                            |

> The services listed above are created automatically when the **Windows-Server-SNMP** host template is used.

</TabItem>
<TabItem value="Not attached to a host template" label="Not attached to a host template">

| Service Alias | Service Template             | Service Description                                     | Discovery |
|:--------------|:-----------------------------|:--------------------------------------------------------|:----------|
| Disk          | os-windows-snmp-storage      | Check the rate of used space on a disk (filter by name) | X         |
| Interface     | os-windows-snmp-interfaces   | Check the bandwidth of interfaces                       | X         |
| Service       | os-windows-snmp-service      | Check if Windows services are started                   | X         |
| Process count | os-windows-snmp-processcount | Check if Windows processes are started                  | X         |

> The services listed above are not created automatically when a host template is applied. To use
> them, [create a service manually](/docs/monitoring/basic-objects/services), then apply the service template you want.

> If **Discovery** is checked, it means a service discovery rule exists for this service template.

</TabItem>
</Tabs>

### Discovery rules

#### Host discovery

| Rule name      | Description                                         |
|:---------------|:----------------------------------------------------|
| Host Discovery | Discover your resources through a SNMP subnet scan. |

More information about discovering hosts automatically is available on
the [dedicated page](/docs/monitoring/discovery/hosts-discovery).

#### Service discovery

| Rule name                  | Description                                                   |
|:---------------------------|:--------------------------------------------------------------|
| os-windows-snmp-interfaces | Discover network interfaces and monitor bandwidth utilization |
| os-windows-snmp-processes  | Discover processes and monitor their system usage             |
| os-windows-snmp-service    | Discover services and monitor their running status            |
| os-windows-snmp-storage    | Discover the disk partitions and monitor space occupation     |

More information about discovering services automatically is available on
the [dedicated page](/docs/monitoring/discovery/services-discovery)
and in the [following chapter](/docs/monitoring/discovery/services-discovery/#discovery-rules).

### Collected metrics & status

Here is the list of services for this connector, detailing all metrics linked to each service.

<Tabs groupId="sync">
<TabItem value="CPU" label="Cpu">

| Metric name                               | Unit |
|:------------------------------------------|:-----|
| cpu.utilization.percentage                | %    |
| *cpu_num*#core.cpu.utilization.percentage | %    |

> To obtain this new metric format, include **--use-new-perfdata** in the **EXTRAOPTIONS** service macro.

</TabItem>
<TabItem value="Disk-*" label="Disk-*">

| Metric name                           | Unit |
|:--------------------------------------|:-----|
| storage.partitions.count              |      |
| *disk_name*#storage.space.usage.bytes | B    |
| *disk_name*#storage.access.count      |      |

> Applies to the following service templates: os-windows-snmp-storage, os-windows-snmp-storage-C

> To obtain this new metric format, include **--use-new-perfdata** in the **EXTRAOPTIONS** service macro.

</TabItem>
<TabItem value="Memory" label="Memory">

| Metric name        | Unit |
|:-------------------|:-----|
| memory.usage.bytes | B    |

> To obtain this new metric format, include **--use-new-perfdata** in the **EXTRAOPTIONS** service macro.

</TabItem>
<TabItem value="NTP" label="NTP">

| Metric name         | Unit |
|:--------------------|:-----|
| time.offset.seconds | s    |

> To obtain this new metric format, include **--use-new-perfdata** in the **EXTRAOPTIONS** service macro.

</TabItem>
<TabItem value="Process count" label="Process count">

| Metric name | Unit |
|:------------|:-----|
| nbproc      | N/A  |
| mem_total   | B    |
| mem_avg     | B    |
| cpu_total   | %    |

</TabItem>
<TabItem value="Service-*" label="Service-*">

| Metric name                     | Unit |
|:--------------------------------|:-----|
| services.active.count           |      |
| services.continue.pending.count |      |
| services.pause.pending.count    |      |
| services.paused.count           |      |
| service status                  |      |

</TabItem>
<TabItem value="Swap usage" label="Swap usage">

| Metric name      | Unit |
|:-----------------|:-----|
| swap.usage.bytes | B    |

</TabItem>
<TabItem value="Interfaces" label="Interfaces">

| Metric name                                               | Unit |
|:----------------------------------------------------------|:-----|
| interface status                                          |      |
| *interface_name*#interface.traffic.in.bitspersecond       | b/s  |
| *interface_name*#interface.traffic.out.bitspersecond      | b/s  |
| *interface_name*#interface.packets.in.error.percentage    | %    |
| *interface_name*#interface.packets.in.discard.percentage  | %    |
| *interface_name*#interface.packets.out.error.percentage   | %    |
| *interface_name*#interface.packets.out.discard.percentage | %    |

</TabItem>
<TabItem value="Uptime" label="Uptime">

| Metric name           | Unit |
|:----------------------|:-----|
| system.uptime.seconds | s    |

> To obtain this new metric format, include **--use-new-perfdata** in the **EXTRAOPTIONS** service macro.

</TabItem>
</Tabs>

## Prerequisites

### SNMP Configuration

To use this pack, the SNMP service must be properly configured on your Windows server. Please refer to
the [Microsoft Knowledgebase to configure SNMP on your server](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/configure-snmp-service)

### Network flow

The target resource must be reachable from the i-Vertix poller on the UDP/161
SNMP port.

## Using the Plugin Pack

### Using a host template provided by the Plugin Pack

1. Log into i-Vertix and add a new host through **Configuration > Hosts**.
2. Fill the **Name**, **Alias** & **IP Address/DNS** fields according to your ressource settings.
3. Apply the **Windows-Server-SNMP** template to the host.

> Windows does not support SNMP v3 and SNMP is a deprecated feature. We recommend to use SNMP v1.

| Macro      | Description                                                                    | Default value | Mandatory |
|:-----------|:-------------------------------------------------------------------------------|:--------------|:---------:|
| EXTRA-OPTS | Any extra option you may want to add to every command (E.g. a --verbose flag). |               |           |

4. [Deploy the configuration](/docs/monitoring/monitoring-servers/deploying-a-configuration). The host appears in the
   list of hosts, and on the **Resources Status** page. The command that is sent by the connector is displayed in the
   details panel of the host: it shows the values of the macros.

### Using a service template provided by the Plugin Pack

1. If you have used a host template and checked **Create Services linked to the Template too**, the services linked to
   the template have been created automatically, using the corresponding service templates.
   Otherwise, [create manually the services you want](/docs/monitoring/basic-objects/services) and apply a service
   template to them.
2. Fill in the macros you want (e.g. to change the thresholds for the alerts). Some macros are mandatory (see the table
   below).

<Tabs groupId="sync">
<TabItem value="Cpu" label="Cpu">

| Macro            | Description                                                                  | Default value | Mandatory |
|:-----------------|:-----------------------------------------------------------------------------|:--------------|:---------:|
| WARNING-AVERAGE  | Warning threshold average CPU utilization                                    | 80            |           |
| WARNING-CORE     | Warning threshold average single core CPU utilization                        |               |           |
| CRITICAL-AVERAGE | Critical threshold average CPU utilization                                   | 90            |           |
| CRITICAL-CORE    | Critical threshold average single core CPU utilization                       |               |           |
| EXTRA-OPTS       | Any extra option you may want to add to the command (E.g. a --verbose flag). |               |           |

</TabItem>
<TabItem value="Disk" label="Disk">

| Macro             | Description                                                                                                            | Default value                                                      | Mandatory |
|:------------------|:-----------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|:---------:|
| STORAGE           | Set the storage name like C, D (empty means 'check all storages')                                                      |                                                                    |           |
| WARNING-USAGE     | Warning threshold                                                                                                      | 85                                                                 |           |
| CRITICAL-USAGE    | Critical threshold                                                                                                     | 90                                                                 |           |
| UNIT              | Unit of thresholds (Default: '%') ('%', 'B')                                                                           | %                                                                  |           |
| EXTRA-OPTS        | Any extra option you may want to add to the command (E.g. a --verbose flag).                                           |                                                                    |           |
| TRANSFORMSRC      | Modify the disk name displayed by using a regular expression (pattern matching). This option is defined on the command | \\().*                                                             |           |
| EXTENDED-PERFDATA | Extend performance datas: add's space usage in %. This option is defined on the command                                | storage.space.usage.bytes,storage.space.usage.percentage,percent() |           |

</TabItem>
<TabItem value="Memory usage" label="Memory usage">

| Macro           | Description                                                                  | Default value | Mandatory |
|:----------------|:-----------------------------------------------------------------------------|:--------------|:---------:|
| WARNING-MEMORY  | Warning threshold                                                            | 85            |           |
| CRITICAL-MEMORY | Critical threshold                                                           | 90            |           |
| UNIT            | Unit of thresholds (Default: '%') ('%', 'B')                                 | %             |           |
| EXTRA-OPTS      | Any extra option you may want to add to the command (E.g. a --verbose flag). |               |           |

</TabItem>
<TabItem value="NTP" label="NTP">

| Macro           | Description                                                                  | Default value | Mandatory |
|:----------------|:-----------------------------------------------------------------------------|:--------------|:---------:|
| WARNING-OFFSET  | Time offset warning threshold (in seconds)                                   | -2:2          |           |
| CRITICAL-OFFSET | Time offset critical Threshold (in seconds)                                  | -5:5          |           |
| EXTRA-OPTS      | Any extra option you may want to add to the command (E.g. a --verbose flag). |               |           |

</TabItem>
<TabItem value="Process count" label="Process count">

| Macro              | Description                                                                  | Default value | Mandatory |
|:-------------------|:-----------------------------------------------------------------------------|:--------------|:---------:|
| PROCESS            | Filter process name                                                          |               |           |
| PROCESS-ARGS       | Filter process arguments                                                     |               |           |
| WARNING            | Warning threshold of matching processes count                                |               |           |
| CRITICAL           | Critical threshold of matching processes count                               | 1:            |           |
| WARNING-MEM-TOTAL  | Warning threshold of total memory used by all processes matched              |               |           |
| CRITICAL-MEM-TOTAL | Critical threshold of total memory used by all processes matched             |               |           |
| WARNING-MEM-EACH   | Warning threshold of memory used by each process matched                     |               |           |
| CRITICAL-MEM-EACH  | Critical threshold of memory used by each process matched                    |               |           |
| WARNING-MEM-AVG    | Warning threshold of average memory used by all processes matched            |               |           |
| CRITICAL-MEM-AVG   | Critical threshold of average memory used by all processes matched           |               |           |
| WARNING-CPU-TOTAL  | Warning threshold of CPU used by all processes matched                       |               |           |
| CRITICAL-CPU-TOTAL | Critical threshold of CPU used by all processes matched                      |               |           |
| EXTRA-OPTS         | Any extra option you may want to add to the command (E.g. a --verbose flag). |               |           |

</TabItem>
<TabItem value="Service" label="Service">

| Macro       | Description                                                                  | Default value | Mandatory |
|:------------|:-----------------------------------------------------------------------------|:--------------|:---------:|
| SERVICENAME | Filter for Service Name                                                      |               |           |
| CRITICAL    | Critical threshold for matching running services                             | 1:            |           |
| EXTRA-OPTS  | Any extra option you may want to add to the command (E.g. a --verbose flag). |               |           |

</TabItem>
<TabItem value="Swap usage" label="Swap usage">

| Macro      | Description                                                                  | Default value | Mandatory |
|:-----------|:-----------------------------------------------------------------------------|:--------------|:---------:|
| WARNING    | Warning threshold in percent                                                 | 80            |           |
| CRITICAL   | Critical threshold in percent                                                | 90            |           |
| EXTRA-OPTS | Any extra option you may want to add to the command (E.g. a --verbose flag). |               |           |

</TabItem>
<TabItem value="Interfaces" label="Interfaces">

| Macro                | Description                                                                                                                           | Default value | Mandatory |
|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------|:--------------|:---------:|
| INTERFACE            | Set the interface name (empty means 'check all interfaces')                                                                           |               |           |
| OID-FILTER           | Choose OID used to display interface (default: ifName) (values: ifDesc, ifAlias, ifName, IpAddr)                                      | ifDesc        |           |
| OID-DISPLAY          | Choose OID used to filter interface (default: ifName) (values: ifDesc, ifAlias, ifName, IpAddr)                                       | ifDesc        |           |
| SPEED                | Set interface speed for incoming/outgoing traffic (in Mb)                                                                             |               |           |
| SPEED-IN             | Set interface speed for incoming traffic (in Mb)                                                                                      |               |           |
| SPEED-OUT            | Set interface speed for outgoing traffic (in Mb)                                                                                      |               |           |
| MAP-SPEED-DSL        | Get interface speed configuration for interface type 'adsl' and 'vdsl2' Syntax: --map-speed-dsl=interface-src-name,interface-dsl-name |               |           |
| WARNING-DISCARD-IN   | Threshold warning number Packets In Discard                                                                                           | 0             |           |
| WARNING-DISCARD-OUT  | Threshold warning number Packets out Discard                                                                                          | 0             |           |
| WARNING-ERROR-IN     | Threshold warning number Packets In Error                                                                                             | 0             |           |
| WARNING-ERROR-OUT    | Threshold warning number Packets out Error                                                                                            | 0             |           |
| WARNING-TRAFFIC-IN   | Threshold warning traffic in                                                                                                          | 80            |           |
| WARNING-TRAFFIC-OUT  | Threshold warning traffic out                                                                                                         | 80            |           |
| CRITICAL-DISCARD-IN  | Threshold critical number Packets In Discard                                                                                          | 0             |           |
| CRITICAL-DISCARD-OUT | Threshold critical number Packets out Discard                                                                                         | 0             |           |
| CRITICAL-ERROR-IN    | Threshold critical number Packets In Error                                                                                            | 0             |           |
| CRITICAL-ERROR-OUT   | Threshold critical number Packets out Error                                                                                           | 0             |           |
| CRITICAL-TRAFFIC-IN  | Threshold critical traffic in                                                                                                         | 80            |           |
| CRITICAL-TRAFFIC-OUT | Threshold critical traffic out                                                                                                        | 80            |           |
| EXTRA-OPTS           | Any extra option you may want to add to the command (E.g. a --verbose flag).                                                          |               |           |

</TabItem>
<TabItem value="Uptime" label="Uptime">

| Macro           | Description                                                                                                                                            | Default value | Mandatory |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|:---------:|
| WARNING-UPTIME  | Warning threshold in seconds                                                                                                                           | 1800:         |           |
| CRITICAL-UPTIME | Critical threshold in seconds                                                                                                                          | 900:          |           |
| REBOOT-WINDOW   | To be used with check-overload option. Time in milliseconds (Default: 5000) You increase the chance of not missing a reboot if you decrease that value | 5000          |           |
| EXTRA-OPTS      | Any extra option you may want to add to the command (E.g. a --verbose flag).                                                                           |               |           |

</TabItem>
</Tabs>

3. [Deploy the configuration](/docs/monitoring/monitoring-servers/deploying-a-configuration). The service appears in the
   list of services, and on page **Resources Status**. The command that is sent by the connector is displayed in the
   details panel of the service: it shows the values of the macros.
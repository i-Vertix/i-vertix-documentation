---
title: "Release Notes"
hide_table_of_contents: true
---

On this page, you can find the release notes of all published *Plugin Store* versions, including new plugin packs, enhancements and fixes, sorted from newest to oldest.

Each version is labeled as `<plugin version> - <configuration version>`, as shown in the *Version Overview* of the *Plugin Store*. For the update and upgrade procedure, see [Updating/Upgrading the Plugin Store](/monitoring/monitoring-resources/plugin-packs#updatingupgrading-the-plugin-store).

<details open>
<summary><h3 id="20261000-20261030-dev">20261000 - 20261030-dev</h3></summary>

#### News

i-Vertix *Common Cloud Discovery*:

* **Azure**: Azure PostgreSQL

</details>

<details>
<summary><h3 id="20261000-20261029-2">20261000 - 20261029-2</h3></summary>

#### Fixes

* Network Path - MTR: fixed HTPL default values

#### i-Vertix agent

* download [i-Vertix Agent x64 25.0 - 20261000](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/mon/iVertix-NSClient-0.25.0-20261000-x64.exe)
* download [i-Vertix Agent x86 25.0 - 20261000](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/mon/iVertix-NSClient-0.25.0-20261000-Win32.exe)

</details>

<details>
<summary><h3 id="20261000-20261029">20261000 - 20261029</h3></summary>

#### News

* Network Path - MTR
* Veeam VBR (Rest API)

#### Enhancements

* F5OS SNMP - Added disks mode.
* Veeam i-Vertix Agent - Improved job execution performance when filtering by specific jobs in job-status mode
* Veeam WSMAN - Improved job execution performance when filtering by specific jobs in job-status mode
* Veeam Backup: renamend Plugin Packs and Host Templates to Veeam-VBR

#### Fixes

* Azure SQL Database - Fixed health mode that was leading to build invalid Azure Resource ID and an host permanently DOWN / ResourceNotFound, by adding --server option
* Docker Rest API - Fixed the desired replicas count for services: it was always reported as 0 and now matches the number of tasks Docker expects to run
* Oracle Database - Fixed rman mode unusable with the option --sqlmode set to sqlpluscmd

#### i-Vertix agent

* download [i-Vertix Agent x64 25.0 - 20261000](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/mon/iVertix-NSClient-0.25.0-20261000-x64.exe)
* download [i-Vertix Agent x86 25.0 - 20261000](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/mon/iVertix-NSClient-0.25.0-20261000-Win32.exe)

</details>

<details>
<summary><h3 id="20260900-2-20261016">20260900-2 - 20261016</h3></summary>

#### News

- Openshift

- Signl4 notification

#### i-Vertix agent

* download [i-Vertix Agent x64 25.0 - 20260900](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/mon/iVertix-NSClient-0.25.0-20260900-x64.exe)

* download [i-Vertix Agent x86 25.0 - 20260900](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/mon/iVertix-NSClient-0.25.0-20260900-Win32.exe)

</details>

<details>
<summary><h3 id="20260900-20261012">20260900 - 20261012</h3></summary>

#### News

* Barracuda FW: add new mode bgp-status (Ticket #5058)
* Kubernetes: add new mode for pod-usage
* Kubernetes: add new service discovery for pod-usage by pod name
* Kubernetes: add new service discovery for pod-usage by namespace
* Securepoint UTM Firewall

#### Enhancements

* Qnap SNMP - Enhanced the error message dipslayed when OIDs return undef in hardware mode.

#### Fixes

* Cloud discovery: fixed template rule for Azure: Application Gateways
* Docker: fixed service discovery templates for name
* HP Ilo Rest API - Removed perl warnings displayed when running the command in some modes.
* Windows i-Vertix Agent: Fixed qwinsta parsing fails with specific languages in **sessions** mode.

#### i-Vertix agent

* download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.20.0-20260800-x64.exe)
* download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.20.0-20260800-Win32.exe)

</details>

<details>
<summary><h3 id="20260800-new-discovery-20261005">20260800-new-discovery - 20261005</h3></summary>

#### Enhancements

* Docker SSH: add service discovery with name filter
* Velocloud renamed (not more VMware)

#### Fixes

* DataDomain cleaning: fixed timezone, there is no a service macro to setup the correct TZ (default: Europe/Rome)

#### i-Vertix agent

* download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.20.0-20260800-x64.exe)
* download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.20.0-20260800-Win32.exe)

</details>

<details>
<summary><h3 id="20260800-new-discovery-20260911">20260800-new-discovery - 20260911</h3></summary>

#### News

The i-Vertix Common Cloud Discovery covers different technologies across different vendors. The discovery process for each technology is based on the same principles, but the configuration parameters and the discovered devices may vary depending on the technology.

Currently, following technologies are covered by the i-Vertix *Common Cloud Discovery*:

* **AWS**: EC2, EBS, S3, RDS, Lambda, ELB, ElastiCache, API Gateway, SQS
* **Azure**: App Gateway, Load Balancer, NetApp Pool, Public IP, SQL Database, SQL Server, Storage Accounts, Virtual Hub, Virtual Machine, Virtual Network
* **Cisco**: Webex
* **VMware VeloCloud**
* **ExtremeCloud IQ**: Building, Device, Floor, Sites
* **Proxmox VE**

#### Enhancements

* ExtremeCloude IQ: introduce macro API (default: api.extremecloudiq.com)

#### Fixes

* QNAP update status: fixed support for QTS Hero
* Waystream-Switch CPU detailed: fixed wrong percent values

#### i-Vertix agent

* download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.20.0-20260800-x64.exe)
* download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.20.0-20260800-Win32.exe)

</details>

<details>
<summary><h3 id="20260800-20260911">20260800 - 20260911</h3></summary>

#### Enhancements

* Quantum DXI SSH: changed SSH backend to libssh (#4891)

#### Fixes

* i-Vertix agent pagefile: resolves wrong status handling (#5032)

#### i-Vertix agent

* download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.20.0-20260800-x64.exe)
* download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.20.0-20260800-Win32.exe)

</details>

<details>
<summary><h3 id="20260800-20260827">20260800 - 20260827</h3></summary>

#### News

- AWS RDS Clusters: new Host-Template
- Docker rest API - Enhanced services monitoring & added discovery for Docker Swarm
- Moxa: add support for models EDS-G512E-8-POE and IKS-G6524A
- Stormshield FW: new mode auto-update
- Stormshield FW: new mode ha-cluster
- Stormshield FW: new mode licenses
- Stormshield FW: new mode interface details
- Stormshield FW: new discovery mode interface details
- Stormshield FW: new mode router (SDWAN/VPN routes)

#### Enhancements

- AWS RDS: removed STPL volumes from HTPL
- QNAP update status: add support for QTS Hero 6.x (#4963)
- Stormshield FW connections: add thresholds for minor/major alarms
- Stormshield FW memory-detailed: add thresholds for user/socket
- Stormshield FW hardware: enhancements

#### Fixes

- Cisco DNA Center Rest API: fixed percentage metrics in network-devices mode.
- Cisco Meraki Rest API: fixed typo in api custom.
- HP OneView Rest API: added API pagination.
- IBM AS400 Connector: fixed AS400 daemon CVEs related to Log4j and Undertow.
- Microsoft SQL Server: fixed empty output for mssql database-size mode.
- PostgreSQL - Fixed an issue where internal PostgreSQL lock types (virtualxid, transactionid) incorrectly counted as exclusive locks.
- Veeam i-Vertix Agent: fixed job-type and session values in job-status mode.
- Veeam WinRM: fixed job-type and session values in job-status mode.

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.16.4-20260800-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.16.4-20260800-Win32.exe)

</details>

<details>
<summary><h3 id="20260700-hotfix-20260818-20260821">20260700-hotfix-20260818 - 20260821</h3></summary>

#### News

- Moxa: add support for models eds508a, edsg508e, edsp510a8poe, icsg7826a, icsg7850a, edsg512e
- Sonicwall FW NeDi discovery rule

#### Enhancements

- Docker SSH: removed services from HTPL
- EMC DataDomain: add option `--snmp-autoreduce` to Host Template
- EMC DataDomain alerts: add option `--verbose` to Service Template to show alarm description
- Moxa switches: removed interface stpl from htpl

#### Fixes

- Cisco WLC ap status: fixed error with caching
- Moxa cpu: fixed wrong threshold options in command
- Moxa memory: fixed wrong threshold options in command

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.16.1-20260700-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.16.1-20260700-Win32.exe)

</details>

<details>
<summary><h3 id="20260700-20260818-2">20260700 - 20260818-2</h3></summary>

#### Enhancements

- PaloAlto API system: changed threshold for CRITICAL-CERTIFICATE-STATUS to `%{cert_status} !~ /Valid|None/i` to avoid errors when no certificate is installed

#### Fixes

- PaloAlto API: fixed wrong HTTP Backend parameter on HTPL from "lwq" -> "lwp"
- PaloAlto API certificates: fixed wrong STPL name from "HA status" -> "Certificates"
- PaloAlto API: certificates removed from HTPL PaloAlto-Firewall-API-basic (it works only with Panorama)
- PaloAlto API: health removed from HTPL PaloAlto-Firewall-API-basic (it works only with Panorama)

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.16.1-20260700-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.16.1-20260700-Win32.exe)

</details>

<details>
<summary><h3 id="20260700-20260818">20260700 - 20260818</h3></summary>

#### News

- AWS SES - Simple Email Service
- AWS SNS - Simple Notification Service
- F5OS
- Juniper MX Series
- Palo Alto API: new mode to monitor certificates
- Palo Alto API: new mode to monitor health
- Palo Alto API: new mode to monitor sdwan modes
- Palo Alto API: allows now to monitor FW also through Panorama
- Waystream: add memory mode

#### Enhancements

- 3CX Rest API - Added support for versions 20 and above and added license mode
- Cisco Meraki Rest API - Added MRxx devices handling
- Cisco WLC ap-status: add caching
- Mobotix Camera SNMP - Enhanced system mode with SD card availability checks
- Oracle Database - Added RMAN Catalog support
- PaloAlto API: enhanced system mode
- Veeam i-Vertix Agent - Enhanced message displayed when using wrong powershell version with veeam 13
- Veeam WSMAN - Enhanced message displayed when using wrong powershell version with veeam 13

#### Fixes

- Cisco Meraki Rest API - Fixed the devices.total.online.count counter
- Commvault Commserve Rest API - Fixed a token expiration issue
- Microsoft SQL Server - Fixed a bad query issue revealed by a previous fix
- Proxmox VE - Fixed authentication failures and caching issues

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.16.1-20260700-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.16.1-20260700-Win32.exe)

</details>

<details>
<summary><h3 id="20260600-20260811">20260600 - 20260811</h3></summary>

#### News

- Atto Fibrebridge
- Masterclock NTP100 GPS
- Quantum DXI series

#### Enhancements

- Audiocodes-SBC: removed network-audiocodes-snmp-trunk-status and network-audiocodes-snmp-interfaces from Hosttemplate
- Extreme Networks Fabric Engine: add NeDi discovery rule

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.14.1-20260600-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.14.1-20260600-Win32.exe)

</details>

<details>
<summary><h3 id="20260600-20260709-hotfix">20260600 - 20260709-hotfix</h3></summary>

#### Fixes

- PaloAlto SNMP sensors: removed wrong option --absent-problem

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.14.1-20260600-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.14.1-20260600-Win32.exe)

</details>

<details>
<summary><h3 id="20260600-20260708">20260600 - 20260708</h3></summary>

#### News

- Easy PDU
- i-Vertix Standard SNMP
- Kubernetes API - new Resource quota status
- Sentry PDU

#### Enhancements

- Kubernetes daemonset-status: add exclude options
- Kubernetes deploayment-status: add exclude options, add filtering options for labels
- MS SQL Server failed jobs - new filtering and threshold options
- PaloAlto FW SNMP: add new mode `sensors`
- Stormagic mirros: add thresholds for "resync-progress"
- Windows Server iVertix agent: add version check

#### Fixes

- Commvault Commserve Rest API - Fixed issues related to tokens in commands and removed undefined ARRAY value if no jobs have been sent in jobs mode
- Fritz!Box UPnP - Fixed system mode status thresholds
- HashiCorp Vault Rest API - Fixed handling of --insecure option
- IBM AS400 Connector - Fixed daemon CVEs related to Log4j
- Phoenixtec UPS SNMP - Removed thresholds for non-existent counters in --help section
- Powerware UPS SNMP - Fixed the output when the plugin does not detect the absence of an input line in input-lines mode
- Windows Agent: fixed agent settings when using PS scripts

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.14.1-20260600-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.14.1-20260600-Win32.exe)

#### Upgrade steps

Please refer to the following [documentation](https://i-vertix.guide/monitoring/monitoring-resources/plugin-packs#updatingupgrading-the-plugin-store) for the correct upgrade procedure

</details>

<details>
<summary><h3 id="20260500-20260613">20260500 - 20260613</h3></summary>

#### Enhancements

- Stormagic: add --snmp-autoreduce on Host Template

#### Fixes

- APC UPS input lines: remove phase thresholds
- PaloAlto Rest API basic Environment: remove --absent-problem parameter
- PaloAlto Rest API basic licenses: change EXPIRATIONS-DAYS thresholds to match "days left"
- PaloAlto Rest API basic HA status: CRITICAL-HA2-LINK-STATUS uses status of ha1 (ha1_status)
- VMware VCSA: fixed wrong thresholds on mode `--update`

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.12.6-20260500-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.12.6-20260500-Win32.exe)

</details>

<details>
<summary><h3 id="20260500-20260529">20260500 - 20260529</h3></summary>

#### News

- APC ATS: add new mode `--output-banks` to monitor the APC Output Bank
- Azure NetApp Pools
- Azure Virtual Hub
- Azure Virtual Public IP
- Azure Virtual Network
- Cambium cnMatrix
- Dell OpenManage
- StorMagic Virtual SAN
- Unifi UAP: add NeDi discovery rule for U6/7-Pro

#### Enhancements

- APC UPS input lines: add options to include/exclude for Input Type/Phase
- Brocade FC Switch: add options to exclude SFP ports by instance or interface
- Brocade FC Switch: add SFP port service discovery on NeDi discovery rule
- Cisco VPC mode: enhanced various status options with defaults
- Cisco VPC mode: added MAC address normalization in vpc mode
- Extreme Networks MLXe Switch: add options to exclude SFP ports by portnumber or interface
- Extreme Networks MLXe Switch: add NeDi discovery rule
- Huawei Standard SNMP: added a way to handle missing fans in hardware mode
- Interface monitoring: Improved cache reload performance for interfaces. The impact on the device is reduced because the cache is refreshed only once due to the introduction of a lock mechanism.
- MessPC EthernetBox: add options to include/exclude sensors by sensor types
- Wastream Switch: add options to exclude SFP ports by portnumber or interface
- Wastream Switch: add options include/exclude for SFP ports by serial number
- Windows WSMAN files-count: add recursive option (default no)

#### Fixes

- Amazon CloudWatch Logs: fixed issues with perl paws custom mode
- Docker Rest API: fixed memory usage calculation in container-usage mode
- F5 BigIP: fixed unknown status returned if no trunk was configured in trunks mode
- Fritzbox traffic: fixed wrong command option
- Fritzbox system: fixed wrong command option
- Proxmox VE: allow password with special chars
- Veeam i-Vertix Agent: fixed warnings about uninitialized values in job-status mode
- Windows WinRM: fixed an issue on discovery and monitoring the Windows Taskscheduler
- VMware vSphere8 VCSA: fixed wrong default threshold for --warning-status and --critical-status

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.12.6-20260500-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.12.6-20260500-Win32.exe)

</details>

<details>
<summary><h3 id="20260400-20260520">20260400 - 20260520</h3></summary>

#### News

- Hitachi HNAS
- Siemens Ruggedcom network devices

#### Enhancements

- Windows WSMAN files-count: add macro $_SERVICEEXTRA-OPTS$ on command

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.29-20260400-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.29-20260400-Win32.exe)

</details>

<details>
<summary><h3 id="20260400-20260426-hotfix">20260400 - 20260426-hotfix</h3></summary>

#### Enhancements

- MS SQL dead locks: new default thresholds (MS recommendet)
- MS SQL locks wait: new default thresholds (MS recommendet)

#### Fixes

- MS SQL dead locks: fixed wrong command option
- MS SQL locks wait: fixed wrong command option

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.29-20260400-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.29-20260400-Win32.exe)

</details>

<details>
<summary><h3 id="20260400-20260424">20260400 - 20260424</h3></summary>

#### News

- Azure SQL DB serverless
- Azure SQL Server
- Forti Authenticator Rest API - monitor Tokens
- PaloAlto FW using Rest API

#### Enhancements

- AIX SNMP - Handled unanticipated hrSWRunStatus in processcount mode
- Amazon API Gateway - Added possibility to change the instance dimension
- Azure-SQL-DB: removed service template app-resources (moved to new derivative template Azure-SQL-DB-serverless)
- Brocade sfp-port-status: add filter for interface name
- Dell Me4 Rest API - Enhanced compatibility with Dell SAN for interfaces mode
- Extreme MLX sfp-port-status: add filter for interface name
- Fortigate SDWAN command/STPL: add exclude filters for id, name, vdom
- Fortigate SDWAN command/STPL: add include/exclude filters for interface
- Fortigate VPN command/STPL: add include/exclude filters for VPN phase 1 & 2
- Fortigate VPN command/STPL: new default values on --warning-status/critical-status based on new `%{vpn_state}`: it is "up" when all Phase 2 tunnels are up, "down" when all Phase 2 tunnels are down, and "degraded" when at least one Phase 2 tunnel is up and at least one is down. `%{phase2_state}` is the status of specific Phase 2 tunnel either "up" or "down"
- Huawei GPON commands/STPL: add include/exclude filters
- MessPC Ethernetbox sensors: add skip-not-valid option for sensors with valid=0
- Rubrik Rest API - Improved cache naming and job mode filtering
- Waystream sfp-port-status: add filter for interface name

#### Discovery

- Better WinRM template detection on network (NMAP-SNMP) discovery

#### Fixes

- Amazon CloudWatch - Fixed get-alarms mode to handle multiple alarms
- Exagrid SNMP - Fixed landing_used calculation to prevent negative values in server-usage mode
- HP Ilo XMLAPI - Fixed ILO3 incorrect temperature thresholds in hardware mode
- IBM AS400 - Handled exceptions in refresh
- NetApp Ontap Rest API - Fixed latency values in cluster mode
- Veeam 13: fixed i-Vertix agent commands
- Extended Azure-SQLdatabase timeframe to 900 seconds
- Phoenixtec UPS Outputlines: remove not existing options current and power
- Phoenixtec UPS Battery Status: fix wrong default warning and critical threshold for "CHARGE-REMAINING"

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.29-20260400-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.29-20260400-Win32.exe)

</details>

<details>
<summary><h3 id="20260300-20260420">20260300 - 20260420</h3></summary>

#### News

- JVM Actuator
- Westermo Lynx Series
- NeDi Cisco AP ping - CW series
- NeDi Westermo Lynx Series

#### Enhancements

- Docker SSH: list containers still us container ID for filter, but now use container name instead container ID for the service name

#### Fixes

- Veeam 13 i-Vertix Agent: fixed wrong discovery commands
- Veeam 13 i-Vertix Agent: add Veeam 13 version as default version on Host template
- Citrix Citrix-XenDesktop: add missing host macro NSCLIENT-USERNAME for new agent authentication
- MessPC sensors: replace wrong gix values with service macros

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.26-20260300-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.26-20260300-Win32.exe)

</details>

<details>
<summary><h3 id="20260300-20260401">20260300 - 20260401</h3></summary>

#### Fixes

- i-Vertix Agent: remove legacy authentication, force new authentication method

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.26-20260300-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.26-20260300-Win32.exe)

</details>

<details>
<summary><h3 id="20260300-20260331-2">20260300 - 20260331-2</h3></summary>

#### News

- Brocade BR: add NeDi discovery rule
- CyberPower UPS: add NeDi discovery rule
- Waystream: add NeDi discovery rule

#### Fixes

- Mikrotik interface service discovery template: fixed regex to exclude lo interface
- Postgresql backend: fixed wrong command options

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.26-20260300-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.26-20260300-Win32.exe)

</details>

<details>
<summary><h3 id="20260300-20260331">20260300 - 20260331</h3></summary>

#### News

- Brocade Foundry switches
- Brocade switches: add modes to discover and monitor sfp ports
- Cisco Webex
- Extreme MLX switches
- Forcepoint SDWAN: add discovery & STPL for storages
- MessPC Ethernetbox
- Ubiquiti Unifi UAP
- Veeam Backup WinRM: add support for Veeam 13
- Veeam Backup Agent: add support for Veeam 13 (new Host template)
- Windows WSMAN: add STPL to monitor Windows Certificates

:::info

for Veeam 13 you need to install i-Vertix Agent 20260300 or higher

:::

#### Enhancements

- Commvault Backup: Added client name to the output prefix of the jobs mode
- Commvault Backup: new STPL token to refresh Rest API token
- HAProxy SNMP - Allow compatibility with version 17 OIDs
- Jboss memory-detailed: add standard thresholds
- Linux SSH: add new STPL to monitor processes including open files
- Postgresql backend: added support for applying thresholds to the total number of connections, not just per database
- **Postgresql: --exclude is now --exclude-database, added options --include-database**
- Weblogic memory-detailed: add standard thresholds
- Windows WinRM: add new HTPL for Kerberos authentication

#### Fixes

- Fortinet Fortigate SNMP - Fixed an error in the bandwidth calculation for the SDWan service
- Linux SSH - Fixed a No peers detected error with --ntp-mode=ntpq
- Microsoft Exchange i-Vertix Agent - Fixed edge cases size calculation in database mode
- Veeam WSMAN - Added a specific command handler dedicated to PowerShell scripts to avoid JSON error messages occurring in some cases
- Windows WSMAN - Added a specific command handler dedicated to PowerShell scripts to avoid JSON error messages occurring in some cases, such as updates and pending-reboot modes
- Windows WSMAN - The temporary files are now deleted when the execution ends

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.26-20260300-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.11.26-20260300-Win32.exe)

</details>

<details>
<summary><h3 id="20260100-20260327">20260100 - 20260327</h3></summary>

#### News

- Aruba Instant: add NeDi rule

#### Enhancements

- APC ATS input lines: changed threshold for voltage to 210:245 and 200:255
- Forcepoint SDWAN FW: disk usage: add default filter for disk ^/dev/sd
- MySQL Long queries: add default command filter ^(?!(sleep)$)
- Riello UPS input lines: changed threshold for voltage to 210:245 and 200:255

#### Fixes

- Forcepoint SDWAN FW: fixed command network-forcepoint-sdwan-snmp-connections

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-Win32.exe)

</details>

<details>
<summary><h3 id="20260100-20260311">20260100 - 20260311</h3></summary>

#### News

- Zebra RFC

#### Fixes

- Netapp Ontap RestAPI hardware: removed --warning/--critical from command
- HP Virtual Connect hardware: removed --warning/--critical from command
- Cisco WLC hardware: removed --warning/--critical from command
- Cisco UCS Server equipment: removed --warning/--critical from command
- UPS Alpha alarms: removed --warning/--critical from command
- Adva FSP150 hardware: removed --warning/--critical from command
- Sophos Cyberoam services: removed --warning/--critical from command
- Oracle Solaris OS SSH v120 status: removed --warning/--critical from command
- Oracle-ZS Rest API hardware: removed --warning/--critical from command
- Oracle ZS SNMP hardware: removed --warning/--critical from command
- MS SQL locks wait: removed thresholds temporaly, check is not reporting correct metrics
- Database DB2 logs: resolve "Unknown option: critica-log-usage-prct"

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-Win32.exe)

</details>

<details>
<summary><h3 id="20260100-20260305">20260100 - 20260305</h3></summary>

#### News

- Arista BGP: new command and STPL
- Mikrotik LTE status: new command and STPL
- VMware vSphere 8 vCSA

#### Enhancements

- Cisco IPSLA: add completion time
- Commvault Jobs: added client name to the output prefix of the jobs mode
- Dell OME: renamed HTPL to Dell-OME-MX7000
- MSSQL Server: added an option to the connected-users mode to filter by database name
- MSSQL Server: added service discovery for connected users
- MSSQL Server: remove service discovery template database-mssql-locks-wait (Breaking change)
- Waystream list sfp connectors: add option --add-interface-name
- Waystream list sfp connectors: add filter option --filter-connector

#### Fixes

- DLink DGS 3100: Fixed “uninitialized values” warnings on interfaces mode
- Dlink Network: Fixed “uninitialized values” warnings on interfaces mode
- Fortigate FW: Fixed “uninitialized values” warnings on interfaces mode
- Fortigate FW switches: fixed command
- HPE MSA: fixed error on hardware mode
- HP Procurve: Fixed “uninitialized values” warnings on interfaces mode
- MSSQL: forced the version of a dependency, to fix a segmentation fault issue
- Nutanix disks: added support of Nutanix 6.10 (fixes ‘No disk found’ error in disk-usage_ service template)
- PaloAlto FW: Fixed “uninitialized values” warnings on interfaces mode

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-Win32.exe)

</details>

<details>
<summary><h3 id="20251100-20260301">20251100 - 20260301</h3></summary>

#### News

- Mellanox: add NeDi rule
- FortiManager: add NeDi rule
- Synology NAS: add NeDi rule

#### Enhancements

- i-Vertix centengine STPL: memory threshold change: warning 100MB->200MB, critical 200MB->400MB
- UPS Cyberpower SNMP battery status: extend the battery-status mode with battery replace indicator, battery life time, last replace date, time on battery
- Windows SNMP: remove disk-c from HTPL
- Windows WinRM: remove autostart services from HTPL

#### Fixes

- Mellanox interface service template fixed
- Windows NeDi discovery rule: remove Microsoft as vendor from condition
- OS Windows WSMAN task scheduler: add missing single quotes for default warning status
- Audiocodes Hardware: removed unknown critical and warning option
- Dell Powerstore: removed unknown critical and warning option

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-Win32.exe)

</details>

<details>
<summary><h3 id="20251100-20260130">20251100 - 20260130</h3></summary>

#### News

- Juniper SRX: add NeDi rule

#### Enhancements

- Juniper EX: exclude SRX from rule

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-Win32.exe)

</details>

<details>
<summary><h3 id="20251100-20260129">20251100 - 20260129</h3></summary>

#### Enhancements

- HPE ILO5 host discovery rule

</details>

<details>
<summary><h3 id="20251100-20260120">20251100 - 20260120</h3></summary>

#### News

- Prometheus nginx ingress controller
- Prometheus Rest API: custom query and target status
- SSL certificates: add new STPL apps-protocols-x509-certificate-https-internal to monitor certificates without chain or CA verification

#### Enhancements

- Cisco DNAC renamed into Cisco Catalyst Center

#### Fixes

- Aruba hardware: removed unknown option --absent-problem
- HP ILO restapi hardware: removed unknown option --absent-problem (#4366)
- ATS APC device status: removed unknown option --absent-problem
- PDU raritan external sensors: removed unknown option --absent-problem
- PDU raritan inlet sensors: removed unknown option --absent-problem
- PDU raritan ocprot sensors: removed unknown option --absent-problem
- APC hardware sensors: removed unknown option --absent-problem
- HWGSTE sensors: removed unknown option --absent-problem
- Jacarta sensors: removed unknown option --absent-problem
- APC Netbotz sensors: removed unknown option --absent-problem
- Oracle Sun sensors: removed unknown option --absent-problem
- Alpha UPS alarams: removed unknown option --absent-problem
- ADVA FSP 150 hardware: removed unknown option --absent-problem
- Aruba CX Series hardware: removed unknown option --absent-problem
- Cisco Firepower FXOS hardware: removed unknown option --absent-problem
- Sophos XG / Cyberoam services: removed unknown option --absent-problem
- Fortinet ADC (Application Delivery Controller) hardware: removed unknown option --absent-problem
- Fortinet FortiMail hardware: removed unknown option --absent-problem
- HPE Virtual Connect hardware: removed unknown option --absent-problem
- Infoblox services: removed unknown option --absent-problem
- Nortel network devices hardware: removed unknown option --absent-problem
- Palo Alto Firewall enviroment: removed unknown option --absent-problem
- Stormshield Firewall (Rest API) hardware: removed unknown option --absent-problem
- Stormshield Firewall (SNMP) hardware: removed unknown option --absent-problem
- Oracle Solaris SSH v120 status: removed unknown option --absent-problem
- Dell EquaLogic hardware: removed unknown option --absent-problem
- Dell ME4 hardware: removed unknown option --absent-problem
- Dell ML6000 hardware: removed unknown option --absent-problem
- Dell EMC Isilon hardware: removed unknown option --absent-problem
- HPE Storeonce 4 (API) hardware storage: removed unknown option --absent-problem
- Netapp Ontap Rest API hardware: removed unknown option --absent-problem
- Oracle ZS (Rest API) hardware: removed unknown option --absent-problem
- Oracle ZS (SNMP) hardware: removed unknown option --absent-problem
- Quantum Scalar hardware: removed unknown option --absent-problem
- Waystream discovery commands: fixed plugin path

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-x64.exe)
- download [i-Vertix Agent x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-Win32.exe)

</details>

<details>
<summary><h3 id="20251100-20260114">20251100 - 20260114</h3></summary>

#### News

- Podman containers
- Waystream network devices

#### Enhancements

- Active Directory WSMAN - Added DE language support
- Aruba standard license: add support for subscription licenses
- Elasticsearch - Added new query mode
- Google Stackdriver - Enhanced compatibility with DISTRIBUTION type values in getmetrics mode
- Office 365 Management - Added filter-classification option to service-status mode
- pfSense SNMP - Added new modes: cpu, cpu-detailed, load, memory, swap and uptime
- Redis Database - Added authentication with username for custommode perlmod
- Splunk API - Extended query mode: numeric-value, string-value
- Stormshield FW: add hardware mode
- Veeam i-Vertix Agent - Added Veeam 12 compatibility by using the correct cmdlets in vsb-jobs mode.
- Veeam WSMAN - Added Veeam 12 compatibility by using the correct cmdlets in vsb-jobs mode.
- Speedtest - Internet bandwidth - added service macro for EXTRA-OPTS

#### Special SSH Enhancements

- Linux-Server-SSH - Added $_HOSTSSHCLI-OPTION2$ with default "-o=LogLevel=ERROR" to hide the SSH banner to avoid parsing error
- IBM-Storwize - Added $_HOSTSSHCLI-OPTION2$ with default "-o=LogLevel=ERROR" to hide the SSH banner to avoid parsing error
- HPE-Storeonce - Added $_HOSTSSHCLI-OPTION2$ with default "-o=LogLevel=ERROR" to hide the SSH banner to avoid parsing error
- IBM-AIX-ssh - Added $_HOSTSSHCLI-OPTION2$ with default "-o=LogLevel=ERROR" to hide the SSH banner to avoid parsing error
- Oracle-Solaris-SSH - Added $_HOSTSSHCLI-OPTION2$ with default "-o=LogLevel=ERROR" to hide the SSH banner to avoid parsing error
- Pacemaker-HA - Added $_HOSTSSHCLI-OPTION2$ with default "-o=LogLevel=ERROR" to hide the SSH banner to avoid parsing error
- Redis-DB-cli - Added $_HOSTSSHCLI-OPTION2$ with default "-o=LogLevel=ERROR" to hide the SSH banner to avoid parsing error
- Dell-EMC-RecoveryPoint - Added $_HOSTSSHCLI-OPTION2$ with default "-o=LogLevel=ERROR" to hide the SSH banner to avoid parsing error
- Redis-Sentinel - Added $_HOSTSSHCLI-OPTION2$ with default "-o=LogLevel=ERROR" to hide the SSH banner to avoid parsing error

#### Fixes

- Commvault Commserve Rest API- Fixed an error with jobs mode occurring when the output was too long
- DB2: CMD database-db2-database-logs fixed
- Dell iDRAC SNMP - Fixed ready status for pdisk.state in hardware mode
- Eclipse Mosquitto MQTT - Fixed format-custom option
- Fortinet Fortigate RestAPI - Take in charge other encodages than UTF8 in returned content
- Fortinet Fortigate Rest API - Fixed an issue with resources in health mode
- Google Stackdriver - Fixed the minimum aggregation calculation
- Huawei Standard SNMP - Fixed missing fan state in short output
- Huawei WLC SNMP - Fixed missing fan state in short output
- IBM Storwize SSH - Fixed an issue occurring while parsing response
- Microsoft SQL Server - Fixed an issue where deadlocks mode returned false positives
- Office 365 Management - Fixed an issue where each new alert for a service overwrote the previous one, making it impossible to have a global vision in service-status
- Windows i-Vertix Agent network rule fixed

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.10.8-20251100-Win32.exe)

</details>

<details>
<summary><h3 id="20250901-20251118">20250901 - 20251118</h3></summary>

#### News

- Avocent 6000: add NeDi rule
- Avocent 8000: add NeDi rule
- Checkpoint FW: add NeDi
- PaloAlto ION: NeDi rules
- PaloAlto ION virtual: add HTPL for virtual appliance
- Watchguard FireboxV HTPL
- Watchguard FireboxV NeDi rule

#### Enhancements

- Netapp Ontap Volume: add thresholds for Snapshot used %
- Netapp Ontap Volume: add thresholds for Virtual used %
- Watchguard swap: if no swap configured default status is now OK

#### Fixes

- Avocent 6000/8000: fixed command for load
- Huawei Storage: fixed controller discovery template

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250901-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250901-Win32.exe)

</details>

<details>
<summary><h3 id="20250901-20251029">20250901 - 20251029</h3></summary>

#### Enhancements

- i-Vertix Agent Windows service monitoring: remove performancedata
- Axentia e-paper display health: set default thresholds for battery status, battery voltage, temperature, tcp/udp quality and uptime

#### Fixes

- Mellanox: fixed wrong command for interfaces
- Watchguard cluster: fix problem that a cluster failure is not detected correctly. Add default value for `--critical-member-status='%{role} !~ /master|backup/i'` (#4097)

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250901-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250901-Win32.exe)

</details>

<details>
<summary><h3 id="20250901-20251014">20250901 - 20251014</h3></summary>

#### News

- Avocent ACS 6000 KVM series
- Avocent ACS 8000 KVM series

#### Fixes

- Windows WinRM: fixed CMD os-windows-wsman-list-taskscheduler

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250901-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250901-Win32.exe)

</details>

<details>
<summary><h3 id="20250901-20251010">20250901 - 20251010</h3></summary>

#### News

- HP Comware: new mode to monitor IRF status
- HP Comware: new HTPL `HP-IRF-stack`
- HP Comware: new NeDi rule for Comware stack device (IRF status)
- Mellanox network devices
- Microsoft Active Directory WinRM: add german language support
- Windows WinRM: new mode files-count
- Windows WinRM: new mode taskscheduler
- Windows WinRM: new discovery mode taskscheduler

#### Enhancements

- AKCP: supports new sensor types (buzzer, security port)
- Docker Rest API - add container health status by calling the /inspector endpoint
- Linux SSH - Added support for timedatectl in ntp mode
- Linux SSH - Added option `--exclude-name` in ntp mode
- Linux SSH - Added option `--exclude-state` in ntp mode
- NetApp Ontap Rest API - add option `--add-virtual` for virtual usage
- NetApp Ontap Rest API - add option `--add-snapshot` for snapshot information
- Proxmox VE Rest API - Added option `--exclude-name` in vm-usage mode
- Proxmox VE Rest API - Added option `--exclude-node-name` in vm-usage mode
- Proxmox VE Rest API - Added option `--include-node-name` in vm-usage mode

#### Fixes

- Docker Rest API - Fixed memory usage calculation in container-usage mode
- Kubernetes w/ Prometheus API - Fixed daemonset-status incorrect key causing skips in daemonset-status mode
- NetApp Ontap Rest API - Fixed total space calculation error and missing snapshot info in volumes mode
- Veeam - Added Veeam Agent compatibility for job monitoring in job-status mode

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250901-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250901-Win32.exe)

</details>

<details>
<summary><h3 id="20250800-20251001">20250800 - 20251001</h3></summary>

#### Enhancements

- Linux SSH storage discovery: exclude UEFI firmware (efivars)
- Linux SSH storage discovery: exclude CD-ROMS (iso9660)
- VMware Cluster status: add warning-status e critical-status

#### Fixes

- AS400: fixed command os-as400-connector-message-queue
- VMware Cluster status: removed password flag for cluster-name macro

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250800-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250800-Win32.exe)

</details>

<details>
<summary><h3 id="20250800-20250915">20250800 - 20250915</h3></summary>

:::warning

Important Notice: This upgrade introduces a breaking change affecting Microsoft Teams Workflow notifications. Before proceeding, please review the following [Knowledge Base article](https://helpdesk.i-vertix.cloud/front/knowbaseitem.form.php?id=127) to ensure a smooth transition.

:::

#### News

- Axentia e-paper (#3704)
- Allied Telesis: add NeDi rule for GS models
- Westermo standard network devices (WeOS Lynx, Redfox, Viper and Wolverine) (#2057)
- Westermo NeDi discovery rule

#### Enhancements

- Apache Server: Reworked requests mode and enhanced slot-states mode
- Aruba CX spanning tree: add default value `'%{op_status} =~ /up/ && %{state} =~ /blocking|broken/'` on critical-status
- AS400 disks: renamed disk filter from `--filter-*` to `--include-*`
- AS400 jobs: renamed filter from `--filter-*` to `--include-*`
- AS400 message-queue: renamed filter from `--filter-*` to `--include-*`
- AS400 message-queue: add option to include/exclude reply status (#2840)
- AS400 message-queue: add option to include/exclude message text
- AS400 subsystems: renamed filter from `--filter-*` to `--include-*`
- Curl commands logging: Display the curl command if --debug option is set
- Forcepoint SDWAN: add service discovery for disks
- HashiCorp Vault Rest API - Enhanced standby-status counter and added code parameters options in health mode
- i-Vertix Agent update: various small bugfixes
- O365 Teams workflow notification: long messages will be displayed (#3727)
- O365 Teams workflow notification: it is not more required to reconfigure the Poller Engine configuration
- UPS APC output lines: new options warning-status and critical-status
- UPS APC supports now Galaxy series (#2497)

#### Fixes

- AIX SNMP - Fixed an issue causing a parsing error
- Aruba CX: fixed spanning tree discovery template
- Aruba CX: fixed spanning tree monitoring template
- EMC Data Domain SNMP - Fixed an issue where default value for timezone option was empty, leading to an unknown status being returned in cleaning mode
- Eclipse Mosquitto MQTT - Fixed a syntax error and an issue with encoding occurring when topic names contained accents
- Huawei HMM - Removed experimental keys on scalar in blade mode components
- Huawei HMM - Fixed `no-component` option
- HP Ilo Rest API - Fixed an issue with some firmware versions to exclude enclosure
- i-Vertix Agent task scheduler: fixed detail-syntax in CMD
- MySQL/MariaDB - Fixed an error occurring when retrieving the server version
- NetApp Santricity Restapi - Fixed cmd component count in hardware mode
- O365 Onedrive discovery: fix service discovery template
- Podman REST API - Fixed API endpoint for container-usage mode
- Printer RFC - Supply usage: fixed wrond standard thresholds
- Viptela: HTPL connected to generic-host

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250800-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.15-20250800-Win32.exe)

</details>

<details>
<summary><h3 id="20250600-20250721">20250600 - 20250721</h3></summary>

#### News

- F5 BigIP: add mode to monitor certificates
- Palo Alto Prisma SASE: new plugin
- Palo Alto ION: new plugin
- Huawei Network Devices:
    - new service templates for GPON ONT traffic
    - new service templates for GPON ONT helath
    - new service templates for GPON ONT ehternet ports
    - service discovery for GPON ONT modules

#### Enhancements

- Cisco IPSLA: add default option --use-new-perfdata
- HPE Alletra volume usage: use "used" instead of "reserved" for free space calculation. "Reserved" is shown in the status output
- HPE Alletra capacity: added performance counter provisioning-virtual-size, provisioning-used, provisioning-allocated, provisioning-free
- Juniper EX: reworked plugin path to be more explicit with the initial release of Juniper M-series with Netconf
- Linux SSH Inodes service discovery: exclude Inodes from type efivarfs (#3775)
- Nmap cli: Enhanced secure execution of commands.
- Sophos XGS HA state: change threshold to raise an critical status also when `%{peer_hastate} =~ /^faulty$/` (#3810)
- Zyxel network device: add models WAX and NX to NeDi

#### Fixes

- Audiocode SBC calls: removed not existing threshold option sbc-calls-notestablished-outbound-failed (#3830)
- HPE Alletra: Fix an issue skipping values filtering on one Volume
- HPE Alletra: Set volume compression state or provisioning type to "NOT_DOCUMENTED" if can't be mapped
- **i-Vertix Agent: fixed issue on error return code. All agents version starting from 0.9.x should be updated**
- O365 onedrive discovery: Fixed service discovery mode for site-usage
- Rubrik: Fixed an issue affecting token renewal

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.8-20250400-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.8-20250400-Win32.exe)

</details>

<details>
<summary><h3 id="20250501-20250622">20250501 - 20250622</h3></summary>

#### News

- Cisco SBS: add stack status mode (CMD, STPL, HTPL)
- Cisco SBS NeDi: add rule for SBS stack
- i-Vertix Agent 0.9.6
- Mikrotik add mode for LTE interfaces
- Mikrotik add LTE interface discovery
- Stormshield Rest API: add new mode for VPN tunnels
- Stormshield Rest API: add new discovery for VPN tunnels

#### Enhancements

- Eclipse MQTT numeric mode: renamed threshold options
- Mikrotik NeDi: add automatic LTE interface service discovery
- QNAP: support for QTS Hero (#3638)
- Socomec UPS battery: add thresholds for ambient temperature
- Socomec UPS battery: add unknown-status, warning-status and critical-status with default values

#### Fixes

- AWS Backup: fixed CMD cloud-aws-backup-job-status
- Eclipse MQTT: fixed error in mqtt.pm

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.6-20250400-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.9.6-20250400-Win32.exe)

</details>

<details>
<summary><h3 id="20250400-20250617">20250400 - 20250617</h3></summary>

#### News

- i-Vertix Agent 0.8.1 (supports TLS 1.3)

#### Enhancements

- Docker SSH: Container discovery use now exact filter
- AWS Backup job status: added timeframe and period options

#### Fixes

- Aruba Clearpass: renamd HTPL (there was a spelling error)
- Azure SQL databases health: removed not supported --server filter from command
- Azure SQL databases deadlocks: renamed warning and critical thresholds parameter for deadlocks in command
- AWS Backup job status: removed not supported --timeout option from command
- Fortigate Rest API - certificates: fixed STPL

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.8.1-20250400-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.8.1-20250400-Win32.exe)

</details>

<details>
<summary><h3 id="20250400-20250512">20250400 - 20250512</h3></summary>

#### News

- MariaDB/MySQL: add new mode for collection (complex custom SQL)
- Microsoft SQL Server: add new mode for collection (complex custom SQL)
- Oracle RDBMS: add new mode for collection (complex custom SQL)

#### Enhancements

- Linux SNMP storage discovery: exclude disks contains "overlay2" from discovery
- O365: subscription discovery: add filter to show only subscriptions with status "enabled"

#### Fixes

- Kubernetes: fixed pod discovery command

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20250400-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20250400-Win32.exe)

</details>

<details>
<summary><h3 id="20250400-20250423">20250400 - 20250423</h3></summary>

#### News

- Exagrid Backup storage
- F5 add new mode to monitor CPU usage
- Fortigate FW: add mode to monitor certificates
- Windows i-Vertix Agent: new mode to check a port of a remote host using i-Vertix Agent

#### Enhancements

- APC UPS SNMP - Enhance replace-lasttime output to be humanly readable in battery-status mode
- F5 trunk: add options to set unknown/warning/critical-status
- F5 trunk: add options to set unknown/warning/critical-interface-status
- Forcepoint packets dropped: renamend options
- Forcepoint packets rejected: renamend options
- MySQL/MariaDB - Enhance uptime date display in uptime mode
- Veeam Backup Enterprise Manager Rest API - Added handling of replication jobs to jobs mode

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20250400-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20250400-Win32.exe)

</details>

<details>
<summary><h3 id="20250300-20250414">20250300 - 20250414</h3></summary>

#### News

- D-Link: add NeDi discovery rule
- QNAP: add NeDi discovery rule
- Windowns SNMP: add NeDi discovery rule

#### Enhancements

- Forcepoint cluster status: removed standby and goingstandby from default critical status
- Fortinet Fortigate snmp VPN: added warning and critical thresholds for IPSEC tunnel count

#### Fixes

- Cisco ASA failover: fixed wrong threshold CRITICAL-ACTIVE-UNITS = 2: (old value 1:)
- Cisco standard load: fixed default STPL threshold
- Huawei spanning tree: fixed wrong filter-port option in command
- Forcepoint cluster status: add status defaults with ''
- AWS ELB network targets health: removed unnecessary quote on param name

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-Win32.exe)

</details>

<details>
<summary><h3 id="20250300-20250330">20250300 - 20250330</h3></summary>

#### News

- Forcepoint SD-WAN Firewall
- Extreme CloudIQ
- Huawei network device: add spanning tree discovery and monitoring
- IBM AS400 SSL HTPL
- Internet Information Server (WinRM)
- Scale Computing
- Sophos XGS - add NeDi discovery rule
- Veeam backup (WinRM)

#### Enhancements

- Fortigate VPN: add options to customize --warning-status and --critical-status
- IBM AS400 Connector - Added capability to use AS400 SSL connection (#3189)
- IBM AS400 commands: add variables `$_HOSTEXTRA-OPTS$ $_SERVICEEXTRA-OPTS$` - use `$_HOSTEXTRA-OPTS$` to setup ssl connection with option `--as400-ssl` (#3189)
- Oracle DB: changed redo log retry ratio thresholds (warning 0->0.5, critical 10->1)
- Pure Storage FlashArray Rest API v2 - Added flagged status attribute in alerts mode
- VMware ESXi standalone: add license check STPL to the HTPL

#### Fixes

- AWS Network Loadbalancer: Plugin Pack was emtpy, no HTPL, STPL and discovery attached
- Azure VPN Gateway - Fixed wrong variable assignment in vpn-gateway-status mode
- Cisco UCS SNMP - Fixed wrong count when memory component is not equipped in equipment mode
- EMC Data Domain SNMP - Added --timezone option for equipment in cleaning mode to avoid misinterpreting the clean time frame
- Generic SNMP - Fixed an unsafe eval for unknown status option in collection mode
- HTTP Server - Fixed an unsafe eval for unknown status option in collection mode
- IBM AS400 Connector - Fixed previous pending error
- MongoDB - Fixed an unsafe eval for unknown status option in collection mode
- MySQL/MariaDB - Fixed an unsafe eval for unknown status option in collection mode
- NetApp Ontap Rest API - Fixed hardware API requests for bays
- PostgreSQL - Fixed an unsafe eval for unknown status option in collection mode
- Raritan PDU SNMP - Fixed an issue with sensors when powerFactor value is missing

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-Win32.exe)

</details>

<details>
<summary><h3 id="20250201-hotfix-20250305-20250321">20250201-hotfix-20250305 - 20250321</h3></summary>

#### News

- Fortigate: add mode to discover Fortiswitches through Fortigate FW
- Fortigate: add mode to monitor Fortiswitches through Fortigate FW
- StorageTek SL

#### Fixes

- apps-protocols-http-expected-content: fixed --http-backend option
- apps-protocols-http-json-content: fixed --http-backend option
- apps-protocols-http-soap-content: fixed --http-backend option
- Microsoft WSUS: add missing macros on Host template (#3471)
- Sonus SBC DSP mode: fixed UNKNOWN error (#3464)

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-Win32.exe)

</details>

<details>
<summary><h3 id="20250201-20250305">20250201 - 20250305</h3></summary>

#### News

- Nortel network devices

#### Enhancements

- Windows WinRM: add network discovery rule

#### Fixes

- Aruba CX: fixed NeDi discovery rule
- Cisco IOS memory flash: exclude ucode0 (#3424)
- Eclipse Mosquitto MQTT Broker: fixed command for numeric-value, string-value
- VMware discovery - ivertix-host-discovery-vmware-datastore: add regexp for Datacenter variable

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-Win32.exe)

</details>

<details>
<summary><h3 id="20250201-20250217">20250201 - 20250217</h3></summary>

#### News

- HAProxy Web API

#### Enhancements

- Brocade: add snmpv3 option --contextname to handle virtual switches
- Fortigate Rest API: added threshold options --warning-last-update and --critical-last-update in license mode
- SMSEagle notification: add option --insecure

#### Fixes

- Azure Storage Blob: default timeframe to 3600 to avoid 0 values
- Azure Storage health: add default value average for aggregation
- Azure Storage Table: default timeframe to 3600 to avoid 0 values
- Brocade interface: removed fixed option --oid-display=ifName
- Netapp Ontap Rest API - hardware status fixed, error 400 Bad Request
- Moxa Switch SNMP - Fixed --add-duplex-status option in interface mode

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-Win32.exe)

</details>

<details>
<summary><h3 id="20250114-20250216">20250114 - 20250216</h3></summary>

#### Enhancements

- Windows SNMP service discovery: add option to filter for service name

</details>

<details>
<summary><h3 id="20250114-20250210">20250114 - 20250210</h3></summary>

#### Global change

- Added a common `--change-output-adv` plugin option to change the short output and the exit code at the same time

#### News

- Aruba CX series: add new HTPL for stack switch
- Aruba CX series: add new STPL for stack status
- Aruba CX series: add new STPL for spanning tree
- Aruba CX series: add new service discovery for spanning tree
- Aruba CX stack: add NeDi discovery rule
- Huawei WLC
- IBM Informix DB
- SMSEagle modem
- SMSEagle notification v2

#### Enhancements

- Aruba CX: renamed Host templates
- Cisco Meraki VPN status: refactored, new filter options
- Generic SNMP string request: add new configuration options
- Huawei switches: renamed and refactored
- Huawei switches: add option `--unit` on uptime with default value s (seconds)
- Lenovo XCC hardware: add health check for cpu, memory and global health
- Linux Inodes (SNMP/SSH): extend filter to exclude special partitions:	`^((?!^\/run|^\/sys|^\/dev|.*overlay-containers.*|.*docker\/containers\/.*\/shm|xc-install).)*$`
- MySQL/MariaDB database size: add extra option `--filter-perfdata=noperfdata` to reduce excessive performance data collecting
- Netapp Ontap Rest API - volumes: add thresholds for logical usage
- Nutanix VM: add extra option `--filter-perfdata=noperfdata` to reduce excessive performance data collecting
- O365 Exchange, Onedrive, Sharepoint, Teams: add extra option `--filter-perfdata=noperfdata` to reduce excessive performance data collecting
- Oracle DB - event waits: add extra option `--filter-perfdata=noperfdata` to reduce excessive performance data collecting
- Watchguard IPsec tunnels: add extra option `--filter-perfdata=noperfdata` to reduce excessive performance data collecting

#### Fixes

- Axis Video - Fixed wrong fan status mapping leading to false positives
- Cisco VG HTPL: removed load from HTPL
- Dell Datadomain: fixed wrong discovery commands
- Dell Datadomain: removed threshold overload from Hardware status
- Purestorage Flasharray API: service discovery templates fixed (missing RegexPattern)
- Stormshield API - Fixed mapped values for state and plugged in interfaces modes.

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-Win32.exe)

</details>

<details>
<summary><h3 id="20241206-hotfix-20250115-20250203">20241206-hotfix-20250115 - 20250203</h3></summary>

#### News

- Eclipse Mosquitto MQTT

#### Enhancements

- Aruba WLC - NeDi: add MM-Virtual to discovery rule
- Cisco AP only ping - NeDi: include more Cisco AP models
- Microsoft Hyper-V: ivertix-agent-apps-microsoft-hyperv-local-node-vm-status support german output
- HP Officeconnect - NeDi: include 1700 series

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-Win32.exe)

</details>

<details>
<summary><h3 id="20241206-hotfix-20250115-20250120">20241206-hotfix-20250115 - 20250120</h3></summary>

#### News

- Forcepoint/Stonesoft: add NeDi discovery rule

#### Enhancements

- Ubiquiti Pro Switch: NeDi discovery rule will now match also for USxx series

#### Fixes

- AS400: fixed to avoid timeouts (#3036)
- Ubiquiti Pro Switch: fixed NeDi discovery rule

</details>

<details>
<summary><h3 id="20241206-20250115">20241206 - 20250115</h3></summary>

#### News

- SAP R3 or SAP 4/HANA: add host template, service templates and commands with SAP connection through message server

#### Enhancements

- Cisco 9200 series: renamed to Cisco Catalyst series
- Cisco 9200 series: renamed NeDi discovery rule to Cisco Catalyst
- Cisco Catalyst: changed NeDi rule to match only Catalyst devices
- Cisco Catalyst environment: override temp sensor machting sensor id \d01\d
- Cisco Standard switch: changed NeDi rule to match only IOS devices
- Cisco Standard switch: removed load from host template
- Cisco WLC IOS: renamed to Cisco WLC Catalyst
- Cisco WLC IOS XE: based on Cisco Catalyst host template

#### Fixes

- fixed icons on service templates

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-Win32.exe)

</details>

<details>
<summary><h3 id="20241206-20241213">20241206 - 20241213</h3></summary>

#### News

- AppearTV
- Dell Datadomain: refactored
    - new mode alert
    - new mode cleaning
    - new mode interfaces
    - new mode Mtrees
    - new mode process
    - new discovery modes for filesystems, interfaces, Mtrees, replications

#### Enhancements

- MariaDB: used the correct MariaDB message when checking MySQL replication state
- IBM Storwize: add $_HOSTEXTRA-OPTS$ $_SERVICEEXTRA-OPTS$ macros (ticket #3219)

#### Fixes

- Cisco IOS configuration status: fixed to have better last running change date
- Cisco WLC: fixed wrong unit for roundtrip-time
- Commvault: fixed storagepools mode to avoid division by 0
- Exclipse Mosquito MQTT: fixed warning-regexp and critical-regexp options
- Linux SSH process: Fixed an issue with the process mode that wasn't returning the process in some cases. We added a column size limit to avoid filter issues
- PostgreSQL: fixed exclude option working as "include"
- Speedtest: fixed packaging issue leading to conflict between speedtest and speedtest-cli binaries
- Windows (WS-Management): fixed warning status issue on os-windows-wsman-pending-reboot. The warning status was not under single quotes

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20241206-Win32.exe)

</details>

<details>
<summary><h3 id="20241011-20241207">20241011 - 20241207</h3></summary>

#### Enhancements

- Cisco WLC AP status: add new threshold: CRITICAL-TOTAL -> 1: (see ticket #3114)

#### Fixes

- Dell Compellent: fixed interface discovery
- Dell Compellent: fixed interface monitoring

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240909-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240909-Win32.exe)

</details>

<details>
<summary><h3 id="20241011-20241124">20241011 - 20241124</h3></summary>

#### News

- Netgear ReadyNAS: add network discovery rule
- Peplink Loadbalancer

#### Enhancements

- Aruba WLC: better NeDi discovery rule
- Dell Unisphere: allow special chars on password
- Netgear ReadyNAS storage: exclude system partitions
- Purestorage volume thresholds: changed default thresholds from B/s to MB/s
- Printer RFC - printer error now with default option --big-endian
- Windwos Task scheduler (i-Vertix Agent): add on critical threshold `or exit_code ne 0` to raise an alert if task scheduler jobs failes (Ticket 3116)

#### Fixes

- Cisco Virtual Stack: discovery rule corrected
- VMware vSAN Cluster usage: fixed CMD, removed not exiting option --filter
- VMware vSAN Cluster usage: fixed CMD, removed option --cluster-name

</details>

<details>
<summary><h3 id="20241011-20241113">20241011 - 20241113</h3></summary>

#### Enhancements

- Purestorage Flasarray volumes: add standard thresholds for reads_per_sec, writes_per_sec, usec_per_read_op, usec_per_write_op, read_bytes_per_sec, write_bytes_per_sec

#### Fixes

- Cisco NeDi: fixed discovery rule for stack device (9200)

</details>

<details>
<summary><h3 id="20241011-20241111">20241011 - 20241111</h3></summary>

#### News

- Cisco C9200 series: add new Host templates to handle the specific environment monitor
- Cisco C9200 series: add new Host templates to handle the specific memory monitor
- Cisco C9200 series: add NeDi discovery rules to identify C9200 switches
- IBM Storwize: new mode vdisk-status (exclude vdisks from component mode) which handles also hyperswap configuration

#### Enhancements

- Cisco standard device interface: add option to monitor FC waits
- Cisco Voice Gateway IOS: add new config status
- Cyberpower UPS load: new threshold and metrics for phase-voltage
- Purestorage Flasharray Array/Volume: add new metrics and thresholds

#### Fixes

- Cisco standard configuration: refactored, fixed wrong calculation
- Cisco Virtual Stack: fixed NeDi rule
- i-Vertix4 Poller: add missing service discovery rules for Linux
- Microsoft WSUS Host Template: fixed wrong host variables - **this problem was introduced by Plugin version "20240909 - 20241028" and blocks the Poller Export**

</details>

<details>
<summary><h3 id="20240909-20241028">20240909 - 20241028</h3></summary>

#### News

- IBM TS2900
- IBM TS3100
- IBM TS3200
- IBM TS3500
- i-Vertix Business Intelligence Server

#### Enhancements

- Cisco SBS: better NeDi rule (add SGX devices)
- Microsoft-WSUS-iVertix-agent: add wsus-server and wsus-port

#### Fixes

- AKCP: command definition was not correct
- Kubernetes discovery templates fixed (contains wrong XML keyfield)
- Lenovo Rackswitch Interfaces: added default critical status condition

#### Business Intelligence

- Service category ivertix_bi_energy_consumption: Category containing all service templates for electric power consumption

</details>

<details>
<summary><h3 id="20240909-20240925">20240909 - 20240925</h3></summary>

#### News

- AWS Classic ELB Loadbalancer
- AWS Classic ELB Availbaility Zone
- AWS Network Loadbalancer
- Azure Application Gateway
- Azure VPN Gateway
- HPE Alletra

#### Enhancements

- HP Procurve: add spanning tree discovery and monitoring

#### Fixes

- HP standard network device: fix spanning tree discovery
- SAP (check_sap_health): fix CMD configuration / wrong path was set

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240909-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240909-Win32.exe)

</details>

<details>
<summary><h3 id="20240808-20240912">20240808 - 20240912</h3></summary>

#### News

- Hashicorp Vault
- HMS Netbiter Argon
- HP Procurve Virtual Chassis: add NeDi discovery rule
- Proxmox Mail Gateway

#### Fixes

- Dell MD3000: fix CMD
- Sophos XGS VPN: fixed wrong command threshold options

#### Business Intelligence

- Service category `ivertix_bi_disk:` add service templates apps-vmware-connector-datastore-io & apps-vmware-connector-datastore-iops to category
- Service category `ivertix_bi_storage`: add service template apps-vmware-connector-datastore-usage to category

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240808-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240808-Win32.exe)

</details>

<details>
<summary><h3 id="20240808-20240827">20240808 - 20240827</h3></summary>

#### News

- New service categories for the i-Vertix BI module:
    - `ivertix_bi_cpu`
    - `ivertix_bi_memory`
    - `ivertix_bi_ping`
    - `ivertix_bi_storage`
    - `ivertix_bi_traffic`
    - `ivertix_bi_uptime`
    - `ivertix_bi_sensors`
    - `ivertix_bi_disk`
    - `ivertix_bi_datastore_vm`
    - `ivertix_bi_datastore_latency`
    - `ivertix_bi_vmware_host_vm`
    - `ivertix_bi_vmware_vm_performance`

</details>

<details>
<summary><h3 id="20240808-20240826">20240808 - 20240826</h3></summary>

#### News

- Cisco Meraki VPN tunnels (monitoring + discovery)
- HPE Primera
- Microsoft Teams notification using workflow api
- Nokia ISAM - formerly Alcatel ISAM
- Sophos XGS - add new mode to monitor Sophos licenses
- Sophos XGS - add new mode to monitor and HTPL for HA status
- Sophos XGS - add new mode to monitor Sophos VPN
- Sophos XGS - add discovery for VPN's
- Teldat cells radio service discovery

#### Enhancements

- 3CX supports now also v18 or higher
- Cisco Meraki devices: add new filter --filter-link-name: Filter VPN links by name
- Teldat cells radio refactored

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240808-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240808-Win32.exe)

</details>

<details>
<summary><h3 id="20240613-20240809">20240613 - 20240809</h3></summary>

#### News

- Buffalo Terastation: add NeDi rule
- Dell S-Series: add NeDi rule
- FortiSwitch: add NeDi rule

#### Enhancements

- FortiGate NeDi rule: exclude FortiSwitch devices
- Huawei network devices: add option to visualize ifAlias
- cloud-aws-lambda-invocation: add EXTRA_OPTS --zeroed (Set metrics value to 0 if none)
- command apps-vmware-connector-cpu-cluster: add scope-datacenter filtered by host macro HOSTDATACENTER
- Host template vCenter: remove service relation apps-vmware-connector-cpu-cluster (will be created from VMware discovery for each cluster on datacenter)

#### Fixes

- Datacore: fix service discovery rule
- Dell N-Series: correct NeDi rule
- IBM DB2: fixed CMD's, remove wrong options
- IBM DB2 logs: fixed wrong threshold options

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240613-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240613-Win32.exe)

</details>

<details>
<summary><h3 id="20240613-20240709">20240613 - 20240709</h3></summary>

#### Release note

here you can access to the [KB ](https://helpdesk.i-vertix.cloud/front/knowbaseitem.form.php?id=110)for this version

#### News

- Aruba Orchestrator
- Cisco DNAC Center
- Varnish cache

#### Enhancements

- Dell N-Series: correct NeDi rule
- HMC Hardware errors: set default hmc-command on STPL
- HMC Led errors: define default thresholds

#### Fixes

- HMC Hardware errors: fixed wrong option command-hmc in CMD
- Microsoft Hyper-V Agent: fixed Hyper-V integration status
- VMware host alive: fixed CMD to ignore default values

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240613-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240613-Win32.exe)

</details>

<details>
<summary><h3 id="20240516-20240621">20240516 - 20240621</h3></summary>

#### Release note

here you can access to the [KB ](https://helpdesk.i-vertix.cloud/front/knowbaseitem.form.php?id=109)for this version

#### News

- Avigilon camera
- Ubiquiti Pro switches NeDi discovery rule

#### Enhancements

- Citrix Netscaler Health: add option to handle standard or alternative status mapping
- Purestorage Flasharray Rest API: changed service discovery for Arrays and Volumes: ID is keyfield, name is used for service description
- RRD tools: add ping mode
- RRD tools: refactored

#### Fixes

- Aruba Clearpass: fixed all commands, wrong reference
- Cambium cnPilot: fixed commands for cpu and memory
- Purestorage Flasharray Rest API: fixed wrong cmd's and STPL

#### i-Vertix agent

- download [i-Vertix Agent x64](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240516-x64.exe)
- download [i-Vertix Agent  x86](https://i-vertix-downloads.s3.eu-west-1.amazonaws.com/i-Vertix+agent/iVertix-NSClient-0.5.2.41-20240516-Win32.exe)

</details>

<details>
<summary><h3 id="20240311-20240606">20240311 - 20240606</h3></summary>

#### News

- Aruba Clearpass

#### Enhancements

- Dell OS10: better NeDi rule

#### Fixes

- CIFS: fixed a wrong hostname directive in all commands

</details>

<details>
<summary><h3 id="20240311-20240603">20240311 - 20240603</h3></summary>

#### News

- HP Virtual Connect NeDi rule

#### Fixes

- Meraki Cisco: fixed CMD for Meraki Cache
- O365 Service discovery: add special char regexp

</details>

<details>
<summary><h3 id="20240311-20240531">20240311 - 20240531</h3></summary>

#### News

- Brocade ICX switch: new NeDi rule
- Dell N-Series: new NeDi rule
- Dell OS10: new NeDi rule
- F5 BigIP: new NeDi rule
- Fujitsu iRMC Host discovery rule
- HWg-STE: new NeDi rule
- HP Virtual Connect
- i-Vertix4 Poller
- Windows Agent: add CMD and STPL ivertix-agent-check_ping (remote ping)

#### Enhancements

- Cisco Meraki cache generation: add option --ignore-orgs-api-disabled to CMD
- HP 3PAR: add variables $_HOSTEXTRA-OPTS$ $_SERVICEEXTRA-OPTS$ to CMD's
- IBM/Lenovo Rackswitch: NeDi rule update

#### Fixes

- apps-protocols-snmp-string-value: fixed CMD and STPL
- apps-protocols-snmp-numeric-value: fixed CMD and STPL
- Cisco WLC: radius - wrong units for rountrip (new unit is µs)
- Docker service discovery: fixed mapping to ID
- i-Vertix4 Central: broker statistics for i-Vertix4
- ivertix-agent-os-windows-local-list-storages: legacy-password not under single quotes
- ivertix-agent-os-windows-local-list-certificates: legacy-password not under single quotes

</details>

<details>
<summary><h3 id="20240311-20240424">20240311 - 20240424</h3></summary>

#### News

- Dynatrace
- Grafana
- Graylog

#### Enhancements

- i-Vertix4 Central Gorgone processes: changed the memory thresholds
- i-Vertix4 Central: add discovery for processes and inodes
- Juniper SRX: STPL storage: add filter for storages to monitor

#### Fixes

- i-Vertix4 Central: fix HTPL macros
- Juniper SRX: fix STPL for ipsec-tunnel with wrong --critical-status value
- Juniper SRX: fixed all CMD's (missing hostname and snmp-timeout option)
- O365 credential app: CMD has wrong Macros applied
- Veeam Enterprise Manager: change backend to curl to avoid HTTP 411 errors

</details>

<details>
<summary><h3 id="20240311-20240411">20240311 - 20240411</h3></summary>

#### News

- Alpha UPS
- Emerson PDU
- i-Vertix4 Central
- Oracle Sun server hardware
- Slack notification
- Teams notification
- Telgram notification

#### Enhancements

- rename i-Vertix3 Poller Plugin Pack to i-Vertix Poller
- Ubiquiti Edge switches NeDi rule
- Veeam Enterprise Manager: add lwp as default http backend

#### Fixes

- add Quantum HTPL to Plugin Pack
- MySQL/MariaDB: fix CMD for replication
- Vertix EES: fixed wrong CMD for input lines

</details>

<details>
<summary><h3 id="20240311-20240327">20240311 - 20240327</h3></summary>

#### News

- ActiveMQ monitoring
- Avaya AES monitoring
- Avaya Media Gateway monitoring
- DataCore monitoring
- VerneMQ monitoring

#### Enhancements

- Windows updates i-Vertx Agent: add filter to exclude non mandatory updates

#### Fixes

- Docker SSH: fixed wrong SSH Backend default value to sshcli

</details>

<details>
<summary><h3 id="20240212-20240320">20240212 - 20240320</h3></summary>

#### Enhancements

- Meraki API: new HTPL generic-host-tcp-port

#### Fixes

- AWS API Gateway: fixed commands to be work with plugin version 20230311

</details>

<details>
<summary><h3 id="20240212-20240317">20240212 - 20240317</h3></summary>

:::info

Please checkout our KB for the Plugin version [2024.02.12](https://helpdesk.i-vertix.cloud/front/knowbaseitem.form.php?id=103)

:::

#### News

- Cisco ASA: add NeDi discovery rule
- Cisco Call Manager: add storage discovery and monitoring
- Cisco Call Manager: add tcp monitoring for H232, SCCP, SIP, TFTP
- Cisco Call Manager: add udp monitoring for HTFTP
- Cisco ISE: new HTPL for OS monitoring
- Cisco Meraki: new discovery rule for Meraki cellular gateways
- Cisco SMB: add Host discovery rule
- Fortigate FW: add new mode for link-monitor
- Fortigate FW: add new discovery for link-monitor
- Himoinsa Generator (UPS)
- Microsoft Azure Monitor
- Teldat
- Quantum Scalar

#### Enhancements

- AWS Cloudwatch: discovery template "cloud-aws-cloudwatch-metrics" extended to handle multi dimensions.
- Barracuda VPN discovery: exclude Barracuda Network Access Client
- Cisco SMB: NeDi discovery rules matches now also for CBS series
- VMware datastore IOPS for NFS: changed rule to exclude all NFS share like NFS41
- Veeam EM: better special char support
- Windows SNMP: STPL DHCP-Server know works also on german systems

#### Fixes

- Active Directory: STPL ivertix-agent-check_pdh-lsass-processor-time: remove "%" from service description
- SNMP custom: fixed CMD apps-protocols-snmp-string-value
- Socomec UPS: fixed wrong battery temperature calclulation
- Veeam EM: fixed service discovery template for jobs

</details>

<details>
<summary><h3 id="20231215-20240213">20231215 - 20240213</h3></summary>

#### News

- Barco Clickshare
- Patton SmartNode: add interface discovery
- Patton SmartNode: add interface monitoring

#### Enhancements

- APC UPS input lines: add standard thresholds for 3phase input line voltages
- Netapp Ontap Restapi: volume discovery add filter state = online
- VMware VSAN: add new warning/critical macros and tresholds for backend-latency-(read|write)
- Windows SNMP: add --snmp-autoreduce on HTPL (compatibility with SNMP version 2c)
- Windows DHCP SNMP: add --snmp-autoreduce on HTPL (compatibility with SNMP version 2c)

</details>

<details>
<summary><h3 id="20231215-20240130">20231215 - 20240130</h3></summary>

Please checkout our KB for the Plugin version [20231215](https://helpdesk.i-vertix.cloud/front/knowbaseitem.form.php?id=102)

#### News

- ADFA FSB 150
- ADFA FSB 3000
- Aruba WLC: add NeDi rule
- AWS Backup
- Azure Loadbalancer
- Azure Web Application Firewall
- Cisco Application Policy Infrastructure Controller (APIC)
- Cisco Umbrella
- Dell MX7000 (OpenManage Enterprise Modular)
- Dell VxRail Manager
- HP Procurve: new stack mode
- HP Procurve: new HTPL Procurve Stack
- HP standard switch: add HTPL and CMD's to monitor VRRP
- Infoblox IPAM/DNS/DHCP
- NVIDIA GPU
- SFTP protocol (active)
- Slack monitoring
- Riverbed Steelhead
- RRDcached

#### Enhancements

- Aruba CX: removed STPL "virtual chassis" and "virtual switch extension" from HTPL "Aruba-CX-Series-SNMP"
- Aruba CX: new HTPL "Aruba-CX-Series-SNMP-VC" containing STPL "virtual chassis" and "virtual switch extension"
- Nokia TimOS: add filter for SAS alarms
- HP Procurve: modified NeDi rule for Procurve Stack (switch with Virtual Chassis)
- Oracle ACME SBC: add missing Plugin Pack description

#### Fixes

- Aruba WLC License: removed default value for warning-status
- Aruba WLC AP connections: fixed CMD and STPL
- AS400: fix CMD for subsystem
- AS400: fix disk discovery template (wrong service name)
- CIFS files count: fixed wrong tresholds in CMD
- Dell iDRAC uptime: removed --force-oid=.1.3.6.1.4.1.674.10892.5.2.5.0, returns wrong values (wrong unit)
- Synology hardware: fixed disk failing

</details>

<details>
<summary><h3 id="20231114-20231230">20231114 - 20231230</h3></summary>

#### News

- AWS Cloudwatch Application ELB
- AWS Cloudwatch Elasticsearch/Opensearch
- Cambium cnPilot
- Mobotix Camera: add NeDi rule
- Oracle ZS storage (SNMP)
- Oracle ZS storage (Rest API)
- SMSEagle notification

#### Enhancements

- Cisco Call Manager SNMP: add CPU to HTPL
- Docker SSH: add discovery modes for Container status and usage
- Ribbon/Sonus SBC: added Ribbon logo, renamed HTPL & Plugin Pack

#### Fixes

- AWS Application ELB: fixed command definition
- Dell EMC Unishpere: fixed CMD for replication status
- Firebird custom SQL: fixed CMD
- Sonus SBC: fixed cmd's for storage and channels

</details>

<details>
<summary><h3 id="20231114-20231207">20231114 - 20231207</h3></summary>

#### News

- AWS Application ELB
- HPE OneView
- Sonus SBC

#### Enhancements

- AWS Lambda: add timeframe and period as Host macros
- Rubrik: add possibility to authenticate with token

#### Fixes

- MongoDB: fixed wrong commands/threholds
- Rukrik: service discovery fixed (jobid)

</details>

<details>
<summary><h3 id="20231017-20231122">20231017 - 20231122</h3></summary>

#### News

- Cisco WAP: add NeDi discovery rule
- CS121/CS141 UPS: add NeDi discovery rule
- Docker SSH
- Lenovo Thinksystem (Netapp SANtricity OEM)
- Meraki discovery: add rule for Appliance
- Ruckus AP: add NeDi discovery rule
- Ruckus ZoneDirector: add NeDi discovery rule

#### Enhancements

- Oracle Fra usage: add standard thresholds (10/25) to reclaimable space
- VMware datastore discovery: enabled regexp for special chars
- Windows service discovery: enabled regexp for special chars

#### Fixes

- Docker Rest API: add missing generic-host to HTPL

</details>

<details>
<summary><h3 id="20231017-20231031-2">20231017 - 20231031-2</h3></summary>

#### Fixes

- Windows SNMP: fix CMD --critical -> critical-total

</details>

<details>
<summary><h3 id="20231017-20231031">20231017 - 20231031</h3></summary>

#### News

- Alcatel ISAM
- Fujitsu Eternus DX: official Fujitsu Nagios plugin
- InfluxDB
- Kadiska
- OpenVPN
- Oracle VM Manager
- Vertiv Geist sensor
- Wallix Bastion
- Whois - Domain monitoring

#### Enhancements

- Nokia TiMOS: new mode SAS alarm
- Linux local/ssh: new mode and STPL for Systemd Journal
- Linux local/ssh: new mode and STPL for Systemd Journal - Postfix sent mails
- Linux local/ssh: new mode and STPL for Systemd Journal - CentEngine reloads
- Linux local/ssh packet errors: add default threshold `critical-status='%{status} ne "RU"'`
- Linux SNMP: new discovery mode for Disk IO
- Website/HTTP response: add STPL for extended metrics
- Windows Agent: monitor certificates from cert store
- Windows Agent: discover certificates from cert store

#### Fixes

- Sophos XG/Cyberoam: fix CMD + STPL for interface discovery & monitoring (--oid-filter=ifDesc --oid-display=ifDesc)

</details>

<details>
<summary><h3 id="20230810-20231023">20230810 - 20231023</h3></summary>

#### News

- Windows i-Vertix Agent: add storage network discovery rule

#### Enhancements

- AWS Lambda: add standard warning thresholds for errors
- Netapp Santricity: allow special chars in password

#### Fixes

- AWS Cloudwatch: fixed CMD and discovery template for list-metrics

</details>

<details>
<summary><h3 id="20230810-20231011">20230810 - 20231011</h3></summary>

#### News

- AWS Cloudwatch
- Firebird Database
- Google Compute Engine
- Sun sfxxk
- Watchguard: new NeDi rule

#### Enhancements

- AWS API Gateway: use paws instead of awscli
- AWS Direct Connect: use paws instead of awscli
- AWS EC2: use paws instead of awscli
- AWS EBS: use paws instead of awscli
- AWS EFS: use paws instead of awscli
- AWS Elasticache: dedicated HTPL for Redis and Memcached
- AWS Elasticache: use paws instead of awscli
- AWS Kinesis: use paws instead of awscli
- AWS Lambda: use paws instead of awscli
- AWS RDS: use paws instead of awscli
- AWS S3: use paws instead of awscli
- AWS SQS: use paws instead of awscli
- AWS Transit Gateway: use paws instead of awscli
- Dell iDrac uptime: new STPL for uptime using OID .1.3.6.1.4.1.674.10892.5.2.5
- Elasticsearch index statistic: remove performance datas
- MongoDB replication status: add ARBITER on warning-status
- O365 application secrets: set default thresholds for password expire to 20d/10d (WARN/CRIT)

#### Fixes

- O365: fixed service discovery template for subscriptions

</details>

<details>
<summary><h3 id="20230810-20230920">20230810 - 20230920</h3></summary>

#### News

- AVM Fritzbox
- AWS APIGateway
- AWS EFS
- AWS ElastiCache
- AWS Kinesis
- AWS Lambda
- Sophos XGS Firewall (v18/v19)

#### Enhancements

- QNAP Hardware status: add EXTRA-OPTS `'--snmp-force-getnext'` to avoid UNKNWON if legacy OID is not present (never firmwares)
- Selenese: new STPL for E2E needed by E2E wizard (STPL for Chrome/Firefox now legacy and will be removed in the future)
- Speedtest: add Jitter thresholds
- Windows i-Vertix Agent Pending Reboot: add default warning threshold `WARNING-STATUS = %{RebootPending} =~ /true/i`
- Windows i-Vertix WinRM Pending Reboot: add default warning threshold `WARNING-STATUS = %{RebootPending} =~ /true/i`
- VMware Snapshot usage: add status thresholds and set `CRITICAL-STATUS = '%{accessible} !~ /^true|1$/i'`
- VMware Host CPU: add default option `--filter-perfdata='cpu-total'` to not collect grafics for single cores

#### Fixes

- Alcatel-Lucent: fixed NeDi rule
- FortiWLC: add HTPL generic-host
- Fujistu Eternus DX: fix CMD for PSU, raid-groups & physical disks (removed threshold overload option)
- Lenovo Rackswitch: fixed CMD's for hardware & cpu
- MySQL/MariaDB: fix wrong CMD for custom sql
- Netapp Ontap Rest API: fixed CMD for Cluster status
- Nimble rest api: special chars in password now works
- Speedtest: fixed CMD
- UPS RFC1628 output lines: fixed wrong option
- WD NAS: fixes list volumes mode (wrong mode)

</details>

<details>
<summary><h3 id="20230810-20230828">20230810 - 20230828</h3></summary>

Please checkout our KB for the [Plugin version 20230810](https://helpdesk.i-vertix.cloud/front/knowbaseitem.form.php?id=89)

#### News

- Alcatel Omniswitch: add NeDi rule
- Audiocode: add new mode & STPL for SBC calls
- IBM Storwize: add new mode, STPL & HTPL for Replication
- Linux SNMP: add new mode & STPL for TCP connections
- Linux SNMP: add new mode & STPL for UDP connections
- Linux SSH: add discovery for Systemd Services
- MariaDB/Mysql: add new mode & STPL to monitor Open tables
- MariaDB/Mysql: add new mode & STPL to monitor custom SQL (integer return)
- MariaDB/Mysql: add new mode & STPL to monitor custom SQL (string return)
- Netapp Ontap Rest API Plugin Pack
- Splunk Plugin Pack
- Rubrik: add new mode & STPL to monitor Rubrik Jobs
- Rubrik: add new discovery for Rubrik Jobs

#### Enhancements

- APC input line: new tresholds and metrics
- Audiocode: add SNMP timeout option
- Audiocode CPU: add thresholds for core cpu util
- Audiocode Memory: add thresholds for system memory
- Brocade interface: add Macro oid-extra-display (default ifAlias)
- Cisco Meraki device: add Macro (warning|critical)-links-ineffective
- Dell EMC Datadomain: exlude storage "/data: pre-comp"
- Dlink standard interface: add option oid-extra-display (ifAlias default)
- Extreme interface: add option oid-extra-display (ifAlias default)
- Fortiswitch interface: add option oid-extra-display (ifAlias default)
- HWg-STE-Sensors: add Host option --snmp-force-getnext to support better v2 sensors
- Juniper EX interface: add option oid-extra-display (ifAlias default)
- Lenovo Iomega interface: add option oid-extra-display (ifAlias default)
- Raisecom interface: add option oid-extra-display (ifAlias default)
- Rittal CMC3: plugin refactoring, add macro for SNMP timeout
- Speedtest: add new thresholds for ping jitter
- Speedtest: renamed ping time to ping latency
- Stormshield FW storages: exclude some system partition
- Teltonica: renamed system to modem
- UPS RCF1628 alarm: display alarm description on verbose mode (verbose mode default on)
- UPS RCF1628 alarm: add new Macros for statuses
- UPS RCF1628 output lines: add new thresholds for frequency

#### Fixes

- Oracle sql string: fixed default value for empty string

</details>

<details>
<summary><h3 id="20230608-hotfix20230630-2-20230812">20230608-hotfix20230630-2 - 20230812</h3></summary>

#### News

- XPPC Phoenixtec UPS

#### Enhancements

- Cisco Meraki: removed STPL network-cisco-meraki-cloudcontroller-restapi-api-requests from HTPL
- Dell iDrac: add option for threshold-overload
- Mikrotik Interfaces: add new threshold options
- VMware Cluster CPU: change time-shift from 1800 to 3600

#### Fixes

- Mikrotik Firmware: add missing default value
- Netscaler vServer SSL discovery: fixed discovery template
- Netapp Ontap SNMP: add default filter on Filesystem to exclude snapshot FS

</details>

<details>
<summary><h3 id="20230608-hotfix20230630-2-20230717">20230608-hotfix20230630-2 - 20230717</h3></summary>

#### News

- APC Netboz 250
- Cisco IOS: new plugin to check/verify "Configuration status"
- Cisco Meraki camera - new rule for discovery
- FortiMail
- Stormshield Firewall SNMP
- Stormshield Firewall Rest API

#### Enhancements

- HP ILO XMLAPI: add threshold-overload='nic,OK,other'
- i-Vertix: STPL gorgone-ivertix - new threshold for 6 processes
- Netscaler: new vServer discoery for Loadbalancer
- Netscaler: new vServer discoery for SSLVPN/Contextswitching
- Netscaler: new vServer STPL for Loadbalancer
- Netscaler: new vServer STPL for SSLVPN/Contextswitching

#### Fixes

- Enterasys storage cmd: renamed filter-memory-name to filter-storage-name
- HPE Simplivity: add generic-host to HTPL
- HPE Simplivity: fix wrong CMD

</details>

<details>
<summary><h3 id="20230608-hotfix20230630-2-20230630-2">20230608-hotfix20230630-2 - 20230630-2</h3></summary>

#### Fixes

- Host discovery - fix a blocking issue with Host discovery
- Linux SSH: fix Host Discovery rule

</details>

<details>
<summary><h3 id="20230608-hotfix20230630-20230630-devel">20230608-hotfix20230630 - 20230630-devel</h3></summary>

#### Fixes

- resolve a blocking issue with Host discovery

</details>

<details>
<summary><h3 id="20230608-20230630">20230608 - 20230630</h3></summary>

#### News

- Enterasys network devices
- Rittal CMC III

</details>

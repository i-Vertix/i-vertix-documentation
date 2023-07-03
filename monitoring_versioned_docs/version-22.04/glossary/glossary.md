---
id: glossary
title: Glossary of i-Vertix IT Monitoring
---

## ACL

Access Control Lists allow you to grant rights to i-Vertix users. You can grant users rights on:

- the menus of the i-Vertix web interface,

- [resources](#resource) users have access to

- the actions that can be performed in the i-Vertix web interface.

**See also**: [Granting rights to i-Vertix users (ACL)](../managing-users-contacts/acl.md).

## Acknowledgement

When a user acknowledges a resource in i-Vertix, they are notifying their teams that they are mindful of the incident and that they will be taking action to resolve it.

When a resource is acknowledged, [notifications](#notification) are stopped, and the resource is highlighted yellow in monitoring screens.

Acknowledging a resource does not mean that the incident is over: it is over when the resource returns to state **OK** or **UP**.

**See also**: [Acknowledging a problem](../events-alerts/managing-alarms/acknowledge.md).

## Architecture: simple VS distributed

- **Simple architecture**: architecture that consists entirely of a [Central Manager](#central-server).

- **Distributed architecture**: architecture consisting of a [Central Manager](#central-manager) and of n [remote server(s)](#remote-server) and [Smart Poller(s)](#smart-poller). Remote servers and pollers allow you to distribute the monitoring load, either for security reasons, geographical or historical reasons, etc.

**See also**: [Architectures](../installation/before-you-start/architecture.md).

## BBDO

Broker Binary Data Object: communication protocol used to transfer monitoring data from [remote servers](#remote-server) and [Smart Pollers](#poller) to the [Central Manager](#central-server).


## Broker

i-Vertix Broker is the software component that receives monitoring data collected by [monitoring engines](#monitoring-engine).
Once it receives this data, by default, I-Vertix Broker redistributes them to the MariaDB and RRD databases.


## Broker reverse mode

Advanced configuration for i-Vertix [Broker](#broker) that reverses the direction of connection for Broker communications. It switches the "client" and "server" roles so as to adapt to particular network configurations. For exemple, this mode is used by I-Vertix MAP to subscribe to the real-time flow of Broker events.

## Central Manager

In i-Vertix, the Central Manager is the main console where you monitor resources. The Central Manager allows you to:

- configure the monitoring of your whole infrastructure,
- monitor resources
- see what all your i-Vertix servers monitor (Central Manager, [remote servers](#remote-server) and [Smart Pollers](#smart-poller)), using its web interface.


## Downtime

A downtime is a time period during which [notifications](#notification) are disabled for a resource. Downtimes are used during planned maintenance operations, to avoid getting unnecessary alerts.

**See also**: [Planning a downtime](../events-alerts/managing-alarms/downtimes.md).

## Engine

See [**Monitoring engine**](#monitoring-engine).

## FQDN

Fully Qualified Domain Name: hostname and domain name for a server. E.g.: demo.I-Vertix.com (hostname: demo, domain name: I-Vertix.com).

## Gorgone

I-Vertix Gorgone is the software component that allows the [Central Manager](#central-manager) to send information to the [remote servers](#remote-server) and the [Smart Pollers](#smart-poller).
Among other things, Gorgone deploys the configuration to the [monitoring engines](#monitoring-engine).


## Graphs

Graphs are generated from the [metrics](#metric) that make up [services](#service), using [RRD files](#rrd-files). They show how these metrics evolve in time.

**See also**: [Graph template](../performance-graphs/graph-template.md) and the other topics in this section.

## Inheritance

Principle according to which a parameter of a [template](#template) is applied to the resource that inherits from this template.

## Host

Devices that have an IP address or FQDN and the host monitoring refers to the process of tracking and analyzing the performance and avalability of a device. Examples: a server, a network device, a website, a printer, a virtual environment, a cloud instance, etc. A host can have one or more associated [services](#service).

A host can have one of the following [statuses](#status): OK, DOWN, UNREACHABLE.

See also: [Monitoring a host](../quick-start-guide/configuring-first-hosts-services/monitoring-the-first-host.md) and the other topics in this section.

## LVM

LVM (logical volume manager): I-Vertix recommends that you use this partitioning system when you install your host system. It will allow you to live adjust the size of partitions and to use LVM snapshots for backups.

## LVM snapshot

Feature included in LVM that allows you to do a snapshot of a file system. I-Vertix uses this process to back up databases.

**See also**: [Backup](../administration/parameters/backup-Backup.md).

## Metric

A metric (or performance data) is part of a [service](#service). This piece of data allows you to display graphs, and to define thresholds according to which you will receive notifications. These thresholds will determine the [status](#status) of the service to which the metric belongs.

If a service has multiple metrics, the state of the service that has the value of the metric outside the threshold and therefore has the highest criticality is shown.

You can see all metrics attached to a service in the details panel of the service.

## Monitoring action

Any action in the interface that affects your real-time monitoring. For instance, to [acknowledge a resource](#acknowledgement), to [plan a downtime](#downtime), to force a check, etc.

## Monitoring engine

I-Vertix Engine is the software component that plans checks, executes them, and [notifies](#notification) users if an incident occurs.
I-Vertix Engine is present on [Smart Pollers](#smart-poller), [remote servers](#remote-server) and the [Central Manager](#central-manager).

## MySQL Dump

Backup, in a text file, of a MySQL/MariaDB database.

## Notification

Message or alert that is sent to inform someone of a particular event or incident.Notification can be sent though various channels, such as email, text message, Teams, etc. You can configure notifications on various [statuses](#status).

**See also**: [How notifications work](../events-alerts/managing-alarms/how-notifications-works.md) and the other topics in this section.


## Performance data

See [**Metric**](#metric).

## Plugin

A plugin is a monitoring probe, i.e. a binary executable or a script that is called by the [monitoring engine](#monitoring-engine) to carry out a check on a [host](#host) or [service](#service). The plugin determines which status should be sent to the monitoring engine, based on the checks it makes and on the thresholds defined in the configuration of the host or service.

## Plugin Pack

The term "Plugin pack" refers to a [plugin](#plugin) and the corresponding pack.

A pack contains the configuration of the plugin in i-Vertix (command, [templates](#template), thresholds), as well as data required by the automatic discovery feature.

**See also**:


## Smart Poller

i-Vertix server used in a [distributed architecture](#architecture-simple-vs-distributed). A Smart Poller can be attached to a [remote server](#remote-server), or directly to a [Central Manager](#central-manager).

- Smart Poller monitors [resources](#resource). It has a [monitoring engine](#monitoring-engine).

- Smart Poller has no graphical interface: the resources it monitors are displayed in the interface of the Central Manager and of the remote server it is attached to.

- Smart Poller can send notifications even if there is no communication with the Central Manager and remote servers.

"Smart Poller" is also used to refer to the monitoring engine that is present in a Central Manager, a remote server and a Smart Poller.

## Pull mode

Advanced configuration for i-Vertix [Gorgone](#gorgone) that reverses the direction of ZMQ flows. The communication is initiated by pollers and remote servers, and is directed to the central server. This mode is commonly used by MSPs.


## Recurring downtime

Recurring downtimes are [downtimes](#downtime) that occur regularly.

**See also**: [Recurrent downtimes](../events-alerts/managing-alarms/downtimes.md#recurrent-downtimes).

## Remote server

i-Vertix server used in a [distributed architecture](#architecture-simple-vs-distributed). A remote server is attached to a central server. Smart Pollers can be attached to a remote server.

- A remote server monitors [resources](#resource). It has a [monitoring engine](#monitoring-engine).

- It has a graphical interface, but no configuration menus.

- The resources it monitors are displayed in its interface, and in the interface of the central server it is attached to.

## Resource

Object monitored by a i-Vertix platform ([hosts](#host), [services](#service), metaservices).

## Retention files

Retention files belong to I-Vertix [Broker](#broker). These files store the monitoring data that could not be inserted into the database. For instance, if a communication problem occurs between Engine and Broker, the data is not lost, Broker stores them in a file (whose name includes the term "queue"). The file will then be read by I-Vertix Broker, then inserted into the databases so as to avoid data loss.

## Retention period

Time period, in days, during which you want to keep the data from your RRD and MariaDB databases.

## RRD files

An RRD file contains the data for a [metric](#metric). RRD files are used to build performance [graph](#graphs). If there are no RRD files, graphs cannot be displayed. Because of the way RRD works, the data displayed in the graphs show a trend rather than the exact data that was measured.

## Scheduler

See [**Monitoring engine**](#monitoring-engine).

## Service

A service is attached to a [host](#host). It is a check point on this host, that can relate to:

- the status of a component: is the power supply connected? Is my instance started?

- the performance of a component: is my website accessible in less than 0.5s? How much of the memory is used on my server?

A service can consist of one or several [metrics](#metric).

A service can have one of the following [statuses](#status): OK, WARNING, CRITICAL, UNKNOWN.

**See also**: [Monitoring a service](../quick-start-guide/configuring-first-hosts-services/monitoring-the-first-host.md) and the other topics in this section.

## State

Unhandled, acknowledged, in downtime.

## Status

Indicates:

- the availability of a [host](#host) (UP, DOWN, UNREACHABLE),

- the availability or performance of a [service](#service) (OK, WARNING, CRITICAL, UNKNOWN).

PENDING is not a status: a resource is "pending" when it has just been created and hasn't been checked yet.

**See also**: [Possible statuses of a resource](../events-alerts/managing-notifications/how-notifications-works.md#status-types).

## Status type

Indicates whether a change in [status](#status) is confirmed (HARD) or not confirmed (SOFT). For instance, if a status becomes HARD, notifications are triggered.

**See also**: [Status types](../events-alerts/managing-notifications/how-notifications-works.md#status-types).

## Template

i-Vertix templates are preconfigured monitoring settings that can be assigned to one or more hosts or services, containing checks, thresholds, notification rules, and graphs.
Skeleton of a [resource](#resource) that is preconfigured so that parameters defined on the skeleton are applied to the resource that inherits from it.


**See also**:

- [Using host templates](../monitoring-resources/monitoring-hosts/host-templates.md),
- [Using service templates](../monitoring-resources/monitoring-services/service-template.md),
- [Using contact templates](../managing-users-contacts/contact-templates.md).

## Time period

Time Periods is a predefined list of time intervals that are used in the i-Vertix IT Monitoring platform to schedule monitoring of various IT infrastructure and services. They enable the functionalities of the [monitoring engine](#monitoring-engine) over a given time slot. Use time periods to define:

- when check commands are executed, i.e. the time period during which resources are monitored

- when [notifications](#notification) are sent

**See also**: [Time periods](../monitoring-resources/generic-object-actions/timeperiods.md).

## Widget

A widget is a configurable visual element that provides a specific function and can be placed on a dashboard or on a map. Widgets can be used for a variety of purposes such as displaying information, controlling devices or applications, providing access to features or settings, and more.

**See also**: [Custom views](../events-alerts/viewing-events/create-custom-view.md).

## ZMQ

ZeroMQ appears as a networking library but operates like a concurrency framework with fast, scalable sockets for transmitting atomic messages over various transports, N-to-N connections with different patterns, and an asynchronous I/O model that can handle multicore applications. It offers language APIs and works on various operating systems. [source](https://zeromq.org/).

Protocol used by i-Vertix [Gorgone](#gorgone) to communicate from the [Central Manager](#central-manager) to the [remote servers](#remote-server) and the [Smart Pollers](#smart-poller), in a [distributed architecture](#architecture-simple-vs-distributed).


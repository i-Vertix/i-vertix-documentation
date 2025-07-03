---
id: architecture
title: Architectures
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

If you are monitoring a small number of hosts and services, a Central Manager is enough. However, to monitor a large number of hosts and services, you will need to distribute the load over multiple Smart Pollers.

## Available architectures

<Tabs>
<TabItem value="simple" label="Basic" default>

### Basic architecture

The basic architecture is set up as follows:

* 1 Central i-Vertix IT Monitoring server

:::info

When operating the monitoring system using a basic architecture:

* the data is collected, processed, stored and delivered by the Central i-Vertix Monitoring server
* the web interface is provided by the Central i-Vertix Monitoring server

:::

</TabItem>
<TabItem value="distributed" label="Distributed">

### Distributed architecture

The distributed architecture is set up as follows:

* **1** Central i-Vertix IT Monitoring server
* **1+** i-Vertix Pollers

:::info

When operating the monitoring system using a distributed architecture:

* the data is collected and initially processed by the i-Vertix Pollers
* the collected data is sent to the Central i-Vertix Monitoring server
* the collected data is stored on the Central i-Vertix Monitoring server
* the web interface is provided by the Central i-Vertix Monitoring server

:::

:::tip

This architecture is especially useful to:

* enable load balancing - when monitoring a large amount of hosts and services, it is recommended to distribute the load on multiple pollers
* monitor isolated networks in an easier and more secure way

:::

</TabItem>
<TabItem value="remotedbms" label="Remote DBMS">

### Remote Database management architecture

The distributed architecture is set up as follows:

* **1** Central i-Vertix IT Monitoring server
* **1** Separate Database management server
* **1+** i-Vertix Pollers

:::info

When operating the monitoring system using a remote DMBS architecture:

* the data is collected and initially processed by the i-Vertix Pollers
* the collected data is sent to the Central i-Vertix Monitoring server
* the collected data is stored on the separate Database Management server
* the web interface is provided by the Central i-Vertix Monitoring server

:::

:::tip

This architecture is especially useful to:

* enable load balancing - when monitoring a large amount of hosts and services, it is recommended to distribute the load on multiple pollers
* monitor isolated networks in an easier and more secure way
* store the data on a separate optimized database server

:::

</TabItem>
<TabItem value="remoteservers" label="Remote Servers">

### Remote Server architecture

The remote server architecture is set up as follows:

* **1** Central i-Vertix IT Monitoring server
* **1+** i-Vertix Remote servers
* **1+** i-Vertix Pollers

:::info

When operating the monitoring system using a remote server architecture:

* the data is collected and initially processed by the i-Vertix Pollers/Remote Servers
* the collected data is sent to the connected i-Vertix Remote Server
* the stored data on the i-Vertix Remote Server is sent to the Central i-Vertix Monitoring server
* the collected data is stored on the connected i-Vertix Remote server and the Central i-Vertix Monitoring server
* the web interface is provided by the Central i-Vertix Monitoring server and the i-Vertix Remote servers

**What is the difference between a i-Vertix Remote Server and a Poller?**

Remote servers can collect and process data in the same way as an i-Vertix Poller does, with the addition that additional Pollers can be linked to the Remote server. The Remote server stores the collected data on his own database instance but forwards the data also to the Central monitoring server. The data can be viewed both on the Remote server and on the Central Monitoring server.

:::

:::tip

This architecture is especially useful to:

* enable load balancing - when monitoring a large amount of hosts and services, it is recommended to distribute the load on multiple pollers
* monitor isolated networks in an easier and more secure way
* have the possibility to directly view collected data by connected Pollers on the Remote servers - this is useful when directly accessing the Central i-Vertix Monitoring server is not always possible

:::

</TabItem>
</Tabs>

## Components

### Central i-Vertix Monitoring server

* Apache (webserver)
* i-Vertix IT Monitoring web interface (provides the graphical monitoring interface)
* MariaDB (stores the monitoring configuration and collected data) - only when there is no separate database server
* Monitoring Engine (collects data)
* Monitoring Broker (stores processed data in the database and generates graphs)
* Gorgone Engine (manages connections between Pollers, Remote servers and the Central server)

### i-Vertix Poller

* Monitoring Engine (collects and processes data)
* Gorgone Engine (manages the connection between the Poller and the Central server)

### Remote monitoring server

* Apache (web server)
* i-Vertix IT Monitoring web interface (provides the graphical monitoring interface)
* MariaDB (stores the monitoring configuration and collected data)
* Gorgone Engine (manages the connection between the Poller and the Central server)
* Monitoring Engine (collects data)
* Collected data are sent to Broker SQL using cbmod by monitoring engine
* Monitoring Broker (stores processed data in the database and generates graphs + forwards data to the Central monitoring server)
* Gorgone Engine (manages connections between Pollers, Remote servers and the Central server)

### DBMS Server

* MariaDB (stores the monitoring configuration and collected data)

## What kind of architecture do you need?

When designing your i-Vertix IT Monitoring platform, have the following things in mind:

* The number of hosts you will monitor is not enough to determine how big your platform should be. You will also need to take into account the number of services per host, as well as the number of metrics per service.
* The need to use Smart Pollers or remote servers to separate your resources according to geographical or logical criteria.
  
  *Example:* If your monitoring architecture has to monitor a DMZ area, it is easier (and safer) to place a remote server in the DMZ network.

* A Central Manager should only monitor a small number of hosts and services, as its CPU must primarily handle the data sent by remote servers and Smart Pollers (this is the same for remote servers). The more hosts and services you monitor on your Central server, you higher the risk of the interface being slowed down, as the monitoring engine will use more resources.
* The Central server should monitor all remote servers and Smart Pollers.
* The Central server should be monitored by a Smart Poller or a remote server.
* Use a Remote server instead of a i-Vertix Poller if you need to visualize data on a site other than where the central server is located.

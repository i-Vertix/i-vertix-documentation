---
id: architecture
title: Architectures
---

If you are monitoring a small number of hosts and services, a Central Manager is enough. However, if you monitor a large number of hosts and services, you will need to distribute the load over multiple Smart Pollers.

## Available architectures

> ### Simple architecture

The simple architecture is to have all oversight entities within the same server, ie:
* i-Vertix IT Monitoring web interface
* Databases (MariaDB + RRD)
* Monitoring Engine
* Broker

This architecture is the simplest a user may encounter.
### Components
Many components are used to build this architecture:
* Apache web server for i-Vertix IT Monitoring web interface
* MariaDB databases to store i-Vertix IT Monitoring configuration parameters as well as monitoring and performance data
* A monitoring engine to collect data
* Collected data are sent to Broker SQL using cbmod by monitoring engine
* Broker SQL allows to store information into MariaDB databases and forward them to Broker RRD
* Broker RRD generates and updates RRD files with data in order to display performance graphs

> ### Distributed architecture

The distributed architecture is to have two types of entities:
* A central i-Vertix IT Monitoring server to display information
* One or more i-Vertix Poller to collect data
The i-Vertix IT Monitoring server includes the following items:
* i-Vertix IT Monitoring web interface
* Databases (MariaDB + RRD)
* Monitoring Engine
* Broker
The i-Vertix Poller includes the following items:

* Monitoring Engine
* Broker module to forward collected data to a central broker
This architecture is used for:
* Enable load balancing across multiple remote monitoring servers
* Network streams isolation: if your monitoring architecture have to monitor a DMZ area, it is easier (and safe) to place a remote server in the DMZ network
### Components
> ### i-Vertix IT Monitoring
Many components are used to build this architecture:
* Apache web server for i-Vertix IT Monitoring web interface
* MariaDB databases to store i-Vertix IT Monitoring configuration parameters as well as monitoring and performance data
* A monitoring engine to collect data
* Collected data are sent to Broker SQL using cbmod by monitoring engine
* Broker SQL allows to store information into MariaDB databases and forward them to Broker RRD
* Broker RRD generates and updates RRD files with data in order to display performance graphs
> ### i-Vertix Poller
Many components are used to build a poller:
* A monitoring engine to collect data
Collected data are sent to Broker SQL using cbmod by monitoring engine


> ### Architecture with remote DBMS

The distributed architecture with remote DBMS is to have three types of entities:
* A central i-Vertix IT Monitoring server to display information
* A DBMS server to store collected data
* One or more i-Vertix Poller to collect data
The i-Vertix IT Monitoring server includes the following items:
* i-Vertix IT Monitoring web interface
* Monitoring Engine
* Broker
* RRD files
The DBMS server store information into MariaDB databases.
The i-Vertix Poller includes the following items:
* Monitoring Engine
* Broker module to forward collected data to a central broker
This architecture is used for:
* Enable load balancing across multiple remote monitoring servers
* Network streams isolation: if your monitoring architecture have to monitor a DMZ area, it is easier (and safe) to place a remote server in the DMZ network
* Have a remote DBMS
### Components
> ### DBMS Server
The DBMS server is used only to store i-Vertix IT Monitoring configuration parameters as well as monitoring and performance data into MariaDB databases
> ### i-Vertix IT Monitoring
Many components are used to build this architecture:
* Apache web server for i-Vertix IT Monitoring web interface
* The central i-Vertix IT Monitoring server get configuration and collected data from DBMS server
* A monitoring engine to collect data
* Collected data are sent to Broker SQL using cbmod by monitoring engine
Broker SQL allows to store information into MariaDB databases and forward them to Broker RRD
* Broker RRD generates and updates RRD files with data in order to display performance graphs
> ### i-Vertix Poller
Many components are used to build a poller:
* A monitoring engine to collect data
* Collected data are sent to Broker SQL using cbmod by monitoring engine

> ### Remote Server architecture
The distributed architecture with Remote sever is to have three types of entities:
* A central i-Vertix IT Monitoring server to display information
* One or more i-Vertix Remote server to display & operate on a subset of collected data
* One or more i-Vertix Poller to collect data
The i-Vertix IT Monitoring server includes the following items:
* i-Vertix IT Monitoring web interface
* Databases (MariaDB + RRD)
* Monitoring Engine
* Broker
The Remote servers include the following items:
* I-Vertix IT Monitoring web interface (display & operate a subset of data)
* Monitoring Engine
* Databases (MariaDB + RRD) - Broker module to forward collected data to a central broker
The i-Vertix Poller includes the following items:
* Monitoring Engine
* Broker module to forward collected data to a central broker
This architecture is used for:
* Enable load balancing across multiple remote monitoring servers
* Network streams isolation: if your monitoring architecture have to monitor a DMZ area, it is easier (and safe) to place a remote server in the DMZ network
* Have dedicated web interface to display and operate on a subset of data
Components
> ### DBMS Server
The DBMS server is used only to store i-Vertix IT Monitoring configuration parameters as well as monitoring and performance data into MariaDB databases
> ### i-Vertix IT Monitoring
Many components are used to build this architecture:
* Apache web server for i-Vertix IT Monitoring web interface
MariaDB databases to store i-Vertix IT Monitoring configuration parameters as well as monitoring and performance data
* The Gorgone process is used to send monitoring configuration to the remote server and to manage it
* A monitoring engine to collect data
* Collected data are sent to Broker SQL using cbmod by monitoring engine
* Broker SQL allows to store information into MariaDB databases and forward them to Broker RRD
* Broker RRD generates and updates RRD files with data in order to display performance graphs
> ### Remote monitoring server
Many components are used to build a remote server:
* Apache web server for i-Vertix IT Monitoring web interface
* MariaDB databases to store monitoring and performance data
* The Gorgone process is used to operate on collected data
* A monitoring engine to collect data
* Collected data are sent to Broker SQL using cbmod by monitoring engine
* Broker SQL allows to store information into MariaDB databases and forward them to Broker RRD locally. All information are forwarded to the i-Vertix IT Monitoring central server
* Broker RRD generates and updates RRD files with data in order to display performance graphs
> ### i-Vertix Poller
Many components are used to build a poller:
* A monitoring engine to collect data
* Collected data are sent to Broker SQL using cbmod by monitoring engine

## What kind of architecture do you need?

When designing your i-Vertix IT Monitoring platform, bear the following things in mind:

* The number of hosts you will monitor is not enough to determine how big your platform should be. You will also need to take into account the number of services per host, as well as the number of metrics per service.
* Another criterion to take into account is whether you need to use Smart Pollers or remote servers to separate your resources according to geographical or logical criteria. Example : If your monitoring architecture has to monitor a DMZ area, it is easier (and safer) to place a remote server in the DMZ network.
* A Central Manager should only monitor a small number of hosts and services, as its CPU must primarily handle the data sent by remote servers and Smart Pollers (this is the same for remote servers). The more hosts and services you monitor on your Central Manager, you higher the risk of the interface being slowed down, as the monitoring engine will use more resources.
* The Central Manager should monitor all remote servers and Smart Pollers.
* The Central Manager should be monitored by a Smart Poller or a remote server.
* Use a remote server instead of a Smart Poller if you need to visualize data on a site other than where the central server is located.
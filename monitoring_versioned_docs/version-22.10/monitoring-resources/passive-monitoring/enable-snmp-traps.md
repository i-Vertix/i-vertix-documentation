---
id: enable-snmp-traps
title: Enable SNMP Traps
---

## Description

SNMP traps are information sent from monitored devices to a polling server using the SNMP protocol.
This information contains several attributes, including

* The address of the device sending the information
* The root OID (Object Identifier) corresponding to the identifier of the received message
* The message sent by the SNMP trap, which corresponds to a set of settings (1 through N).

To be able to interpret the received event, the management server must have in its configuration the necessary elements to translate the event.
To do this, it must have a database containing the OID and the descriptions, which are called MIB files. There are two types of MIBs:

* Standard MIBs, which use standardized OIDs and are implemented by many vendors on their devices
* MIB vendors, which are specific to each vendor and often to each device model.

MIB vendors can be retrieved from the device.
I-Vertix allows us to store the definition of SNMP traps in its MariaDB database.
The traps can then be associated with passive services via the **Relationships** tab of a service's definition.

## Architecture

### SNMP trap processing by the central server

SNMP trap processing is as follows:

1. **snmptrapd** is the service that allows the retrieval of SNMP traps sent by the device (by default, it listens on port **UDP 162**).
2. Once the SNMP trap is received, it is sent to the 'centreontrapdforward' script, which writes the received information to a buffer folder (by default **/var/spool/centreontrapd/**)
3. The **centreontrapd** service reads the information received in the buffer folder and interprets the traps received, checking the i-Vertix database for the actions required to handle these events
4. **centreontrapd** transmits the information to the scheduler or the **gorgoned** service (to send the information to a remote scheduler), which changes the status and information associated with the service to which the SNMP trap is linked.

![image](../../assets/monitoring-resources/passive-monitoring/06_trap_centreon.png)

### SNMP trap processing by a poller server

To keep a copy of the SNMP trap configuration on each satellite server, a SQLite database is used to cache the trap information contained in the MariaDB database. This SQLite database is automatically created by the central server.

The processing of an SNMP trap is as follows:

1. **snmptrapd** is the service used to retrieve SNMP traps sent by the device (by default it listens on port **UDP 162**)
2. Once the SNMP trap is received, it is sent to the 'centreontrapdforward' script, which writes the received information to a buffer folder (by default **/var/spool/centreontrapd/**)
3. The **centreontrapd** service reads the information received in the buffer folder and interprets the various traps received, checking in the SQLite database the actions to be taken to process the traps received
4. The **centreontrapd** service transmits the information to the scheduler, which changes the status and information associated with the service to which the SNMP trap is linked.

![image](../../assets/monitoring-resources/passive-monitoring/06_trap_poller.png)


:::note

The i-Vertix Gorgone process is responsible to copy the SQLite base on the remote poller.

:::

### Successive actions by the centreontrapd process

Successive actions by the centreontrapd process are:

![image](../../assets/monitoring-resources/passive-monitoring/SNMP_Traps_management_general_view.png)
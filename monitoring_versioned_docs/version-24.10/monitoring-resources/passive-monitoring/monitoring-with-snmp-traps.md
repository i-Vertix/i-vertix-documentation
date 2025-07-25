---
id: monitoring-with-snmp-traps
title: Monitoring with SNMP Traps
---

## Monitoring configuration

Go to the **Configuration > Services > Services by host** menu and click on **Add**.

* Set a description of the service
* Select the host to which to attach this service
* Select the **generic-service-passive** template

![image](../../assets/monitoring-resources/passive-monitoring/06createpassiveservice.png)

* Go on the **Relation** tab and choose the SNMP traps in **Service Trap Relation**

![image](../../assets/monitoring-resources/passive-monitoring/06servicetrapsrelation.png)

* Click on **Save**

## Applying the changes

To be able to export the OID present in the database in the configuration file to centreontrapd, follow the following procedure:

1. Go to the **Configuration > SNMP traps > Generate** menu
![image](../../assets/monitoring-resources/passive-monitoring/generate.png)
2. Select the poller to which you want to export the configuration files
3. Check **Generate traps database** and **Apply configurations**
4. In the drop-down list **Send signal** (the **Reload** option is preferable)
![image](../../assets/monitoring-resources/passive-monitoring/apply.png)
5. Click on the **Generate** button
6. [*Export the monitoring configuration*](../export-configuration)

## Advanced settings

### Modify the output

#### Use all the arguments

For a SNMP trap, when configuring the output message, the argument ```$\``` will display all information (the value of arguments) contained in the SNMP trap.
However, it is possible to display only certain information contained in the SNMP trap by invoking uniform arguments.

For example:
![image](../../assets/monitoring-resources/passive-monitoring/06servicetrapsrelation.png)

The output message **Link down on interface $2. State: $4.** will display only the name of the interface and its status
(`$2` and `$4` argument).

Where can I find the arguments?

The arguments are in the documentation of the MIB manufacturer or in the **Comments** field of the SNMP trap.

![image](../../assets/monitoring-resources/passive-monitoring/klinkcomment.png)

To show:

* The index link, use the `$1` argument
* The interface name , use the `$2` argument
* The administrative state of the interface, use the `$3` argument
* The state interface, use the `$4` argument

For example, the following output message displays all the arguments:

``` shell
Link down on interface: $2 (index: $1). Operational state: $4, Administration state: $3
```

#### Active checks after trap reception

**Reschedule associated services** option to actively check the service after the trap reception.

The active service linked in the service configuration is executed.

#### Execute special command

With **Centreontrapd** it is possible to execute a special command after receiving a SNMP trap.
Just use the option **Execute special command** followed by the description of this command.

#### Use all the arguments (via OID)

It is also possible to have an argument value directly without knowing the order of the arguments ($1, $2, $3, etc.). to do this, use the full OID number of the needed arguments.

For example:

``` shell
Link down on interface: @{.1.3.6.1.2.1.2.2.1.2} (index: @{.1.3.6.1.2.1.2.2.1.1}). Operational state: @{.1.3.6.1.2.1.2.2.1.8}, Administration state: @{.1.3.6.1.2.1.2.2.1.7}
```

#### Use an external variable

It's also possible to modify the output message by using scripts or external commands to retrieve information and include the result in the output.
To do this, go to the **Advanced** tab in the definition of your SNMP trap and add one (or more) preexec commands.

For example:
![image](../../assets/monitoring-resources/passive-monitoring/kpreexec.png)

The first command **snmpget -v 2c -Ovq -c public @HOSTADDRESS@ ifAlias.$1** and allows you to retrieve the alias interface. The "$1" variable is for the argument 1 associated value of linkUp/linkDown traps.

The second command **snmpget -v 2c -Ovq -c public @HOSTADDRESS@ ifSpeed.$1** and allows you to retrieve interface speed.
The "$1" variable is for the argument 1 associated value of linkUp/linkDown traps.

To see the result of the first command in the output, you must use $p1 argument. To include the result of the second command in the output, you must use $p2 argument.

Therefore, we can deduce the following output message:

``` shell
Link down on interface: $2 (index: $1). Operational state: $4, Administration state: $3, Alias : $p1, Speed : $p2
```

#### Use a Regular expression

It's also possible to transform the output using a regular expression with the **Output Transform** option. You just have to define the regexp and it will be executed when the trap is received.

For example:

``` shell
s/\|/-/g
```

Will replace **|** in the output to **-**.

### Route/Transfer SNMP traps

It is possible to have a SNMP trap concentrator. For example: Oracle GRID.
Oracle GRID is responsible for aggregating information for all Oracle servers when necessary, it's the Oracle GRID server that sends the SNMP trap to the monitoring server.

However, we want to extract the IP address of the host from the SNMP trap sent by Oracle GRID and display the message in the service trap not belonging to Oracle Grid but to the correct host.

To do this, perform the following steps:

1. Create a generic trap, with the following parameters:

* In **Main** Tab:

| Attributes     | Description           |
| -------------- | --------------------- |
| Trap Name      | Trap name             |
| Mode           | Unique                |
| OID            | OID of the trap       |
| Default Status | Trap default status   |
| Output Message | Custom output message |

* In **Advanced** Tab:

| Attributes       | Description                                                    |
| ---------------- | -------------------------------------------------------------- |
| Enable routing   | Checked                                                        |
| Route definition | `$2` (In this example $2 argument is for IP address of the host) |

2. Create a second trap definition:

* In **Main** Tab:

| Attributes     | Description                          |
| -------------- | ------------------------------------ |
| Trap Name      | Trap name (not the same as previous) |
| OID            | OID of the trap (same as previous)   |
| Default Status | Trap default status                  |
| Output Message | Custom output message                |

3. Associate the first definition to a service (eg PING) of Oracle GRID server
4. Associate the second definition to a passive service of the host.
5. Generate SNMP traps definitions and restart centreontrapd

In the **Route definition** field you can use the following arguments:

| Variable name       | Description                                                                           |
| ------------------- | ------------------------------------------------------------------------------------- |
| ```@GETHOSTBYADDR($2)@``` | Reverse DNS resolution to know the DNS name from IP address (127.0.0.1 -\> localhost) |
| ```@GETHOSTBYNAME($2)@``` | DNS resolution to know the Ip address from the DNS (localhost -\> 127.0.0.1)          |

### Ignore SNMP Trap when resource is on downtime

**Check Downtime** allows centreontrapd to check that the service is not in Downtime status when the trap is received. The submission can be aborted.

:::note

It's only possible with Centreon Broker and on Central monitoring.

:::

There are three ways to configure this:

* None: nothing to do, the trap is sent as normal
* Real-Time: with this option, a trap sent with a current downtime, the service status is not updated
* History: option used to not acknowledge a trap snmp that refers to a past event during a downtime.
---
id: create-host-manually
title: Creating host manually
---

To create a host manually these activities must be carried out:

1. Go to **Configuration \> Hosts \> Hosts** and then click **Add**.
2. Fill in the fields (see [below](#host-configuration-tab)), then click on **Save**.
3. [Export the configuration](export-configuration.md).

## Host configuration tab

### Host basic information

* **Name**: defines the host name that will be used by the IT Monitoring Engine.
* **Alias**: shows the alias of the host.
* **IP Address / DNS**: defines IP address or DNS name of the host. **Resolve** button enables to resolve the domain name by questioning the DNS server configured on the central server.
* **SNMP Community & Version**: contain the name of the community and the SNMP version.
* **Monitoring from**: indicates which poller is charged with monitoring this host.
* **Timezone**: indicates the timezone location of the monitored hosts.
* **Templates**: enables to associated one or more templates of hosts with this object. In case of conflicts of settings present on multiple templates, the host template above overwrites the identical properties defined in host templates below. This button enables us to change the order of host templates ![image](../../assets/create-host-manually/move.png#thumbnail1). This button serves to delete the host template ![image](../../assets/create-host-manually/delete.png#thumbnail1)

* If the **Create Services linked to the Template too** is **Yes**, i-Vertix IT Monitoring automatically generates the services based their self on the service templates linked to the [host templates](host-templates.md) defined above.

### Host check options

* **Check Command**: indicates the command use to check the availability of the host.
* **Args**: defines the arguments given to the check command (each argument starts with a ”!”).

* **Custom macros**:

   * **Name** and **Value** enable to define the name and value of the macro.
   * **Password** enables the value of the macro to be hidden.

  To reinitialize to the default value (defined in template) click on ![image](../../assets/create-host-manually/undo.png#thumbnail1)
  
  To view the description of the macro, click on ![image](../../assets/create-host-manually/description.png#thumbnail1)

  To delete the macro, click on ![image](../../assets/create-host-manually/delete.png#thumbnail1)

  To change the order of the macros, click on ![image](../../assets/create-host-manually/move.png#thumbnail1)

### Scheduling options

* **Check Period**: defines the time period during which the scheduler checks the status of the object.
* **Max Check Attempts**: defines the number of checks to be performed before confirming the status of the
  host: when the status is confirmed the notification process is triggered.
* **Normal Check Interval**: is expressed in minutes. It defined the interval between checks when the host status is OK.
* **Retry Check Interval**: is expressed in minutes. It defined the check interval of the Not-OK status of the host.
* **Active Checks Enabled** and **Passive Checks Enabled**: enable / disable the active and passive checks.

## Notification tab

* **Notification Enabled**: allows to enable or disable the notifications concerning the object.
* The list of **Linked contacts** indicates the contacts which will receive the notifications.
* The list of **Linked contacts Groups** indicates the groups of contacts which will receive the notifications.
  
  If, on page **Administration > Parameters > Centreon UI**, the **Vertical inheritance only** option is enabled, two extra checkboxes appear:

    * If the **Contact additive inheritance** box is checked, i-Vertix does not overwrite the configuration of the parent host template but adds the contacts in addition to the contacts defined in the parent template.
    * If the **Contact group additive inheritance** box is checked, i-Vertix does not overwrite the configuration of the parent host template but adds the contact groups in addition to the contact groups defined in the parent template.

* **Notification Options**: define the statuses for which a notification will be sent.
* **Notification Interval**: is expressed in minutes. It indicates the time between sending each notifications when the status is Not-OK. If the value is defined as 0 the scheduler sends a single notification per status change.
* **Notification Period**: field indicates the time period during which the notifications will be enabled.
* **First notification delay**: is expressed in minutes. It refers to the time delay to be respected before sending the first notification when a Not-OK status is validated.
* **Recovery notification delay**: is the time that must pass before a recovery notification is sent (when the host goes back to an UP state).

## Relations tab

* **Parent Host Groups**: defined the host groups to which the host belongs.
* **Parent Host Categories**: defined the categories to which the host belongs.
* **Parent Hosts**: enables us to define the physical family relationships between objects.
* **Child Hosts**: enables us to define the physical family relationships between objects.

## Data processing tab

* If **Obsess Over Host** is enabled, the host check feedback command will be enabled.
* **Acknowledgement timeout**: specify a duration of acknowledgement for this host or host depending to this template. If you leave it blank, no timeout will be set.
* **Check Freshness**: allows to enable or disable the result freshness check.
* **Freshness Threshold**: is expressed in seconds. if during this period no host status change request (passive command) is received the active check command is executed.
* **Flap Detection Enabled**: allows to enable or disable the detection flapping in the statuses (status value changing too often on a given period).
* **Low Flap Threshold** and **High Flap Threshold**: define the high and low thresholds for the detection of flapping in percentage of status change.
* **Retain Status Information** and **Retain Non Status Information**: indicate if the information concerning the status is saved after every time the check command is repeated.
* **Stalking Options**: defined the options to be recorded if retention is enabled.
* **Event Handler Enabled**: allows us to enable or disable the events handler.
* **Event Handler**: defined the command to be executed if the event handler is enabled.
* **Args**: defined the arguments of the events handler command.

## Host Extended Infos tab

### Monitoring engine

* **URL**: defined a URL that can be used to give more information on the host.
* **Note**: permits to add optional notes.
* **Action URL**: defined a URL normally use for giving information on actions on the host (maintenance, etc.).
* **Icon**: indicates the icon use for the host.
* **Alt Icon**: is the text use if the icon cannot be display.
* **Status Map Image**: defined the logo for Maps.
* **Geographic coordinates**: defines geographical coordinates used by the Geographic Maps to position the resource on a map. Define "Latitude,Longitude", for example for Amsterdam coordinates set "52.37,4.89".
* **2d Coords**: are obsolete
* **3d Coords**: are obsolete
* **Host severity**: indicates the severity level of the host.

### Access groups

* **ACL Resource Groups**: (only displayed for non administrator) allows to link this host to an hostgroup in order to visualize it (see [Access Control Lists](../../managing-users-contacts/acl.md)).

### Additional Information

* **Status**: allows to enable or disable the host.
* **Comments**: can be used to add a comment or a note.
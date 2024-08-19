---
id: groups
title: Groups
---

## Description

In i-Vertix, it is possible to group hosts and services into groups:

Generally speaking, groups are containers in which sets of objects that share a common property can be grouped together:

* Same physical identity (Dell, HP, IBM, etc. servers), logical identity (network equipment) or geographical identity
  (Europe, Asia, Africa, North America, etc.)
* belonging to the same application (CMS application, etc.) or to the same sector of activity (salary management, etc.)
* etc.

Host groups and service groups are used to group objects according to logical entities. They are used to:

* Configure ACLs to associate a set of resources with a type of profile.
* Allow availability reports to be viewed by group. Generate a "Rome Agency" availability report for resources.
* View the status of a set of items by selecting a group of items in the search filters.
* Quickly browse multiple performance graphs by browsing the object tree structure by group and then by resource.

Generally we try to group hosts by functional level. For example: DELL and HP hosts, or Linux, Windows, etc. hosts.
We also try to group services by application job. For example: Payroll application, ERP application, etc.

> For the hosts belonging to a host group, the retention of RRD files can be defined in the host group. This definition overrides the global definition.
> If the same host belongs to multiple groups, each with a retention definition, the highest value is selected for the host.

## Creating a host group

Go to the **Configuration > Hosts > Host Groups** menu and click on **Add**

* The **Name** and **Alias** define the name and alias of the host group.
* The **Members** list allows us to add hosts to the hostgroup.
* The **Notes** field allows us to add optional notes about the hostgroup.
* The **Notes URL** field defines a URL that can be used to provide further information about the host group.
* The **Action URL** field defines a URL normally used to give information about actions on the hostgroup (maintenance, etc.).
* The **Icon** field specifies the icon to be used for the hostgroup.
* The **Map Icon** is the icon used for mapping.
* The **Geographical Coordinates** field defines the geographical coordinates used by the MAP module to position the resource on a map.
* The **RRD Retention** field is expressed in days and is used to define the duration of retention of the services belonging to this hostgroup in the RRD database. It will be the default duration defined in the **Administration > Options** menu if this value is not defined.
* The **Activate/deactivate resource** and **Comments** fields allow the host group to be activated or deactivated and to be commented on.

## Creating a service group

Go to the **Configuration > Services > Service Groups** menu and click on **Add**

* The **Name** and **Description** fields describe the name and description of the service group.
* The **Linked Host Services** list allows us to select the different services that will be included in this group.
* The **Linked Host Group Services** list allows us to select the services linked to a host group that will be part of this group.
  of this group.
* The **Linked Service Templates** list allows you to deploy a service based on this template to all hosts linked to this group.
* The **Geo Coordinates** field defines the geographical coordinates used by the MAP module to position the resource on a map. Define **"Latitude,Longitude"**, for example for **Rome** set the coordinates to **"41.53,12.32"**.
* The **Status** and **Comments** fields allow you to activate or deactivate the service group and to add comments.
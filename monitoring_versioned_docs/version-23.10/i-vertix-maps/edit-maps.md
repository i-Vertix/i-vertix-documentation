---
id: edit-maps
title: Edit maps
---

## Editing

### Adding objects

From **Monitoring -> Maps** page, click on the map you want to edit, then click on Edit at the top right corner to enter **Edit mode** 

![Image](../assets/maps/button_edit.png)

To save the changes applied to the map, click on **Save Map**.

To discard them click on **Reset**. 

To get back to map visualization, click on **Exit Edit Mode**.

![Image](../assets/maps/save_map.png)

![Image](../assets/maps/select.png) **Select objects** icon (available only for graphical maps): allows you to select one or more objects and reposition it/them on the map

![Image](../assets/maps/marker.png) **Create a new marker** icon (available for both graphical and geographical maps): allows you  to **add a new object** on the map.

The **object** has the following **properties**:

![Image](../assets/maps/edit_properties.png)

* **Linked Object type**: Host, Service, Servicegroup, Hostgroup or Map
* **Icon Properties**: select **icon size** and the **icon pack** that is to be used
* **Service Status on Host Icon**: The host icon displays the most critical status of all services assigned to a host.

![Image](../assets/maps/host_status1.png)

![Image](../assets/maps/host_status2.png)

* **Label Properties**: if the label is enabled, it is possible to decide what information to display, its position relative to the object, size and color.
* **Popup Properties**: to select/change popup messages settings and configure which information they should include

### Adding Links

![Image](../assets/maps/line.png) **Create a new line** icon: to add a new line/link between 2 objects

The object has the following properties:

![Image](../assets/maps/edit_line_properties.png)

* **Linked Object type**: Host, Service, Servicegroup or Hostgroup.
* **Line Properties**: you can select the **thickness** of the line and the line **appearance** 

* **Performance Data Interpreter**: it can be used to select which performance metrics have to be displayed and the position of their values.

![Image](../assets/maps/performance_data.png)


* **Label Properties**: if the label is enabled, it is possible to decide what information to display, its position relative to the object, size and color.
* Popup Properties: to select/change popup messages settings and configure which information they should include

### Adding Gadgets

![Image](../assets/maps/gadget_icon.png) **Create a new gadget icon**.

Select the **service** that has to be represented by the new Gadget.

If in **Gadget Properties > Gadget** Type you select Map, instead of a service, you have to select the map that will be displayed within/inside the current one (i.e. the one you are editing). 

**Gadget Properties**: 
* **Gadget Type**: Gauge, Performance Graph, Big Text, Map
* **Gadget Size**
* **Gadget Opacity**

![Image](../assets/maps/gadget_properties.png)

**Performance Data Interpreter**
* **Metrics** select the performance metric that has to be displayed
* **Data unit**

![Image](../assets/maps/gadget.png)

**Label Properties**: if the label is enabled, it is possible to decide what information to display, its position relative to the object, size and color.

**Popup Properties**: to select/change popup messages settings and configure which information they should include

## Map in Map feature
The "Map in Map" feature allows user to embed smaller maps within larger maps to provide a hierarchical view of infrastructure. Maps are created for each segment or location of the network to represent specific areas of the infrastructure, such as different floors of a building or separate departments within an organization.

:::note

This functionality can be used on the Graphic Map or the Geo Map

:::

### How to use Map in Map

Create the Graphical or Geo Map ([Maps configuration](managing-maps.md)).

There are available two options: **Create New Marker** or **Create a new Gadget**.

### Create New Marker

**Create New Marker**: select "Map" on **Linked Object Type** and the map you want to show. The icon placed on the map will be smaller and stylised. In the Geo Map it will only be visible by zooming into the position of the inserted object.

**Select the icon size**: tiny, small, middle, big

**Save** the Map

**Icon for Graphical Map** (ok, critical, warning, unknown, pending status):

![Image](../assets/maps/ok_map.png) ![Image](../assets/maps/critical_map.png) ![Image](../assets/maps/warning_map.png) ![Image](../assets/maps/unknown_map.png) ![Image](../assets/maps/pending_map.png)

**Icon for Geo Map** (ok, critical, warning, unknown, pending status):

![Image](../assets/maps/ok_geo.png) ![Image](../assets/maps/critical_geo.png) ![Image](../assets/maps/warning_geo.png) ![Image](../assets/maps/unknown_geo.png) ![Image](../assets/maps/pending_geo.png) 

![Image](../assets/maps/create_marker1.png)

![Image](../assets/maps/create_marker2.png)

### Create a new Gadget

**Create a new Gadget**: select "Map" on **Gadget Type** and the map you want to show. The icon shown will be larger than the one created by marker. 

**Select the Gadget size**: small, medium, big

**Save** the Map

![Image](../assets/maps/map_gadget.png)

## Set acknowledgement
It is possible to acknowledge and stop the notification of hosts with problems directly from the map.

![Image](../assets/maps/ack_window_click.png)

Right click and select acknowlegde.

![Image](../assets/maps/ack_window.png)

## Set the downtime
It is possible to set downtime of hosts and related services directly from the map.

![Image](../assets/maps/set_down.png)

Press the right with button with the mouse and select downtime.

![Image](../assets/maps/set_down1.png)

Enter the period during which the downtime will be active.

## Full list of map icon
Host displays **UP** status

![Image](../assets/maps/ok.png) 

Host displays **WARNING** status

![Image](../assets/maps/warning.png)

Host displays **DOWN** status

![Image](../assets/maps/critical.png)

Host displays **PENDING** status

![Image](../assets/maps/pending.png)

Host displays **UNKNOWN** status

![Image](../assets/maps/unknown.png)

Service displays **OK** status

![Image](../assets/maps/ok_round.png)

Host displays **WARNING** status

![Image](../assets/maps/warning_round.png)

Service displays **CRITICAL** status

![Image](../assets/maps/critical_round.png)

Service displays **PENDING** status

![Image](../assets/maps/pending_round.png)

Service displays **UNKNOWN** status

![Image](../assets/maps/unknown_round.png)

All hosts in the hostgroup are in **UP** status

![Image](../assets/maps/ok_hostgroup.png)

One or more hosts in the hostgroup are in **WARNING** status

![Image](../assets/maps/warning_hostgroup.png)

One or more hosts in the hostgroup are in **DOWN** status

![Image](../assets/maps/critical_hostgroup.png)

One or more hosts in the hostgroup are in **PENDING** status

![Image](../assets/maps/pending_hostgroup.png)

One or more hosts in the hostgroup are in **UNKNOWN** status

![Image](../assets/maps/unknown_hostgroup.png)

All services in the servicegroup are in **UP** status

![Image](../assets/maps/ok_servicegroup.png)

One or more services in the servicegroup are in **WARNING** status

![Image](../assets/maps/warning_servicegroup.png)

One or more services in the servicegroup are in **CRITICAL** status

![Image](../assets/maps/critical_servicegroup.png)

One or more services in the servicegroup are in **PENDING** status

![Image](../assets/maps/pending_servicegroup.png)

One or more services in the servicegroup are in **UNKNOWN** status

![Image](../assets/maps/unknown_servicegroup.png)

The host is displaying **UP** status, but one or more services are displaying **WARNING** status.

![Image](../assets/maps/ok_warning.png)

The host is displaying **UP** status, but one or more services are displaying **CRITICAL** status.

![Image](../assets/maps/ok_critical.png)

The host is displaying **UP** status, but one or more services are displaying **UNKNOWN** status.

![Image](../assets/maps/ok_unknown.png)

One or more services are in  status **ACKNOWLEDGE**

![Image](../assets/maps/ok_acknowledge.png)

One or more services are in  status **DOWNTIME**

![Image](../assets/maps/ok_downtime.png)

The host is status **ACKNOWLEDGE**

![Image](../assets/maps/acknowledge.png)

The host is status **DOWNTIME**

![Image](../assets/maps/downtime.png)

All hosts are in **UP** status and services are in **OK** status

![Image](../assets/maps/ok_geo.png)

One or more hosts/services are in **WARNING** status

![Image](../assets/maps/warning_geo.png)

One or more hosts are in **DOWN** status and/or one or more service are in **CRITICAL** status

![Image](../assets/maps/critical_geo.png)

One or more hosts/services are in **PENDING** status

![Image](../assets/maps/pending_geo.png) 

One or more hosts/services are in **UNKNOWN** status

![Image](../assets/maps/unknown_geo.png)

All hosts are in **UP** status and services are in **OK** status

![Image](../assets/maps/ok_map.png)

One or more hosts/services are in **WARNING** status

![Image](../assets/maps/warning_map.png) 

One or more hosts are in **DOWN** status and/or one or more service are in **CRITICAL** status

![Image](../assets/maps/critical_map.png) 

One or more hosts/services are in **PENDING** status

![Image](../assets/maps/pending_map.png)

One or more hosts/services are in **UNKNOWN** status

![Image](../assets/maps/unknown_map.png) 


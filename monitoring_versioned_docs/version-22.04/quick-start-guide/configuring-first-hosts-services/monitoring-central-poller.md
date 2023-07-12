---
id: monitoring-central-poller
title: Monitoring Central and Poller
---

## Monitoring Central

In this example we show how to **manually add** and **monitor** the Central Manager from itself. The same procedure can be used to monitor any other hosts.
1. Install the **i-Vertix3 Monitoring Central** plugin from Plugin Store: **Administration -> i-Vertix -> Plugin Store**
2. To manually add an host select **Configuration -> Hosts -> Hosts** and click on **ADD**
3. Fill in the following fields:
    * **Name**: device/host name
    * **Alias**: alternative name / description
    * **IP Address / DNS**: IP address or FQDN of the host  (insert 127.0.0.1 for the Central Manager). If you enter a FQDN you can click on Resolve to have the system check name resolution. 
    * **Monitored from**: select "Central" from the dropdown menu
    * **Templates**: select relevant templates previously installed
    * **Create Services linked to the Template too**: Select Yes
 4. Click on **Save**

 ## Monitoring Poller

 In this example we show how to **manually add** and **monitor** the Smart Poller from itself. The same procedure can be used to monitor any other hosts.
1. Install the **i-Vertix3 Poller VM monitoring** plugin from Plugin Store: **Administration -> i-Vertix -> Plugin Store**
2. To manually add an host select **Configuration -> Hosts -> Hosts** and click on **ADD**
3. Fill in the following fields:
    * **Name**: device/host name
    * **Alias**: alternative name / description
    * **IP Address / DNS**: IP address or FQDN of the host  (insert 127.0.0.1 for the Central Manager). If you enter a FQDN you can click on Resolve to have the system check name resolution. 
    * **Monitored from**: select "Central" from the dropdown menu
    * **Templates**: select relevant templates previously installed
    * **Create Services linked to the Template too**: Select Yes
 4. Click on **Save**

 ![image](../../assets/quick-start/monitor_central_poller.png)

 ### Monitoring additional services (Service Discovery)

Once you have added an Host you can add additional Services manually. 

Select **Configuration -> Services -> Manual Discovery**

1. Select:  
    * **Host**: this is the Host to which you want to add services (in this example it’s the Central Manager or Poller)
    * **Discovery template**: set of commands that have to be executed to search for services (the system automatically shows relevant/applicable ones)
2. Click on Scan Host
3. Select the Services that you want to add and monitor and click on Add

![image](../../assets/quick-start/monitor_central_poller1.png)

### EXPORTING THE CONFIGURATION

Once the host and services have been added, it is essential to export the configuration for the changes to take effect.

[Exporting the configuration](../../monitoring-resources/monitoring-hosts/export-configuration.md)
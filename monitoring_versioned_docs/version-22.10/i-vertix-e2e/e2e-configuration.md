---
id: e2e-configuration
title: E2E Configuration
---

## Plugin Store

Go to Administration > i-Vertix > Plugin Store and install **Selenese synthetic monitoring** plugin.

![image](../assets/quick-start/e2e2.png)

## Create Host
You need to create a host manually, see the topic [how to create a host](../monitoring-resources/monitoring-hosts/create-host-manually.md).

### Host basic information

* **Name**: defines the host name that will be used by the IT Monitoring Engine.
* **Alias**: shows the alias of the host.
* **IP Address / DNS**: defines IP address or DNS name of the host. **Resolve** button enables to resolve the domain name by questioning the DNS server configured on the central server.
* **Monitoring from**: indicates which poller is charged with monitoring this host.
* **Templates**: assign the **generic-host** template

Press the Save button and then [export the configuration](../monitoring-resources/monitoring-hosts/export-configuration.md) to the Poller.

![image](../assets/quick-start/e2e1.png)

:::note

Check on the Resource page that the host is UP.

![image](../assets/quick-start/e2e3.png)

:::

## Create the scenario

### Add browser extension

Before recording the scenario, you need to install the Selenium browser extension. 

![image](../assets/quick-start/e2e10.png)

Here an example of created scenario:

![image](../assets/quick-start/e2e9.gif)

::: note

Please contact support@i-vertix.com for further assistance in creating scenarios.

:::

## E2E Management

Go to Configuration > Services > E2E Management

![image](../assets/quick-start/e2e5.png)

Different filters are available: **Search-text, Poller, Host, Servicegroup, Browser**.

Press the button + Add Scenario:

* **Service Name**: use a meaningful name 
* **Service Template**: select apps-selenese-scenario
* **Poller**: select the Smart Poller that will run the scenario
* **Host**: select the E2E Host
* **Scenario**: upload the previously created scenario
* **Browser**: select the browser that will run the scenario
* **Scenario Timeout**: this is the maximum time Selenium will wait for a scenario to load completely
* **Step Timeout**: this is the maximum time for every single step
* **Warning Time**: set threshold to error or warning after a specific amount of time
* **Critical Time**: set threshold to error or critical after a specific amount of time
* **Enable Screenshots**: enable if you want to save screenshots per step
* **Enable Debug Log**: enable if you want to debug
* **Comment**: insert description or a comment

Press the button Save and then [export the configuration](../monitoring-resources/monitoring-hosts/export-configuration.md) to the Poller.

## Resource Status
Now your Synthetic End use Monitoring scenario is ready. 

Go to Monitoring > Resource Status and search the E2E Host.

Here the result:

![image](../assets/quick-start/e2e7.gif)

Clic to E2E scenario service to check every monitored step on tab Details. 

If enabled, IT Monitoring allow to show the screenshoot per every step.

Go to Monitoring > Status Detalis > E2E Management

Different filters are available: **Poller, Host, Scenario**.

![image](../assets/quick-start/e2e8.png)


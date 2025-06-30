---
id: create-host-manually
title: Create the first Host
---

1. Go to **Configuration \> Hosts \> Hosts** and then click **Add**.
2. Fill in the fields (see [below](#host-configuration-tab)), then click on **Save**.
3. [Export the configuration](../../monitoring-resources/monitoring-hosts/export-configuration.md).

## Host configuration tab

* **Name**: defines the host name that will be used by the IT Monitoring Engine.
* **Alias**: shows the alias of the host.
* **IP Address / DNS**: defines IP address or DNS name of the host. **Resolve** button enables to resolve the domain name by questioning the DNS server configured on the central server.
* **SNMP Community & Version**: contain the name of the community and the SNMP version.
* **Monitoring from**: indicates which poller is charged with monitoring this host.
* **Templates**: enables to associated one or more templates of hosts with this object. In case of conflicts of settings present on multiple templates, the host template above overwrites the identical properties defined in host templates below. This button enables us to change the order of host templates ![image](../../assets/create-host-manually/move.png#thumbnail1). This button serves to delete the host template ![image](../../assets/create-host-manually/delete.png#thumbnail1)

![image](../../assets/quick-start/create-host.gif)

The following topics explain advanced host configuration: [Create Host Manually](../../monitoring-resources/monitoring-hosts/create-host-manually.md)
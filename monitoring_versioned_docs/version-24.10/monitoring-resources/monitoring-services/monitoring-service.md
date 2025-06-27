---
id: monitoring-service
title: Monitoring a service
---

A service is a monitoring aspects or indicator that is observed on a host. For instance, it could measure the percentage of partition used on a server, memory load, network traffic, and more.

To see the list of monitored services, go to **Configuration > Services > Services by host**.

It is possible to:

- [create a service manually](create-service-manually.md)
- [discover services automatically](create-service-automatically.md).

## Monitoring a service

1. Create a service:

    - Use the [host autodiscovery feature](../discovery/description): the corresponding services will be created automatically.

    - [Create a host manually](../monitoring-hosts/create-host-manually.md) using a [Plugin Pack](../plugin-packs), and select **Create Services linked to the Template too**: the services for the host will be created automatically.

    - Use the [service discovery feature](create-service-automatically.md).

    - Create the [service manually](create-service-manually.md) and, in the **Template** field, select a [service template](service-template.md) (coming from a Plugin Pack or not).

    - Create a check [command](../generic-object-actions/commands.md) or use an existing one, and link it to a service you have [created manually](create-service-manually.md).


2. [Export the configuration](../monitoring-hosts/export-configuration.md).
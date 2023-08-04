---
id: monitoring-principles
title: Monitoring principles
---

# Here are a few basic i-Vertix monitoring concepts:

* A [**host**](../monitoring-hosts/monitoring-host.md) is any device that has an IP address and that one wishes to monitor. For example, a physical server, a
  virtual machine, a temperature probe, an IP camera, a printer or a storage space.
* A [**service**](../monitoring-services/monitoring-service.md) is a check point, or indicator, to be monitored on a host. This can be the CPU usage rate, temperature,
  motion detection, bandwidth usage rate, disk I/O, and so on.
* In order to collect each indicator value, monitoring **plugins** are used which are periodically executed by a
  collection engine called **Centreon Engine**.
* To be executed, a plugin needs a set of arguments that define, for example, which host to connect to or through which protocol.
  The plugin and its associated arguments form a [**command**](../../monitoring-resources/generic-object-actions/commands.md).

For example, to monitor a host with i-Vertix is to configure all the commands needed to measure the desired indicators,
and then [deploy that configuration](../../monitoring-resources/monitoring-basics/config-deploy.md) to the collection engine so that these commands are run periodically.

Once hosts and services are monitored, they have a [status](../../events-alerts/viewing-events/concepts.md) in i-Vertix (e.g. **OK**, **Warning**, **Critical**...). You can keep track of any changes using the [Resources Status](../../events-alerts/viewing-events/resources-status.md) page.

If a problem occurs (not-OK/not-UP status), [contacts](../../managing-users-contacts/contacts-users.md) will be able to receive [notifications](../../events-alerts/managing-notifications/configuring-notification.md), within set [time periods](../../monitoring-resources/generic-object-actions/timeperiods.md).

In i-Vertix, monitoring is made easy by the following elements:

- [Host templates](../../monitoring-resources/monitoring-hosts/host-templates.md) and [service templates](../../monitoring-resources/monitoring-services/service-template.md), that allow you to define default values so as to speed up the creation of these objects.

- [Plugin Packs](../../monitoring-resources/monitoring-basics/plugin-packs.md), that provide ready-to-use host and service templates. These greatly simplify the configuration of hosts and services: for instance, all you have to do is to apply Plugin Pack templates to a host for it to be monitored.

- The [autodiscovery feature for hosts and services](../../monitoring-resources/discovery/description.md), that allows you to get a list of new hosts and services and to add them automatically to the list of monitored resources.
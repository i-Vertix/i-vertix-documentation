---
id: monitoring-principles
title: Monitoring principles
---

# Here are some basic i-Vertix monitoring concepts:

* A [**host**](../monitoring-hosts/monitoring-host.md) is any device with an IP address that you want to monitor. For example, a physical server, a virtual machine, a temperature sensor, an IP camera, a printer, or a disk space.
* A [**service**](../monitoring-services/monitoring-service.md) is a checkpoint or indicator that you want to monitor on a host. This can be CPU utilization, temperature, motion detection, bandwidth utilization, disk I/O, and so on.
* To collect each indicator value, monitoring plug-ins are used, which are periodically executed by a collection engine called Centreon Engine.
* In order to be executed, a plugin needs a set of arguments that define, for example, which host to connect to or through which protocol.
  The plugin and its arguments form a [**command**](../../monitoring-resources/generic-object-actions/commands.md).

For example, to monitor a host with i-Vertix, configure all the commands needed to measure the desired indicators, and then [deploy that configuration](../../monitoring-resources/monitoring-basics/config-deploy.md) to the collection engine so that those commands are run periodically.

Once hosts and services are monitored, they have a [status](../../events-alerts/viewing-events/concepts.md) in i-Vertix (e.g. **OK**, **Warning**, **Critical**...). You can keep track of any changes using the [Resources Status](../../events-alerts/viewing-events/resources-status.md) page.

If a problem occurs (not-OK/not-UP status), [contacts](../../managing-users-contacts/contacts-users.md) can receive [notifications](../../events-alerts/managing-notifications/configuring-notification.md), within set [time periods](../../monitoring-resources/generic-object-actions/timeperiods.md).

In i-Vertix, monitoring is facilitated by the following elements:

- [Host templates](../../monitoring-resources/monitoring-hosts/host-templates.md) and [service templates](../../monitoring-resources/monitoring-services/service-template.md), which allow you to define defaults to speed up the creation of these objects.

- [Plugin Packs](../../monitoring-resources/monitoring-basics/plugin-packs.md), which provide out-of-the-box host and service templates. These greatly simplify the configuration of hosts and services: for example, you only need to apply Plugin Pack templates to a host in order to monitor it.

- The [Host and service auto-discovery](../../monitoring-resources/discovery/description), which allows you to obtain a list of new hosts and services and automatically add them to the list of monitored resources.
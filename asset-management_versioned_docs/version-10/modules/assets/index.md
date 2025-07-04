---
id: index
title: Index
---

# Assets

The i-Vertix ITAM Asset module is used to manage all the assets that are part of
your IT infrastructure.

## Asset management in i-Vertix ITAM

In order to manage hardwares and software of an IT infrastructure, i-Vertix ITAM
allows natively to list all the assets that are used inside the managed
organization.

However, it is possible to automate information pushing from the assets
thanks to the native inventory and i-Vertix ITAM Agent and third-party tools.

More information on the i-Vertix ITAM Agent can be found in its dedicated
[documentation](https://glpi-agent.readthedocs.io/en/latest/index.html).

:::info

If you have used Fusion Inventory in the past with i-Vertix ITAM, it is very
easy to migrate over to the i-Vertix ITAM Agent due to the native inventory
remaining compatible with the Fusion Inventory agent.

:::

i-Vertix ITAM also supports automatic inventory via multiple plugins including
but not limited to:

- The [Fusion   Inventory](https://github.com/fusioninventory/fusioninventory-for-glpi/)
  plugin transforms i-Vertix ITAM into an inventory server with the Fusion
  Inventory agents interfacing directly with the i-Vertix ITAM server.
- The [ocsinventoryng](https://github.com/pluginsi-Vertix ITAM/ocsinventoryng)
  plugin allow to synchronize the i-Vertix ITAM database with the [OCS Inventory   NG](http://www.ocsinventory-ng.org) inventory tool: the agents
  installed on the computers interface directly the the OCS Inventory NG
  server.

## Available types

::: 
computers displays softwares Network equipments \<network-equipments\>
peripherals printers cartridges consumables phones global
:::


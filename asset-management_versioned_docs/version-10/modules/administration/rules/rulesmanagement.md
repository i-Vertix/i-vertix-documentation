---
id: rulesmanagement
title: Rulesmanagement
---

# Rules

Export, import and duplication is possible for all rules. These
operations can be carried out globally from the main rules page or by
batch from the search engines for the various rules via massive actions.
These features are interesting for example in the context of switching
of rules from a pre-production environment to a production environment.

:::info

 export or import use a XML file format

:::

## Rules engine

i-Vertix ITAM contains a rules engine which enables a certain number of actions
and associations to be carried out automatically.

This engine is used for both:

- management rules:
  - assigning an asset to an entity
  - granting permissions to a user
  - assigning category to a software
  - routing tickets to entities
  - automatic actions when opening ticket
- [data dictionaries](../../../modules/administration/dictionnaries.md) :
  - manufacturers
  - software
  - printers
  - types of assets
  - models of assets
  - operating system related fields

The engine behaves differently depending on the types of rules:

- stop after first matching rule
- apply all rules
- apply rules and pass rule result to next rule

Rules can be disabled, for example when writing and testing new rules.
:::tip

in general, it is recommended to test the rules well before using them
and to make a backup before setting up each new rule. On the main form
of a rule, a *Test* button opens an additional window that allows to see
all the criteria and results of the rule.
:::

## The different rules

### Rules for assigning a ticket opened via a mail collector

See Rules for assigning a ticket opened via a mail collector

### Rules for assigning authorizations to a user

See
[Rules for assigning authorizations to a user](../../../modules/administration/rules/userauthorizations.md)

### Rules for assigning a category to software

Classification by category makes it easier to display and find software.
This can be done automatically for any new software, or retroactively.
The available criteria are the publisher, the name and the comment of
the software. The only possible action is to assign software to a
category. It is possible to replay the rules from the software list,
using massive action *Recalculate category*.

### Business rules for tickets

When opening or modifying a ticket, a mechanism allows to modify ticket
attributes automatically.

See
[Business rules for tickets](../../../modules/administration/rules/ticketbusinessrules.md)

### Rules for inventory agent

The two menus below are only visible if you use an inventory agent for
an automatic inventory of computers in i-Vertix ITAM.

- rules for assigning an item to an entity
- rules for importing and linking computers

See
[Rules for inventory agent](../../../modules/administration/rules/inventorytools.md)

- **Transfer** This menu allows you to define the inter-entity transfer
  profiles.

  Several actions are possible:

  - **Preserve**: the item will be transferred with the object;
  - **Put in Trash Bin**: the item will be placed in the recycle bin of
    the ceding entity;
  - **Delete Permanently**: the item will be deleted from the database;
  - **Keep**: the item will remain in the ceding entity;
  - **Disconnect**: the connection between element and object will be
    deleted

- **Blacklists** Thanks to the i-Vertix ITAM blacklist mechanism, it is possible
  to exclude certain values from processing by the rules engine. The
  types that can be taken into account are:

  - IP address;
  - MAC address;
  - serial number;
  - UUID;
  - email

  This allows, for example, to exclude certain IP addresses from the
  inventory agent (for example an IP 127.0.0.1 or 0.0.0.0) or not to
  create a ticket from a particular email address (for example daily
  backup of a server).

## Create a rule

A rule is composed of a series of criteria. Depending on the option
chosen (OR/ ND) one or all of the criteria must be verified to trigger
an action list.

A preview mechanism allows you to test the rules being written before
putting them into production.

Several criteria are available:

- simple:
  - is
  - is not
  - contains
  - does not contain
  - starts with
  - ends with
  - under (for tree dropdowns, indicates to be this dropdown or one of
    the child dropdowns)
  - not under (for tree dropdowns, indicates not to be this dropdown or
    one of the child dropdowns))
- complex:
  - regular expression match
  - regular expression does not match

Regular expressions (otherwise known as regex) return one or more
results which can then be used by actions using the \#x directive (where
x is the number of the result of the regular expression).
:::note[**Example**]

Criteria : name matching regular expression `/DESKTOP\_(.\*)/` If object
is named `DESKTOP_0001`, then it will be possible to use `0001` in the
actions of the rules using parameter `#0`
:::

**KEEP ?**

You need to create **location rules** to affect a location to a
computer. Before, you need to define the criteria which will trigger the
rule (a tag inventory, a subnet, a domain, etc.) In our example, we're
going to create a rule that takes the [inventory tag](https://glpi-agent.readthedocs.io/en/latest/man/glpi-agent.html#execution-mode-options)
into account. If the tag is France, then apply the Paris location

- In **administration \> Rules \> Location Rules**

- Click **+ Add**

- You can add different information (name, logical operator, comments,
  description, active)

:::warning

**Logical operator AND / OR**

- **"OR"** the rule will then apply from the 1st corresponding
criterion. It will ignore all subsequent criteria.
- **"AND"**, on the other hand, will have to take all the
criteria into account for the rule to be applied.

:::

- **Active** your rule

- Clik **+ Add**

- In **Criteria**, click **Add a new criterion**

- Select **Agent \> Inventory tag**

- Enter **France**

- Click **+ Add**

  > ![add rule location](../../../assets/tabs/common_fields/images/add-rule-location-criteria.png)

- In **Actions** tab, click **Add a new action**

- Select the location to assign

- Click **+ Add**

  > ![add rule location](../../../assets/tabs/common_fields/images/add-rule-location-action.png)

You can test the rule location by clicking on **Test rules engines** in
**Administration \> Locations rules**

![add rule location](../../../assets/tabs/common_fields/images/test-rule-location.png)

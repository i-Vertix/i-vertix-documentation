---
id: rest-api-v1
title: Rest API (v1)
---

## Overview

This documentation is for developers familiar with HTTP requests and JSON. It
explains various API operations, related requests and responses structure, and
error codes.

## Permissions

To perform API calls, you must be an administrator.

## Authentication

Using POST method and the URL below:

```text
api.domain.tld/centreon/api/index.php?action=authenticate
```

Body form-data:

| Parameter | Type | Value                          |
|-----------|------|--------------------------------|
| username  | Text | The user name you use to login |
| password  | Text | Your monitoring password       |

The response is a json flow getting back the authentication token :

```json
{
  "authToken": "NTc1MDU3MGE3M2JiODIuMjA4OTA2OTc="
}
```

This token will be used later on the other API actions.

## Error codes

| Code | Message                                                                                  |
|------|------------------------------------------------------------------------------------------|
| 200  | Successful                                                                               |
| 400  | Missing parameter / Missing name parameter  / Unknown parameter / Objects are not linked |
| 401  | Unauthorized                                                                             |
| 404  | Object not found / Method not implemented into Monitoring API                            |
| 409  | Object already exists / Name is already in use / Objects already linked                  |
| 500  | Internal server error (custom message)                                                   |

## Configuration

### Getting started

Here is an example for listing hosts using rest API.

Using POST method and the URL below:

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header:**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body:**

```json
{
  "action": "show",
  "object": "HOST"
}
```

- The key **action** corresponds to the option **-a** of the Monitoring commandline API, the
  value **show** corresponds to the **-a** option's value.
- The key **object** corresponds to the option **-o** of the Monitoring commandline API, the
  value **HOST** corresponds to the **-o** option's value.

The equivalent action using the Monitoring commandline API is:

```shell
centreon -u admin -p centreon -o HOST -a show
```

**Response:** The response is a json flow listing all hosts and formated as
below:

```json
{
  "result": [
    {
      "id": "12",
      "name": "mail-uranus-frontend",
      "alias": "mail-uranus-frontend",
      "address": "mail-uranus-frontend",
      "activate": "1"
    },
    {
      "id": "13",
      "name": "mail-neptune-frontend",
      "alias": "mail-neptune-frontend",
      "address": "mail-neptune-frontend",
      "activate": "1"
    },
    {
      "id": "14",
      "name": "srvi-mysql01",
      "alias": "srvi-mysql01",
      "address": "srvi-mysql01",
      "activate": "1"
    }
  ]
}
```

> Some actions need the values key (the option **-v** of the Monitoring commandline API).
> Depending on the called action, the body can contain **values** key. We will see
> that in detail later.

### API Calls

All API calls you can do on objects are described below. Note that you need to
be authenticated before each call.

API calls on the Host object are fully-detailed below. For the next objects,
only the actions available are listed, so just follow the same approach as for
the host object for an API call.

### Host

#### List hosts

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "show",
  "object": "host"
}
```

**Response**

```json
{
  "result": [
    {
      "id": "79",
      "name": "mail-uranus-frontend",
      "alias": "mail-uranus-frontend",
      "address": "mail-uranus-frontend",
      "activate": "1"
    },
    {
      "id": "80",
      "name": "mail-neptune-frontend",
      "alias": "mail-neptune-frontend",
      "address": "mail-neptune-frontend",
      "activate": "1"
    },
    {
      "id": "81",
      "name": "mail-earth-frontend",
      "alias": "mail-earth-frontend",
      "address": "mail-earth-frontend",
      "activate": "1"
    }
  ]
}
```

#### Add host

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "add",
  "object": "host",
  "values": "test;Test host;127.0.0.1;generic-host;central;Linux-SerVers"
}
```

**Response**

```json
{
  "result": []
}
```

#### Delete host

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "del",
  "object": "host",
  "values": "test"
}
```

**Response**

```json
{
  "result": []
}
```

#### Set parameters

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "setparam",
  "object": "host",
  "values": "test;ParameterToSet;NewParameter"
}
```

Available parameters

| Parameter                      | Description                                                            |
|--------------------------------|------------------------------------------------------------------------|
| 2d\_coords                     | 2D coordinates (used by statusmap)                                     |
| 3d\_coords                     | 3D coordinates (used by statusmap)                                     |
| geo\_coords                    | Geo coordinates (used by i-Vertix Maps)                                |
| action\_url                    | Action URL                                                             |
| activate                       | Whether or not host is enabled                                         |
| active\_checks\_enabled        | Whether or not active checks are enabled                               |
| acknowledgement\_timeout       | Acknowledgement timeout (in seconds)                                   |
| address                        | Host IP Address                                                        |
| alias                          | Alias                                                                  |
| check\_command                 | Check command                                                          |
| check\_command\_arguments      | Check command arguments                                                |
| check\_interval                | Normal check interval                                                  |
| check\_freshness               | Check freshness (in seconds)                                           |
| check\_period                  | Check period                                                           |
| checks\_enabled                | Whether or not checks are enabled                                      |
| contact\_additive\_inheritance | Enables contact additive inheritance                                   |
| cg\_additive\_inheritance      | Enables contactgroup additive inheritance                              |
| event\_handler                 | Event handler command                                                  |
| event\_handler\_arguments      | Event handler command arguments                                        |
| event\_handler\_enabled        | Whether or not event handler is enabled                                |
| first\_notification\_delay     | First notification delay (in seconds)                                  |
| flap\_detection\_enabled       | Whether or not flap detection is enabled                               |
| flap\_detection\_options       | Flap detection options                                                 |
| icon\_image                    | Icon image                                                             |
| icon\_image\_alt               | Icon image text                                                        |
| max\_check\_attempts           | Maximum number of attempt before a HARD state is declared              |
| name                           | Host name                                                              |
| notes                          | Notes                                                                  |
| notes\_url                     | Notes URL                                                              |
| notifications\_enabled         | Whether or not notification is enabled                                 |
| notification\_interval         | Notification interval                                                  |
| notification\_options          | Notification options                                                   |
| notification\_period           | Notification period                                                    |
| obsess\_over\_host             | Whether or not obsess over host option is enabled                      |
| passive\_checks\_enabled       | Whether or not passive checks are enabled                              |
| process\_perf\_data            | Process performance data command                                       |
| retain\_nonstatus\_information | Whether or not there is non-status retention                           |
| retain\_status\_information    | Whether or not there is status retention                               |
| retry\_check\_interval         | Retry check interval                                                   |
| snmp\_community                | Snmp Community                                                         |
| snmp\_version                  | Snmp version                                                           |
| stalking\_options              | Comma separated options: 'o' for OK, 'd' for Down, 'u' for Unreachable |
| statusmap\_image               | Status map image (used by statusmap                                    |
| host\_notification\_options    | Notification options (d,u,r,f,s)                                       |
| timezone                       | Timezone                                                               |

**Response**

```json
{
  "result": []
}
```

#### Get parameters

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "getparam",
  "object": "host",
  "values": "test;ParameterToGet|ParameterToGet"
}
```

Available parameters

| Parameter                      | Description                                                            |
|--------------------------------|------------------------------------------------------------------------|
| 2d\_coords                     | 2D coordinates (used by statusmap)                                     |
| 3d\_coords                     | 3D coordinates (used by statusmap)                                     |
| geo\_coords                    | Geo coordinates (used by i-Vertix Maps)                                |
| action\_url                    | Action URL                                                             |
| activate                       | Whether or not host is enabled                                         |
| active\_checks\_enabled        | Whether or not active checks are enabled                               |
| address                        | Host IP Address                                                        |
| alias                          | Alias                                                                  |
| check\_command                 | Check command                                                          |
| check\_command\_arguments      | Check command arguments                                                |
| check\_interval                | Normal check interval                                                  |
| check\_freshness               | Check freshness (in seconds)                                           |
| check\_period                  | Check period                                                           |
| checks\_enabled                | Whether or not checks are enabled                                      |
| contact\_additive\_inheritance | Enables contact additive inheritance                                   |
| cg\_additive\_inheritance      | Enables contactgroup additive inheritance                              |
| event\_handler                 | Event handler command                                                  |
| event\_handler\_arguments      | Event handler command arguments                                        |
| event\_handler\_enabled        | Whether or not event handler is enabled                                |
| first\_notification\_delay     | First notification delay (in seconds)                                  |
| flap\_detection\_enabled       | Whether or not flap detection is enabled                               |
| flap\_detection\_options       | Flap detection options                                                 |
| icon\_image                    | Icon image                                                             |
| icon\_image\_alt               | Icon image text                                                        |
| max\_check\_attempts           | Maximum number of attempt before a HARD state is declared              |
| name                           | Host name                                                              |
| notes                          | Notes                                                                  |
| notes\_url                     | Notes URL                                                              |
| notifications\_enabled         | Whether or not notification is enabled                                 |
| notification\_interval         | Notification interval                                                  |
| notification\_options          | Notification options                                                   |
| notification\_period           | Notification period                                                    |
| obsess\_over\_host             | Whether or not obsess over host option is enabled                      |
| passive\_checks\_enabled       | Whether or not passive checks are enabled                              |
| process\_perf\_data            | Process performance data command                                       |
| retain\_nonstatus\_information | Whether or not there is non-status retention                           |
| retain\_status\_information    | Whether or not there is status retention                               |
| retry\_check\_interval         | Retry check interval                                                   |
| snmp\_community                | Snmp Community                                                         |
| snmp\_version                  | Snmp version                                                           |
| stalking\_options              | Comma separated options: 'o' for OK, 'd' for Down, 'u' for Unreachable |
| statusmap\_image               | Status map image (used by statusmap                                    |
| host\_notification\_options    | Notification options (d,u,r,f,s)                                       |
| timezone                       | Timezone                                                               |

**Response**

```json
{
  "result": [
    {
      "alias": "test",
      "address": "192.168.56.101",
      "timezone": "Europe/Berlin"
    }
  ]
}
```

#### Set instance poller

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "setinstance",
  "object": "host",
  "values": "test;Poller-2"
}
```

**Response**

```json
{
  "result": []
}
```

#### Get macro

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "getmacro",
  "object": "host",
  "values": "mail-uranus-frontend"
}
```

**Response** Here is a response example :

```json
{
  "result": [
    {
      "macro name": "ALIVENUM",
      "macro value": "1",
      "is_password": "",
      "description": "",
      "source": "generic-host-bench"
    },
    {
      "macro name": "ALIVEWARNING",
      "macro value": "3000,80",
      "is_password": "",
      "description": "",
      "source": "generic-host-bench"
    },
    {
      "macro name": "ALIVECRITICAL",
      "macro value": "5000,100",
      "is_password": "",
      "description": "",
      "source": "generic-host-bench"
    }
  ]
}
```

#### Set macro

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "setmacro",
  "object": "host",
  "values": "mail-uranus-frontend;MacroName;NewValue"
}
```

To edit an existing custom macro, The MacroName used on the body should be
defined on the Custom Marco of the chosen host. If the marco doesn't exist, it
will be created.

**Response**

```json
{
  "result": []
}
```

#### Delete macro

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "delmacro",
  "object": "host",
  "values": "mail-uranus-frontend;MacroName"
}
```

The MacroName used on the body is the macro to delete. It should be defined on
the Custom Marco of the chosen host.

**Response**

```json
{
  "result": []
}
```

#### Get template

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "gettemplate",
  "object": "host",
  "values": "mail-uranus-frontend"
}
```

**Response** Here is a response example :

```json
{
  "result": [
    {
      "id": "3",
      "name": "Servers-Linux"
    },
    {
      "id": "62",
      "name": "Postfix-frontend"
    },
    {
      "id": "59",
      "name": "Cyrus-murder-frontend"
    }
  ]
}
```

#### Set template

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "settemplate",
  "object": "host",
  "values": "mail-uranus-frontend;MyHostTemplate"
}
```

The MyHostTemplate used on the body should exist as a host template. The new
template erase templates already exist.

**Response**

```json
{
  "result": []
}
```

#### Add template

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "addtemplate",
  "object": "host",
  "values": "mail-uranus-frontend;MyHostTemplate"
}
```

The MyHostTemplate used on the body should exist as a host template. The new
template is added without erasing template already linked

**Response**

```json
{
  "result": []
}
```

#### Delete template

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "deltemplate",
  "object": "host",
  "values": "mail-uranus-frontend;MyHostTemplate"
}
```

The MyHostTemplate used on the body should exist as a host template.

**Response**

```json
{
  "result": []
}
```

#### Apply template

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "applytpl",
  "object": "host",
  "values": "mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": []
}
```

#### Get parent

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "getparent",
  "object": "host",
  "values": "mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": [
    {
      "id": "219",
      "name": "mail-uranus-frontdad"
    }
  ]
}
```

#### Add parent

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "addparent",
  "object": "host",
  "values": "mail-uranus-frontend;fw-berlin"
}
```

**Response**

```json
{
  "result": []
}
```

To add more than one parent to a host, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;fw-berlin|fw-dublin"
}
```

The add action add the parent without overwriting he previous configuration.

#### Set parent

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "setparent",
  "object": "host",
  "values": "mail-uranus-frontend;fw-berlin"
}
```

**Response**

```json
{
  "result": []
}
```

To set more than one parent to a host, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;fw-berlin|fw-dublin"
}
```

The set action overwrite the previous configuration before setting the new
parent.

#### Delete parent

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "delparent",
  "object": "host",
  "values": "mail-uranus-frontend;fw-berlin"
}
```

**Response**

```json
{
  "result": []
}
```

To delete more than one parent, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;fw-berlin|fw-dublin"
}
```

#### Get child

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "getchild",
  "object": "host",
  "values": "mail-uranus-frontdad"
}
```

**Response**

```json
{
  "result": [
    {
      "id": "219",
      "name": "mail-uranus-frontchild"
    }
  ]
}
```

#### Add child

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "addchild",
  "object": "host",
  "values": "fw-berlin;mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": []
}
```

To add more than one child to a host, use the character `|`. Ex:

```json
{
  "values": "fw-berlin;mail-uranus-frontend|mail-neptune-frontend"
}
```

The add action add the child without overwriting the previous configuration.

### Set child

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "setchild",
  "object": "host",
  "values": "fw-berlin;mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": []
}
```

To set more than one child to a host, use the character `|`. Ex:

```json
{
  "values": "fw-berlin;mail-uranus-frontend|mail-neptune-frontend"
}
```

The set action overwrite the previous configuration before setting the new child.

### Delete child

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "delchild",
  "object": "host",
  "values": "fw-berlin;mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": []
}
```

To delete more than one child, use the character `|`. Ex:

```json
{
  "values": "fw-berlin;mail-uranus-frontend|mail-neptune-frontend"
}
```

#### Get contact group

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "getcontactgroup",
  "object": "host",
  "values": "mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": [
    {
      "id": "6",
      "name": "Mail-Operators"
    }
  ]
}
```

#### Add contact group

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "addcontactgroup",
  "object": "host",
  "values": "mail-uranus-frontend;Supervisors"
}
```

**Response**

```json
{
  "result": []
}
```

To add more than one contactgroup to a host, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;Supervisors|Guest"
}
```

The add action add the contact without overwriting he previous configuration.

#### Set contact group

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "setcontactgroup",
  "object": "host",
  "values": "mail-uranus-frontend;Supervisors"
}
```

**Response**

```json
{
  "result": []
}
```

To set more than one contactgroup to a host, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;Supervisors|Guest"
}
```

The set action overwrite the previous configuration before setting the new
contactgroup.

#### Delete contact group

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "delcontactgroup",
  "object": "host",
  "values": "mail-uranus-frontend;Guest"
}
```

**Response**

```json
{
  "result": []
}
```

To delete more than one contactgroup, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;Guest|Supervisors"
}

```  

#### Get contact

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "getcontact",
  "object": "host",
  "values": "mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": [
    {
      "id": "20",
      "name": "user-mail"
    }
  ]
}
```

#### Add contact

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "addcontact",
  "object": "host",
  "values": "mail-uranus-frontend;admin"
}
```

**Response**

```json
{
  "result": []
}
```

To add more than one contact to a host, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;admin|SuperAdmin"
}
```

The add action add the contact without overwriting he previous configuration.

#### Set contact

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "setcontact",
  "object": "host",
  "values": "mail-uranus-frontend;admin"
}
```

**Response**

```json
{
  "result": []
}
```

To set more than one contact to a host, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;admin|SuperAdmin"
}
```

The set action overwrite the previous configuration before setting the new
contact.

#### Delete contact

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "delcontact",
  "object": "host",
  "values": "mail-uranus-frontend;Guest"
}
```

**Response**

```json
{
  "result": []
}
```

To delete more than one contact, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;admin|SuperAdmin"
}
```

#### Get hostgroup

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "gethostgroup",
  "object": "host",
  "values": "mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": [
    {
      "id": "53",
      "name": "Linux-Servers"
    },
    {
      "id": "63",
      "name": "Mail-Cyrus-Frontend"
    }
  ]
}
```

#### Add hostgroup

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "addhostgroup",
  "object": "host",
  "values": "mail-uranus-frontend;Mail-Postfix-Frontend"
}
```

**Response**

```json
{
  "result": []
}
```

To add more than one hostgroup to a host, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;Mail-Postfix-Frontend|Linux-Servers"
}

```  

The add action add the hostgroup without overwriting he previous configuration.

#### Set hostgroup

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "sethostgroup",
  "object": "host",
  "values": "mail-uranus-frontend;Linux-Servers"
}
```

**Response**

```json
{
  "result": []
}
```

To set more than one hostgroup to a host, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;Linux-Servers|Mail-Postfix-Frontend"
}
```

The set action overwrite the previous configuration before setting the new
hostgroup.

#### Delete hostgroup

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "delhostgroup",
  "object": "host",
  "values": "mail-uranus-frontend;Linux-Servers"
}
```

**Response**

```json
{
  "result": []
}
```

To delete more than one hostgroup, use the character `|`. Ex:

```json
{
  "values": "mail-uranus-frontend;Linux-Servers|Mail-Postfix-Frontend"
}
```

#### Enable

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "enable",
  "object": "host",
  "values": "mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": []
}
```

#### Disable

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "disable",
  "object": "host",
  "values": "mail-uranus-frontend"
}
```

**Response**

```json
{
  "result": []
}
```

### ACL

- **Object**

    - ACL

**Actions**

    - reload
    - lastreload

#### Action ACL

- **Object**

    - ACLACTION

**Actions**

    - show
    - add
    - del
    - setparam
    - getaclgroup
    - grant
    - revoke

#### ACL groups

- **Object**

    - ACLGROUP

**Actions**

    - show
    - add
    - del
    - setparam
    - getmenu
    - getaction
    - getresource
    - getcontact
    - getcontactgroup
    - setmenu
    - setaction
    - setresource
    - addmenu
    - addaction
    - addresource
    - delmenu
    - delaction
    - delresource
    - setcontact
    - setcontactgroup
    - addcontact
    - addcontactgroup
    - delcontact
    - delcontactgroup

#### Menu ACL

- **Object**

    - ACLMENU

**Actions**

    - show
    - add
    - del
    - setparam
    - getaclgroup
    - grant
    - revoke

#### Resource ACL

- **Object**

    - ACLRESOURCE

**Actions**

    - show
    - add
    - del
    - setparam
    - getaclgroup
    - grant
    - revoke

### Centreon Broker

- **Object**

    - CENTBROKERCFG

**Actions**

    - show
    - add
    - del
    - setparam
    - listinput, listoutput, listlogger, listcorrelation, listtemporary, liststats
    - getinput, getoutput, getlogger, getcorrelation, gettemporary, getstats
    - addinput, addoutput, addlogger, addcorrelation, addtemporary, addstats
    - delinput, deloutput, dellogger, delcorrelation, deltemporary, delstats
    - setinput, setoutput, setlogger, setcorrelation, settemporary, setstats

### CGI CFG

- **Object**

    - CGICFG

**Actions**

    - show
    - add
    - del
    - setparam

### Commands

- **Object**

    - CMD

**Actions**

    - show
    - add
    - del
    - setparam

### Contacts

- **Object**

    - CONTACT

**Actions**

    - show
    - add
    - del
    - setparam
    - enable
    - disable

#### Contact templates

- **Object**

    - CONTACTTPL

**Actions**

    - show
    - add
    - del
    - setparam
    - enable
    - disable

#### Contact groups

- **Object**

    - CG

**Actions**

    - show
    - add
    - del
    - setparam
    - enable
    - disable
    - getcontact
    - addcontact
    - setcontact
    - delcontact

### Dependencies

- **Object**

    - DEP

**Actions**

    - show
    - add
    - del
    - setparam
    - listdep
    - addparent
    - addchild
    - delparent
    - delchild

### Downtimes

- **Object**

    - DOWNTIME

**Actions**

    - show
    - add
    - del
    - listperiods
    - addweeklyperiod
    - addmonthlyperiod
    - addspecificperiod
    - addhost, addhostgroup, addservice, addservicegroup
    - delhost, delhostgroup, delservice, delservicegroup
    - sethost, sethostgroup, setservice, setservicegroup

### Host template

- **Object**

    - HTPL

**Actions** APPLYTPL and SETINSTANCE actions on HTPL

    - show
    - add
    - del
    - setparam
    - getmacro
    - setmacro
    - delmacro
    - getparent
    - addparent
    - setparent
    - delparent
    - getcontactgroup
    - addcontactgroup
    - setcontactgroup
    - delcontactgroup
    - getcontact
    - addcontact
    - setcontact
    - delcontact
    - gethostgroup
    - addhostgroup
    - sethostgroup
    - delhostgroup
    - setseverity
    - unsetseverity
    - enable
    - disable

### Host categories

- **Object**

    - HC

**Actions**

    - show
    - add
    - del
    - getmember
    - addmember
    - setmember
    - setseverity
    - unsetseverity
    - delmember

### Hostgroups

- **Object**

    - HG

**Actions**

    - show
    - add
    - del
    - setparam
    - getmember
    - addmember
    - setmember
    - delmember

### Instances ( Pollers)

- **Object**

    - INSTANCE

**Actions**

    - show
    - add
    - del
    - setparam
    - gethosts

### Service templates

- **Object**

    - STPL

**Actions**

    - show
    - add
    - del
    - setparam
    - gethosttemplate
    - addhosttemplate
    - sethosttemplate
    - delhosttemplate
    - getmacro
    - setmacro
    - delmacro
    - getcontact
    - addcontact
    - setcontact
    - delcontact
    - getcontactgroup
    - setcontactgroup
    - delcontactgroup
    - gettrap
    - settrap
    - deltrap

### Services

- **Object**

    - SERVICE

**Actions**

    - show
    - add
    - del
    - setparam
    - addhost
    - sethost
    - delhost
    - getmacro
    - setmacro
    - delmacro
    - setseverity
    - unsetseverity
    - getcontact
    - addcontact
    - setcontact
    - delcontact
    - getcontactgroup
    - setcontactgroup
    - delcontactgroup
    - gettrap
    - settrap
    - deltrap

### Service groups

- **Object**

    - SG

**Actions**

    - show
    - add
    - del
    - setparam
    - getservice
    - gethostgroupservice
    - addservice
    - setservice
    - addhostgroupservice
    - sethostgroupservice
    - delservice
    - delhostgroupservice

### Service categories

- **Object**

    - SC

**Actions**

    - show
    - add
    - del
    - setparam
    - getservice
    - getservicetemplate
    - addservice
    - setservice
    - addservicetemplate
    - setservicetemplate
    - delservice
    - delservicetemplate
    - setseverity
    - unsetseverity

### Time periods

- **Object**

    - TIMEPERIOD

**Actions**

    - show
    - add
    - del
    - setparam
    - getexception
    - setexception
    - delexception

### Traps

- **Object**

    - TRAP

**Actions**

    - show
    - add
    - del
    - setparam
    - getmatching
    - addmatching
    - delmatching
    - updatematching

#### Vendors

- **Object**

    - VENDOR

**Actions**

    - show
    - add
    - del
    - setparam
    - generatetraps

#### Get business views

**POST**

```text
api.domain.tld/centreon/api/index.php?action=action&object=centreon_clapi
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Body**

```json
{
  "action": "show",
  "object": "bv"
}
```

**Response**

The response is a JSON flow listing all hosts, formated as follows: :

```json
{
  "result": [
    {
      "id_ba_group": "1",
      "name": "BA-Mail-View",
      "description": "BA Mail View"
    },
    {
      "id_ba_group": "2",
      "name": "BA-CIO-View",
      "description": "BA CIO View"
    }
  ]
}
```

## Realtime information

### Host Status

All monitoring information regarding hosts are available in through the Monitoring
API.

Using GET method and the URL below:

```text
api.domain.tld/centreon/api/index.php?object=centreon_realtime_hosts&action=list
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Parameters**

You can pass a list of parameters in order to select the data you want.

| Parameters  | values                                                                             |
|-------------|------------------------------------------------------------------------------------|
| viewType    | select the predefined filter like in the monitoring view: all, unhandled, problems |
| fields      | the fields list that you want to get separated by a ","                            |
| status      | the status of hosts that you want to get (up, down, unreachable, pending, all)     |
| hostgroup   | hostgroup id filter                                                                |
| instance    | instance id filter                                                                 |
| search      | search pattern applyed on host name                                                |
| criticality | a specific criticity                                                               |
| sortType    | the sortType (selected in the field list)                                          |
| order       | ASC ou DESC                                                                        |
| limit       | number of line you want                                                            |
| number      | page number                                                                        |

Field list :

| Fields                     | Description                              |
|----------------------------|------------------------------------------|
| id                         | host id                                  |
| name                       | host name                                |
| alias                      | host alias (description of the host)     |
| address                    | host address (domain name or ip)         |
| state                      | host state (UP = 0, DOWN = 2, UNREA = 3) |
| state\_type                | host state type (SOFT = 0, HARD = 1)     |
| output                     | Plugin output - state message            |
| max\_check\_attempts       | maximum check attempts                   |
| check\_attempt             | current attempts                         |
| last\_check                | last check time                          |
| last\_state\_change        | last time the state change               |
| last\_hard\_state\_change  | last time the state change in hard type  |
| acknowledged               | acknowledged flag                        |
| instance                   | name of the instance who check this host |
| instance\_id               | id of the instance who check this host   |
| criticality                | criticality fo this host                 |
| passive\_checks            | accept passive results                   |
| active\_checks             | active checks are enabled                |
| notify                     | notification is enabled                  |
| action\_url                | shortcut for action URL                  |
| notes\_url                 | shortcut for note URL                    |
| notes                      | note                                     |
| icon\_image                | icone image for this host                |
| icon\_image\_alt           | title of the image                       |
| scheduled\_downtime\_depth | scheduled\_downtime\_depth               |
| flapping                   | is the host flapping ?                   |

Using GET method and the URL below:

```text
api.domain.tld/centreon/api/index.php?object=centreon_realtime_hosts&action=list&limit=60&viewType=all&sortType=name&order=desc&fields=id,name,alias,address,state,output,next_check
```

### Service Status

All monitoring information regarding services are available through the
Monitoring API. With this call, you can also get host information in the same
time that service information. This web service provide the same possibility
that the service monitoring view.

Using GET method and the URL below:

```text
api.domain.tld/centreon/api/index.php?object=centreon_realtime_services&action=list
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Parameters**

You can pass a list of parameters in order to select the data you want.

| Parameters   | values                                                                                     |
|--------------|--------------------------------------------------------------------------------------------|
| viewType     | select the predefined filter like in the monitoring view: all, unhandled, problems         |
| fields       | the fields list that you want to get separated by a ","                                    |
| status       | the status of services that you want to get (ok, warning, critical, unknown, pending, all) |
| hostgroup    | hostgroup id filter                                                                        |
| servicegroup | servicegroup id filter                                                                     |
| instance     | instance id filter                                                                         |
| search       | search pattern applied on service                                                          |
| searchHost   | search pattern applied on host                                                             |
| searchOutput | search pattern applied on output                                                           |
| criticality  | a specific criticity                                                                       |
| sortType     | the sortType (selected in the field list)                                                  |
| order        | ASC ou DESC                                                                                |
| limit        | number of line you want                                                                    |
| number       | page number                                                                                |

Field list :

| Fields                     | Description                              |
|----------------------------|------------------------------------------|
| host\_id                   | host id                                  |
| host\_name                 | host name                                |
| host\_alias                | host alias (description of the host)     |
| host\_address              | host address (domain name or ip)         |
| host\_state                | host state (UP = 0, DOWN = 2, UNREA = 3) |
| host\_state\_type          | host state type (SOFT = 0, HARD = 1)     |
| host\_output               | Plugin output - state message            |
| host\_max\_check\_attempts | maximum check attempts for host          |
| host\_check\_attempt       | current attempts                         |
| host\_last\_check          | last check time                          |
| host\_acknowledged         | acknowledged flag                        |
| instance                   | name of the instance who check this host |
| instance\_id               | id of the instance who check this host   |
| host\_action\_url          | shortcut for action URL                  |
| host\_notes\_url           | shortcut for note URL                    |
| host\_notes                | note                                     |
| description                | service description - service name       |
| display\_name              | service display name                     |
| service\_id                | service id                               |
| state                      | service state                            |
| state\_type                | service state type (SOFT = 0, HARD = 1)  |
| output                     | service output returned by plugins       |
| perfdata                   | service perfdata returned by plugins     |
| current\_attempt           | maximum check attempts for the service   |
| last\_update               | last update date for service             |
| last\_state\_change        | last time the state change               |
| last\_hard\_state\_change  | last time the state change in hard type  |
| next\_check                | next check time for service              |
| max\_check\_attempts       | maximum check attempts for service       |
| action\_url                | shortcut for action URL                  |
| notes\_url                 | shortcut for note URL                    |
| notes                      | notes                                    |
| icone\_image               | icone image for service                  |
| passive\_checks            | accept passive results                   |
| active\_checks             | active checks are enabled                |
| acknowledged               | acknowledged flag                        |
| notify                     | notification is enabled                  |
| scheduled\_downtime\_depth | scheduled\_downtime\_depth               |
| flapping                   | is the host flapping ?                   |
| event\_handler\_enabled    | is the event-handfler enabled            |
| criticality                | criticality fo this service              |

Example:

Using GET method and the URL below:

```text
api.domain.tld/centreon/api/index.php?action=list&object=centreon_realtime_services&limit=60&viewType=all&sortType=name&order=desc&fields=id,description,host_id,host_name,state,output
```

### Submit results

You can use the monitoring API to submit information to the monitoring engine. All
information that you submit will be forwarded to the monitoring engine poller that
host the configuration.

The user must be admin or have access to "Reach API Configuration".

For the service submission please provide following information:

| Fields              | Description                                              |
|---------------------|----------------------------------------------------------|
| host                | host name                                                |
| service             | service description                                      |
| status              | status id (0, 1, 2, 3) or ok, warning, critical, unknown |
| output              | a specific message                                       |
| perfdata (optional) | all performance metric following the nagios plugin API   |
| updatetime          | the check time (timestamp)                               |

For the host submission please provide the following information :

| Fields     | Description                |
|------------|----------------------------|
| host       | host name                  |
| status     | status id (0, 1, 2, 3)     |
| output     | a specific message         |
| updatetime | the check time (timestamp) |

To send status, please use the following URL using POST method:

```text
api.domain.tld/centreon/api/index.php?action=submit&object=centreon_submit_results
```

**Header**

| Key                 | Value                                                         |
|---------------------|---------------------------------------------------------------|
| Content-Type        | application/json                                              |
| centreon-auth-token | The value of authToken you got on the authentication response |

**Example of service body submit:** The body is a json with the parameters
provided above formated as below:

```json
{
  "results": [
    {
      "updatetime": "1528884076",
      "host": "Central",
      "service": "Memory",
      "status": "2",
      "output": "The service is in CRITICAL state",
      "perfdata": "perf=20"
    },
    {
      "updatetime": "1528884076",
      "host": "Central",
      "service": "fake-service",
      "status": "1",
      "output": "The service is in WARNING state",
      "perfdata": "perf=10"
    }
  ]
}
```

**Example of body response** The response body is a json with the HTTP
return code and a message for each submit

```json
{
  "results": [
    {
      "code": 202,
      "message": "The status send to the engine"
    },
    {
      "code": 404,
      "message": "The service is not present."
    }
  ]
}
```

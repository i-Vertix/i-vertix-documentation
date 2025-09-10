---
id: forms
title: Forms
---

# Forms

Since i-Vertix ITAM 11, forms are native, so the formcreator plugin is no longer
required. Forms must be migrated from formcreator to forms.

## Migration formcreator to forms

:::warning

Form migration must be done from the i-Vertix ITAM 10 database. It is not
possible to import forms from i-Vertix ITAM 10 to i-Vertix ITAM 11.

:::

When migrating your instance to i-Vertix ITAM 11, the formcreator plugin must be
installed. Once the migration is complete, enter the command in
`CLI` mode from your i-Vertix ITAM folder:

`php bin/console migration:formcreator_plugin_to_core`

## Forms by default

There are two pre-created forms by default:

- Report an issue
- Request a service

![view home self-service profile](../../../assets/modules/administration/forms/images/forms_view_self-service.png)

These 2 forms are accessible to everyone. They can be
deactivated/deleted/modified

## List of forms

The list of forms is available from **Administration** \> **Forms**.
They will also be visible from **Assistance** \> **Service catalog**.
This tab refers to the self-service profile home page (see
`Service catalog</modules/assistance/service-catalog>`).

![List of forms](../../../assets/modules/administration/forms/images/forms_list.png)

## Forms options

When creating a form (by **+ Add**), several options will be available
to customize and facilitate the user experience as much as possible.

![Add a new form](../../../assets/modules/administration/forms/images/add_form.png)

### Customize the formatting

Tools are available to customize the organization of the forms

![Customize the formatting](../../../assets/modules/administration/forms/images/custom_formatting.png)

1.  Add a new question
2.  Add a comment
3.  Add a new section
4.  Add an horizontal layout

You can move the questions to reorganize the form

![Reorganize your forms](../../../assets/modules/administration/forms/images/move_question.png)

There are tools to reorganize an entire section

![Option for sections](../../../assets/modules/administration/forms/images/section_option.png)

### Basic information

- Modify the form's title in the **Underlined form** file (this title
  will be visible to people with access to the form)
- Add a **description** to simplify the use of the form (this
  description will be visible to people with access to the form)

### Add questions

Each question has its own **title** field (identified by new question)
and will be **visible to the user**. Each question **can be made
mandatory** so that the user must fill in the field to validate the form

There are actually several possible question types:

- **Short answer**: Text field with limited length and no formatting
  (bold, italics, color, etc.).

![Short answer option](../../../assets/modules/administration/forms/images/short_answer.png)

This field has additional options:

- *Text*: Allows you to enter text (alphanumeric)
- *Emails*: Allows you to enter email addresses only
- *Number*: Allows you to enter numeric characters only
- **Long answer**: field limited to 65,535 characters. The formatting of
  this field can be customized by the user (bold, italic, color, etc.)

![Long answer option](../../../assets/modules/administration/forms/images/long_answer.png)

- **Date and time**: a date and/or time

![Date and time option](../../../assets/modules/administration/forms/images/date_and_time.png)

This field has additional options:

- *Current date/time*: Use the current date and/or time and not allow
  the user to change it (leave the box unchecked to allow the user to
  specify the date/time they want).
- *Date*: Specify the date only (without the time).
- *Time*: Specify the time of day.

<!-- -->

- **Actors**: add one or more users/groups/suppliers referenced in i-Vertix ITAM

![Actors option](../../../assets/modules/administration/forms/images/actors.png)

This field has additional options:

> - *Requesters / Observers / Assignees*: each users / groups /
>   suppliers that will be added will be pre-filled in the ticket
>   according to the type of actor that will be chosen. A
>   user/group/provider can be preselected that the user can modify or
>   not
> - *Allow multiple actors*: allow multiple selections (allows groups,
>   users and suppliers in the same field)
>
:::warning

If you want to allow the user to select multiple actor types, you
will need to create as many questions as desired actors. An actor
question can only contain one actor type.

:::

- **Urgency**: add an urgency (very low, low, medium, high, very high)

![Urgency option](../../../assets/modules/administration/forms/images/urgency.png)

- **Request type**: select the type of request (incident or request)

![Request type option](../../../assets/modules/administration/forms/images/request_type.png)

- **Document**: add a document

![Document option](../../../assets/modules/administration/forms/images/document.png)

- **Radio**: set up a response list. The user will only be able to
  select one response.

An additional description can be added to make it easier for the user to
choose.

![Radio option](../../../assets/modules/administration/forms/images/radio.png)

- **Checkbox**: set up a response list. The user will be able to select
  multiple answers.

An additional description can be added to make it easier for the user to
choose.

![Checkbox option](../../../assets/modules/administration/forms/images/checkbox.png)

- **Dropdown**: set up a drop-down list to select one or more answers

![Dropdown option](../../../assets/modules/administration/forms/images/dropdown.png)

This field has an additional option:

> - *Allow muliple options*

- **Item**: Allows you to select differents i-Vertix ITAM's objects

![Item option](../../../assets/modules/administration/forms/images/item.png)

This field has additional options

**Users devices**: allows the user to select their own assets

**i-Vertix ITAM Objects** available :

::: 
Assets

- Computers
- Monitors
- Network devices
- Peripherals
- Phones
- Printers
- Licenses
- Certificates
- Unmanaged assets
- Appliances
- Software
- Cartridge models
- Consumable models
- Lines
- Passive devices
- PDUs
:::

::: 
Assistance

- Tickets
- Changes
- Problems
- Recurrent tickets
:::

::: 
Management

- Budgets
- Suppliers
- Contacts
- Contracts
- Documents
- Projects
- Certificates
- Appliances
- Databases
:::

::: 
Tools

- Reminders
- RSS Feed
:::

::: 
Administration

- Users
- Groups
- Entities
- Profiles
:::

**Dropdowns** available:

::: 
Common

- Locations
- Statuses of items
- Manufacturers
- Blacklists
- Blacklisted mail content
- Default filters
:::

::: 
Assistance

- ITIL category
- Task categories
- Task templates
- Solution types
- Solutions templates
- Approval templates
- Request sources
- Followup templates
- Project states
- Project types
- Project tasks types
- Project tasks templates
- External events templates
- Event categories
- Pending reason
- Service catalog categories
- Approval steps
:::

::: 
Type

- Computer types
- Networking types
- Printer types
- Monitor types
- Devices types
- Phone types
- License types
- Cartrige types
- Consumable types
- Contract types
- Contact types
- Generic types
- Sensor types
- Memory types
- Third party types
- Interface types (Hard drive...)
- Cases types
- Phone power supply types
- Files systems
- Certificate types
- Budget types
- Simacard types
- Line types
- Rack types
- PDU types
- Passive device types
- Cluster types
- Database instance type
:::

::: 
Models

- Computer models
- Networking models
- Printer models
- Monitor models
- Peripheral models
- Phone models
- Device camera models
- Device case models
- Device control models
- Device drive models
- Device generic models
- Device graphic card models
- Device hard drive models
- Device memory models
- System board models
- Other component models
- Device power supply models
- Device processor models
- Device sound card models
- Device sensor models
- Rack models
- Enclosure models
- PDU models
- Passive device models
:::

::: 
Virtual machines

- Virtualization systems
- Virtualization models
- States of the virtual machine
:::

::: 
Maangement

- Document heading
- Document types
- Business criticies
- Databse instance categories
:::

::: 
Tools

- Knowledge base categories
:::

::: 
Calendars

- Calendars
- Close times
:::

::: 
Operating systems

- Operating systems
- Versions of the operating systems
- Service packs
- Operating systems architectures
- Editions
- Kernels
- Kernels versions
- Update sources
:::

::: 
Networking

- Networking interfaces
- Networks
- Network port types
- VLANs
- Line operators
- Domain types
- Domain relations
- Records types
- Fiber types
:::

::: 
Cable management

- Cables types
- Cable strands
- Socket models
:::

::: 
Internet

- IP networks
- Internet domains
- Wifi networks
- Networks names
:::

::: 
Software

- Software categories
:::

::: 
User

- Users titles
- User categories
:::

::: 
Authorizations assignment rules

- LDAP criteria
:::

::: 
Fields unicity

- Ignored values for the unicity
:::

::: 
External authentications

- Fields storage of the login in the HTTP request
:::

::: 
Power management

- Plugs
:::

::: 
Appliance

- Appliance types
- Appliance environments
:::

::: 
Camera

- Resolutions
- Image formats
:::

::: 
Others

- USB vendors
- PCI vendors
- Webhook categories
:::

### Configure visibility

Visibility conditions can be specified for a question based on the
answer to a previous question.

For example, a user reports an issue with a printer. Depending on the
location (question type **Item** \> **Dropdowns** \> **Common -
Locations**), the form could be conditional on displaying only a list of
printers linked to that location.

![Configure the visibility](../../../assets/modules/administration/forms/images/answer_visibility.png)

You can indicate whether the question should be shown or hidden based on
chosen criteria.

![Choose your condition](../../../assets/modules/administration/forms/images/which_question.png)

The available condition types:

- *Always visible*
- *Visible if...*
- *Hidden if...*

Select the question from the drop-down list

Select the condition:

- *Is visible*
- *Is note visible*
- *Is equal to*
- *Is not equal to*
- *Contains*
- *Do not contains*
- *Match regular expression*
- *Do not match regular expression*

Enter the desired value as needed.

### Conditionnal Approval

It is possible to set conditional Approval (only on short/longer answer
fields) using a `Regular expression`.
This forces the user to enter a conditional answer, such as a certain
number of digits, a maximum of 30 characters, etc.

In this example, the expected response is a sequence of 6 numbers

If the entered answer is not suitable, a red error message will appear
during Approval.

### Submit button visibility

To ensure that the form is filled in as accurately as possible, it is
also possible to specify conditions for the visibility of a form. If
certain conditions are not met, the send button will not be visible and
the user will not be able to submit the form.

This can be used, for example, to prevent a field with a default choice
from being left blank even though it is mandatory.

Conditions can be created using the logical AND/OR operators.

![Submit button visibility](../../../assets/modules/administration/forms/images/submit_button_visibility.png)

## Service catalog

The service catalog allows you to make a form visible in the
**Assistance** \> **Service catalog** tab and from the home page of a
self-service portal

![View service catalog](../../../assets/modules/administration/forms/images/service_catalog.png)

### Customization

You can add:

- A description that will be visible on the form tile
- An illustration (from a catalog or you can upload one)

![Add an illustration of the catalog](../../../assets/modules/administration/forms/images/illustation_form.png)

![Add a custom illustration](../../../assets/modules/administration/forms/images/custom_illustration_form.png)

### Category

You can create a category (and child-categories) to make it easier to
select a form (e.g., all IT forms, all HR forms, etc.)

![Add a form's category](../../../assets/modules/administration/forms/images/form_category.png)

You can select the category in the dropdwon list or create a new one by
clicking on **+**

:::tip

Categories are manage in **Setup** \> **Drowpdowns** \> **Service
catalog**

:::

It is also possible to pin the form in the service catalog (with or
without category) so that it is available directly to users

## Access control

Access control allows you to determine who can use the form. It can be
public or private, visible to users, groups, or profiles.

![Access control view](../../../assets/modules/administration/forms/images/access_control.png)

:::warning

If you need to specify a visibility condition from an entity, you
simply need to create the form in the desired entity

:::

### Public access

Public access allows all users with the form link to access it in order
to submit their request. If you check the `allow unauthenticated users`
box, you can also allow users who do not have a i-Vertix ITAM account to use the
form.

:::tip

If the `allow unauthenticated users` box is checked, authenticated
users will no longer see this form

:::

### Private access

Private access allows you to filter the visibility of the form. It can
be conditioned to users and/or groups and/or profiles. Multiple
selection is allowed.

If all users should have access to the form, you can use the all users
option in the drop-down list.

:::tip

When your selection is complete, you will be able to see the list of
people who have access to the form

![List of users allowed to see the form](../../../assets/modules/administration/forms/images/matching_criteria.png)

:::

If you see this message, This means that unauthenticated users are not
allowed to see certain i-Vertix ITAM objects contained in certain questions. You
must then check the question(s) in order to modify them and avoid an
error when submitting the form by unauthenticated users.

![Error form](../../../assets/modules/administration/forms/images/error_form.png)

## Item to create

This tab allows you to customize the various fields of the item to be
created (entity, priority, actors, etc.).

You can create various items from the form:

- Tickets
- Changes
- Problems

You can allow the creation of multiple items from the same form.

### Conditions

It is possible to specify creation conditions.

For example, if the user answers **yes** to the question, "\*\*Is this
problem recurring?\*\*", the form could create a problem instead of a
ticket.

![Condition's creation of item](../../../assets/modules/administration/forms/images/condition_creation.png)

You need to click on **Always created** to create one or more
conditions.

### Custom fields

It is possible to customize the content of the item that will be
created. By default, **autoconfig** is selected. This will include all
questions/answers in the ticket that will be created.

![Custom content of item](../../../assets/modules/administration/forms/images/custom_content_item.png)

By clicking on `#` you can add answers for existing questions or delete
them.

A formatting menu is available to improve the rendering display.

### Followup / Task / Approval 

For each item created, you can add a follow-up, a task or request an
approval

For **followup** and **task**, you can:

- Not indicate one
- Choose from the template list
- Create a new template that you can then select

For Approval, you can:

- Not indicate one
- Add a specific actor (user, group or supplier, multiple selection is
  allowed)
- Answer from specific questions (a question with a user object is
  required in the form)

## Custom

You can customize the various fields of the item to be created
(properties, actors, service levels, associated items).

### Properties

:::warning

Please note that if business rules for tickets/changes/problems are
implemented, some information may be modified.

:::

#### Template

You can choose a specific template to automatically implement certain
elements. For more information, go to
[template](https://glpi-user-documentation.readthedocs.io/fr/latest/modules/overview/templates.html#ticket-templates)

:::warning

Only unfilled elements will be included via a template. The template
never takes precedence over field filling.

:::

#### Entity

Choose a specific entity in which the ticket must be created. A possible
choice among several proposals:

- **Active in entity of the form filler**: uses the entity in which the
  user creates their ticket
- **From form**: uses the entity in which the form was created
- **Specific entity**: manually select the desired entity
- **Answer from a specific question**: if a question with the entity
  object is asked, forms will use that answer. If no such question is
  asked or the answer remains empty, forms will use the option
- **Answer to last "Entity" item question**: if multiple entity
  questions are asked, forms will use the last entity object type
  question. If no such question is asked or the answer remains empty,
  forms will use "active entity of the form filler". The entities
  offered in the form will be only those to which the user is authorized

#### Request type

Allows you to select the ticket type (incident or request):

- **From template**: if a template is selected, the forms will use the
  requested types entered
- **Specific request type**: select request or incident
- **Answer from a specific question**: uses the answer to the question
  regarding the request type. If no question exists or the answer
  remains empty, forms will use **incident** by default
- **Answer to last Request type" question**: if multiple questions of
  the request type are asked, forms will use the last question. If no
  question exists or the answer remains empty, forms will use
  **incident** by default

#### ITIL Category

Allows you to select a specific category:

- **Specific category**: choose a category that already exists in the
  dropdown list
- **Answer from a specific category**: uses the answer to the question
  referring to the category. If no question is asked or the answer
  remains empty, the category will not be populated.
- **Answer to last "ITIL Category" dropdown question**: if multiple
  questions of ITIL category are asked, forms will use the last
  question. If no question exists or the answer remains empty, the
  category will not be entered

#### Status

Define the status of the ticket:

- **Default**: use the behavior by default (**new** if no actor is
  assigned, **processing (assigned)** if a actor is assigned,
  **processing (planned)** if a task is scheduled)
- **Closed**: ticket will be directly closed

#### Request source

- **From template**: use the template's specific source. The template
  uses the default value specified in **Setup** \> **General** \>
  **Assistance** \> **Request sources by default**
- **From a specific source**: select a source from the dropdown list

#### Urgency

- **From template**: if a template is selected, the forms will use the
  urgency entered. If no emergency is entered, this field will remain
  empty
- **Specific urgency**: select the urgency from the dropdown list
- **Answer from a specific question**: uses the answer to the question
  referring to the urgency. If no question is asked or the answer
  remains empty, the emergency will not be entered
- **Answer to last "Urgency" question**: if multiple questions of
  urgency are asked, forms will use the last question. If no question
  exists or the answer remains empty, the urgency will not be entered

#### Location

- **From template**: if a template is selected, the forms will use the
  location entered. If no location is entered, this field will remain
  empty
- **Specific location**: select the location from the dropdown list.
- **Answer from a specific question**: uses the answer to the question
  referring to the location. If no question is asked or the answer
  remains empty, the location will not be entered
- **Answer to last "Location" dropdown question**: if multiple
  questions of loaction are asked, forms will use the last question. If
  no question exists or the answer remains empty, the location will not
  be entered

### Actors

#### Requesters / Observers / Assignees 

:::tip

For each type of actor, it is possible to combine several criteria by
clicking on **+ Combine with another option**

![Combine option with another option](../../../assets/modules/administration/forms/images/combine_options.png)

:::

- **User who filled the form**
- **Supervisor of the user who filled the form**: use the person entered
  as supervisor in **Administration** \> **Users** \> *User* \>
  **Supervisor** If no supervisor is entered, the **User who filled the
  form** option will apply
- **From template**: if a template is selected, the forms will use the
  user entered. If no user is entered, the **User who filled the form**
  option will apply
- **Specific actors**: select user/group/supplier in the dropdwon list.
  Mutliple selection is allowed
- **Answer from a specific questions**: use the actor of the question
  that uses a users object. If no user is entered, the **User who filled
  the form** option will apply
- **Answer from the last "Requesters" question**: if multiple
  questions of user are asked, forms will use the last question If no
  question exists or the answer remains empty, the **User who filled the
  form** option will apply
- **User from i-Vertix ITAM object answer**: this option is used to retrieve the
  user assigned to an asset (asset **user** field). A question of type
  *object i-Vertix ITAM* \> *asset* must therefore be present
- **Tech from i-Vertix ITAM object answer**: this option is used to retrieve the
  technician assigned to an asset (asset **technician in charge**
  field). A question of type *object i-Vertix ITAM* \> *asset* must therefore be
  present
- **Group from i-Vertix ITAM object answer**: this option is used to retrieve the
  group assigned to an asset (asset **group** field). A question of type
  *object i-Vertix ITAM* \> *asset* must therefore be present
- **Tech group from i-Vertix ITAM object answer**: this option is used to
  retrieve the group(s) of technician assigned to an asset (asset
  **group in charge** field). A question of type *object i-Vertix ITAM* \>
  *asset* must therefore be present. If multiple groups are present in
  the field, they will all be assigned to the ticket

### Service levels

#### `TTO` / `TTR` / Internal TTO / Internal TTR 

- **From template**: if a template is selected, the forms will use the
  SLA entered. If no SLA is entered, this field will remain empty
- **Specific location**: select the SLA from the dropdown list

### Associated items

Items include:

- Computers
- Databases
- Enclosures
- Monitors
- Network devices
- Peripherals
- Phones
- Printers
- Rack
- Server rooms
- Software

**Possible choices**:

- **Specific items**: select the item from the dropdown list.
- **Answer from a specific questions**: use the item of the question
  that uses an item object. If no item is entered, the item will not be
  entered
- **Answer from the last assets item question**: if multiple questions
  of item are asked, forms will use the last question If no question
  exists or the answer remains empty, the item will not be entered
- **All valid "Item" answers**: includes all valid items entered

## Form translations

You can translate your forms. Displaying the form in another language is
based on the language set in the user's preferences.

When you click on **+Add language**, you can select the language you
want to translate your form.

![Add a a new translation](../../../assets/modules/administration/forms/images/add_translation.png)

Each field is displayed in the language the form was created in, along
with another translation field.

![Update the translation](../../../assets/modules/administration/forms/images/translated_form.png)

A progress bar shows you the progress of the form translation

![Progress of the form translation](../../../assets/modules/administration/forms/images/translation_progress.png)

## Import / Export 

Forms allows exporting and importing forms between instances of i-Vertix ITAM.

:::warning

This feature is designed to let administrators develop forms on a
testing environment and copy them on a production environment.

:::

### Export

To export forms, you need to use the massive actions

![Export forms](../../../assets/modules/administration/forms/images/export_forms.png)

### Import

To import forms, you need to click on **Import Forms** at the top of the
screen

![Import forms](../../../assets/modules/administration/forms/images/import_forms.png)

If your import is correct, you can click on import

![Import correct](../../../assets/modules/administration/forms/images/import_ok.png)

#### Import behavior

Forms allows field reconciliation. If some information is missing
(entity, user, group, etc.) from the instance where the form is
imported, Forms will offer you to either select a different existing
value or create a new value for each field in conflict. Click on
"Resolve issues" to display the conflicts.

![Preview after incorrect import](../../../assets/modules/administration/forms/images/preview_import.png)

1.  displays the field found during import
2.  the value with which you wish to replace it

![Form reconciliation](../../../assets/modules/administration/forms/images/reconciliation.png)

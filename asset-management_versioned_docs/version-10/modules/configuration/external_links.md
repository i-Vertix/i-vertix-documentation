---
id: external_links
title: External Links
---

# External links

Some elements of i-Vertix ITAM can be associated with a set of links to external
applications. These are visible from the **Links** tab of the various
forms.

## Add an external link

- Click on **+ Add**
- Enter a **name**
- Enter an **URL**
- Choose your **icon**
- You can choose to open it in a **different tab**

![Add external link](../../assets/modules/tabs/images/external_link_add.png)

From a i-Vertix ITAM object, select the newly created link so that it appears in
the Links tab.

![View external link](../../assets/modules/tabs/images/external_link_view.png)

## Add an "generic" external link

You can add a generic link for all elements of a i-Vertix ITAM object.

- In the **links** tab of your objet, click on **Configure XXXXXXXX
  links** (or go to **Setup** \> **External Links**)
- Click on **+ Add**

To setup a link, it is possible to use tags which will be replaced by
the values of the element. External links now use Twig templates.
Existing links will be converted automatically during the upgrade to
i-Vertix ITAM 11, but new links need to use Twig syntax. \*NAME\* -\> }.

The tags are :

<table>
<thead>
<tr>
<th>}</th>
<th>The logged in user's username</th>
</tr>
</thead>
<tbody>
<tr>
<td>}</td>
<td><blockquote>
<p>The internal numeric ID for the item</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The name of the item</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The name of the item's location</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The internal numeric ID for the item's location</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The IP address of the item</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The MAC address of the item</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The item's network</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The item's domain. If more than one domain is associated with the
item, the first one is used</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The item's serial number</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The item's inventory number/asset tag</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The item's user</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>The item's group</p>
</blockquote></td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td>The user's first name (Only applies to User external links)</td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td>The user's surname (Only applies to User external links)</td>
</tr>
<tr>
<td><hr /></td>
<td><hr /></td>
</tr>
<tr>
<td>}</td>
<td><blockquote>
<p>If the field you want is not available as a separate tag, it may
still be possible to use it by referencing its internal field name</p>
<p>For example, the comment field would be <span
class="title-ref">}</span> The field name is case
sensitive and typically it will need to be all lowercase.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Each link can be associated with one or more element types.

If the content is empty, a simple link will be generated. If content is
present, it is a link to the download of the content that will be
generated.

### Example

#### For remote access on computer

- Create an external protocol link with the name link with the name [}.rdp]
- Set the **file content** by inserting the content of an RDP type file
  and replacing the ip / name / domain by TAGS like }, },
  }. (To obtain the contents of an RDP file, open it with a
  notepad-type tool)

![Add an external RDP Link](../../assets/modules/configuration/images/external_link_rdp.png)

:::info

When using tags from network ports (IP, MAC), if the hardware has
several, then this will create as many create as many links as there
are ports. For example, for a machine with 2 different IP addresses, 2
links will be displayed.

:::

### A web type link

Create an external protocol link with the name
[https://}] and assign it to the network hardware.

### Remote control through a VNC extension

Some VNC implementations provide an extension that allows to take
control of a computer through a browser. In general, the port used is
5900. The corresponding link will be of type
[https://}:5900] or
[https://}.}:5900].

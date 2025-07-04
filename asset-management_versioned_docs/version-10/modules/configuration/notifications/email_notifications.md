---
id: email_notifications
title: Email_Notifications
---

# Email follow-ups configuration

For i-Vertix ITAM to be able to send notification via email, an email server
connection will need configured.

The email server configuration can be configured globally, and then some
options can be overridden at the entity level.

Global settings can be accessed from the "Email followups
configuration" option on the **Setup \> Notifications** page.

## Global Configuration

The global configuration allows you to set the following options:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr>
<td><blockquote>
<p><strong>Option</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Meaning</strong></p>
</blockquote></td>
</tr>
<tr>
<td><span class="title-ref">Administrator email</span></td>
<td><div class="line-block">i-Vertix ITAM Administrator email.<br />
This can be used as a special recipient in notifications</div></td>
</tr>
<tr>
<td><span class="title-ref">Administrator name</span></td>
<td>The display name to use for the Administrator email address.</td>
</tr>
<tr>
<td><span class="title-ref">From email</span></td>
<td>The email address to use in the From field for emails sent by
i-Vertix ITAM.</td>
</tr>
<tr>
<td><span class="title-ref">From name</span></td>
<td><div class="line-block">The display name to use for the From email
address.<br />
This name will be seen by end users.</div></td>
</tr>
<tr>
<td><span class="title-ref">Reply-to address</span></td>
<td>The email address to use when user's reply to the email
notifications.</td>
</tr>
<tr>
<td><span class="title-ref">Reply-to name</span></td>
<td>The display name to use for the Reply-to email address.</td>
</tr>
<tr>
<td><span class="title-ref">No-Reply address</span></td>
<td>The email address to use for emails that shouldn't be responded
to.</td>
</tr>
<tr>
<td><span class="title-ref">No-Reply name</span></td>
<td>The display name to use for the No-Reply email address.</td>
</tr>
<tr>
<td><blockquote>
<div class="line-block"><span class="title-ref">Add documents
into</span><br />
<span class="title-ref">ticket notifications</span></div>
</blockquote></td>
<td><div class="line-block">If enabled, documents attached to a ticket
will be added<br />
to related notifications as links.<br />
The links will use the i-Vertix ITAM URL specified in the general
configuration.</div></td>
</tr>
<tr>
<td><span class="title-ref">Email signature</span></td>
<td>Text added at the end of every notification.</td>
</tr>
<tr>
<td><span class="title-ref">Way of sending emails</span></td>
<td>Method to send emails (PHP, SMTP, SMTP+SSL, SMTP+TLS).</td>
</tr>
<tr>
<td><span class="title-ref">Max delivery retries</span></td>
<td>Number times i-Vertix ITAM will try to send a notification.</td>
</tr>
<tr>
<td><span class="title-ref">Try to deliver again in
(minutes)</span></td>
<td>Time between notification delivery attempts.</td>
</tr>
</tbody>
</table>

You can test the sending of notifications from the global notification
configuration form by trying to send an email to the specified
Administrator email address.

## Email Method - PHP

This option cannot be configured within i-Vertix ITAM and must be done in your
PHP configuration. This option uses the [mail()] function of
PHP.

:::info

The PHP email method is blocked by most hosting providers.

:::

## Email Method - SMTP

The following configuration options are available for the
[SMTP] email method(s):

- Check certificate - Verify the email server has a valid certificate.

- SMTP host - The SMTP server address.

- 

  Port - The port to communicate with the SMTP host over.

  :   Typically, this is port 25. Check your provider's documentation
      for more info.  
      Also, additional configuration may be needed if your provider
      needs [IMAP       OAuth](https://glpi-plugins.readthedocs.io/en/latest/oauthimap/index.html).

- SMTP login (optional) - Username to authenticate with the email
  server.

- SMTP password (optional) - Password to authenticate with the email
  server.

- 

  Email sender - This may be needed for some email providers.

  :   If this is not specified, the Administrator email will be used.

## Email Method - SMTP+SSL

The configuration options are the same as the [SMTP] option
but i-Vertix ITAM will use [SSL] security for the connection.

## Email Method - SMTP+TLS

The configuration options are the same as the [SMTP] option
but i-Vertix ITAM will use [TLS] security for the connection.

## Entity Configuration

The following options can be overridden at an entity level (see global
configuration for more information about each option): - Administrator
email - Administrator name - Reply-to address - Reply-to name - Email
signature

The entity level options can be accessed for the **Notifications** tab
in the entity's form.

The following options can only be configured at the entity level:

- [Prefix for notifications] - Text to prefix to the subject
  of email notifications.
- [Delay to send email notifications] - Optional delay to
  the initial sending of notifications.
- [Enable notifications by default] - If enabled, a user is
  automatically set to receive notifications in some cases such as when
  they are assigned to a ticket.

Fields that are no set, will be inherited from their parent entity by
default.

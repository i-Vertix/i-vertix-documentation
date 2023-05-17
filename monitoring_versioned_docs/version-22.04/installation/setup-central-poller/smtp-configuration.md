---
id: smtp-configuration
title: SMTP configuration
---

Email notifications settings can be configured on both Central Manager and Smart Poller.

**NOTE:**
> By default, notifications about to monitored devices/services are sent by Smart Pollers.

Since the Central Manager can perform self-diagnostics procedures, in case it detects any issues, it can generate alarm
notifications as well.

Therefore, SMTP should be configured also on the Central Manager itself.

## SMTP Configuration

1) Select option **7) SMTP settings (e-mail)**

![i-Vertix menu](../../assets/installation/ivertix-menu.png)

2) A new menu shows up

![Relay host](../../assets/installation/relay-host.png)

3) Select **Y**
4) A new menu shows up

![SMTP options](../../assets/installation/smtp-options.png)

5) Select the proper SMTP option among the proposed ones

### Available options are

1) **Normal SMTP**: please follow each step carefully

![Normal SMTP](../../assets/installation/simple-relay.png)

2) **SMTP with authentication**

![Authenticated SMTP](../../assets/installation/auth-smtp.png)

3) **SMTP for Office365 or Amazon AWS SES**

![O365 - AWS SES SMTP](../../assets/installation/O365-smtp.png)


---

### Configuration steps for SMTP

Compile every voice the menu steps indicate for each SMTP option you choose.

Once the proper option has been selected and configured, quit using **q** command

If you want to test the configuration you've just made, simply type **T) Test SMTP settings** in the menu.

![Relay host](../../assets/installation/relay-host.png)

**NOTE:**
> Provide real a e-mail sender and a e-mail reciver for the test.

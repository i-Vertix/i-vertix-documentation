---
title: "Azure Prerequisites"
---

The Azure plugin packs retrieve their data through the Azure Rest API. To monitor Azure resources (and to use the
[Azure cloud discovery](/monitoring/monitoring-resources/discovery/common-discovery#azure)), you need an *Application* in Azure,
which provides the following credentials:

* Subscription ID
* Tenant ID
* Client ID
* Client Secret

## Create the Azure application

The walkthrough below helps you to prepare the Azure application and the role required for monitoring and discovery:

1. Log in to the Azure Portal
2. Switch to **Azure Active Directory** (*Microsoft Entra ID*)
3. Navigate to **App registrations** using the left sidebar
4. Click `+ New registration` and choose a name for the application (e.g. *i-Vertix Monitoring*)
5. Return to the main page of the Azure Portal
6. Switch to **Resource groups**
7. Choose or create a resource group containing the resources you want to monitor/discover
8. Click on `Access Control (IAM)` and `+ Add`, `Add role assignment`
9. Select the built-in **Monitoring Reader** role and click `Next`
10. Select the new application you previously created as a member for this resource group by clicking `+ Select members`
11. Review and assign the changes

## Retrieve the credentials

Now you need to obtain the credential information mentioned above:

1. Retrieve the *Subscription ID*
    * Switch to **Subscriptions** in the Azure Portal
    * Copy the *Subscription ID* next to the name of your subscription
2. Retrieve the *Tenant ID*
    * Switch to **Azure Active Directory** (*Microsoft Entra ID*)
    * Navigate to **Overview** and copy the *Tenant ID*
3. Retrieve the *Client ID*
    * Switch to **Azure Active Directory** (*Microsoft Entra ID*)
    * Navigate to **App registrations** using the left sidebar
    * Select **Overview** and copy the *Application ID* (*Client ID*)
4. Retrieve the *Client Secret*
    * Switch to **Azure Active Directory** (*Microsoft Entra ID*)
    * Navigate to **App registrations** using the left sidebar
    * Select **Certificates & Secrets**
    * Click on `+ New client secret` and choose a description and expiration date for the new secret
    * Add the new secret, then copy and temporarily store the generated *Client Secret* (it is only shown once)

:::warning

The *Client Secret* expires at the date you chose. Renew it in time and update it in i-Vertix, otherwise the monitoring of all
Azure resources using this application stops working.

:::

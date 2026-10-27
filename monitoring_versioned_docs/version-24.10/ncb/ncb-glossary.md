---
id: ncb-glossary
title: NCB Glossary
---

| Term | Explaination |
| --- |---|
| Backup (Configuration) / Device | The configuration that determines how to access and handle a given host |
| Network Configuration Backup | The stored output returned from the network device after the backup service executed the necessary commands to extract said configuration. |
| Vendor | The device's vendor |
| OS Model | The device's specific OS Model. Depends on the vendor and determines which commands are executed by the backup service to extract the devices network configuration. |
| Oxidized / Backup service | The program run as a service that is used to fetch the backup configuration, contact each device, retrieve the configuration, compare it with the already stored configuration and, if necessary, store the newer version of the configuration. |
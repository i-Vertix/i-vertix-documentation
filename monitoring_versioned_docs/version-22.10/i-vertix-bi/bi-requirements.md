---
id: bi-requirements
title: Requirements
---

## Dedicated i-Vertix BI machine

The i-Vertix BI runs on its own instance to prevent negative impacts of the resources on the central monitoring system. Some tasks of the i-Vertix BI are very resource-intensive and it is therefore necessary to plan the hardware for the i-Vertix BI system accordingly.

The basic factor here is the size of the monitoring system itself, i.e. how many hosts and services are monitored and how much data is generated approximately every day.

### Hardware-Computing requirements

The required system computing requirements depend on the amount of data which is generated daily by the monitoring checks (services).

The required storage depends on the amount of data, the quantity of generated reports and the configured retention.

The below table is intended to help you find the right hardware resources for the i-Vertix BI instance based on the amount of hosts and services on your monitoring system.

|         | 1.000 Hosts | 2.500 Hosts | 5.000 Hosts | 10.000 Hosts |
| ------- | ----------- | ----------- | ----------- | ------------ |
| CPU     | 4 Cores     | 4 Cores     | 6 Cores     | 8 Cores      |
| RAM     | 8 GB        | 8 GB        | 12 GB       | 16 GB        |
| Storage | 250 GB      | 350 GB      | 500 GB      | 750 GB       |

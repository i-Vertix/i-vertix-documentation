---
title: "AWS Prerequisites"
---

The AWS plugin packs retrieve their data through the AWS API (metrics from *Amazon CloudWatch*). To monitor AWS resources
(and to use the [AWS cloud discovery](/monitoring/monitoring-resources/discovery/common-discovery#aws)), you need a
dedicated AWS user, which provides the following credentials:

* Access Key ID
* Secret Access Key

The host templates also need the *region* of the resources (e.g. `eu-west-1`).

## Create the AWS user

1. Log in to the AWS Management Console
2. Switch to **IAM** and navigate to **Users**
3. Click `Create user` and choose a name for the user (e.g. *i-Vertix Monitoring*); console access is not needed
4. Attach a policy with the permissions listed [below](#required-permissions), depending on what you want to monitor/discover
5. Review and create the user

## Retrieve the credentials

1. Open the new user in **IAM** > **Users** and switch to **Security credentials**
2. Click `Create access key` and choose *Third-party service* (or *Other*) as use case
3. Copy and temporarily store the *Access Key ID* and the *Secret Access Key* (the secret is only shown once)

Set them in the host macros `AWS-ACCESS-KEY` and `AWS-SECRET-KEY` of the AWS hosts.

## Required permissions

All AWS plugin packs read their metrics from CloudWatch and need `cloudwatch:GetMetricStatistics`.
Discovery and some checks need additional permissions for the monitored service:

<details>
<summary>API Gateway</summary>

| Privilege                      | Description                                          |
|--------------------------------|------------------------------------------------------|
| apigateway:GetRestApis         | Display API Gateway REST APIs details                |
| cloudwatch:GetMetricStatistics | Get metrics from the API Gateway namespace on CloudWatch |

</details>

<details>
<summary>EBS</summary>

| Privilege                      | Description                                          |
|--------------------------------|------------------------------------------------------|
| ec2:DescribeVolumes            | Display EBS volumes details                          |
| cloudwatch:GetMetricStatistics | Get metrics from the EBS namespace on CloudWatch     |

</details>

<details>
<summary>EC2</summary>

| Privilege                      | Description                                          |
|--------------------------------|------------------------------------------------------|
| ec2:DescribeInstances          | Display EC2 instances & ASG details                  |
| ec2:DescribeSpotFleetRequests  | Display EC2 Spot Fleet Requests details              |
| cloudwatch:GetMetricStatistics | Get metrics from the EC2 namespace on CloudWatch     |

</details>

<details>
<summary>ElastiCache</summary>

| Privilege                      | Description                                              |
|--------------------------------|----------------------------------------------------------|
| elasticache:DescribeCacheClusters | Display ElastiCache clusters details                     |
| cloudwatch:GetMetricStatistics | Get metrics from the ElastiCache namespace on CloudWatch |

</details>

<details>
<summary>ELB (Load Balancer)</summary>

| Privilege                      | Description                                              |
|--------------------------------|----------------------------------------------------------|
| elasticloadbalancing:DescribeLoadBalancers | Display ELB details                                      |
| cloudwatch:GetMetricStatistics | Get metrics from the ELB namespace on CloudWatch         |

</details>

<details>
<summary>Lambda</summary>

| Privilege                      | Description                                              |
|--------------------------------|----------------------------------------------------------|
| lambda:ListFunctions           | Display Lambda functions details                         |
| cloudwatch:GetMetricStatistics | Get metrics from the Lambda namespace on CloudWatch      |

</details>

<details>
<summary>RDS (Relational Databases)</summary>

| Privilege                      | Description                                              |
|--------------------------------|----------------------------------------------------------|
| rds:DescribeDBInstances        | Display RDS instances & cluster details                  |
| cloudwatch:GetMetricStatistics | Get metrics from the RDS namespace on CloudWatch         |

</details>

<details>
<summary>S3</summary>

| Privilege                      | Description                                          |
|--------------------------------|------------------------------------------------------|
| s3:ListAllMyBuckets            | Display S3 buckets details                           |
| cloudwatch:GetMetricStatistics | Get metrics from the S3 namespace on CloudWatch      |

</details>

<details>
<summary>SQS</summary>

| Privilege                      | Description                                          |
|--------------------------------|------------------------------------------------------|
| sqs:ListQueues                 | Display Messaging Queue Services                     |
| cloudwatch:GetMetricStatistics | Get metrics statistics from the SQS on CloudWatch    |
| cloudwatch:ListMetrics         | List metrics from the SQS on CloudWatch              |

</details>

:::warning

Rotate the access key regularly and update it in i-Vertix, otherwise the monitoring of all AWS resources using this user
stops working once the old key is deactivated.

:::

# 🚀 Automated EC2 Instance Management - AWS Lambda and Boto3

Welcome to the `heroVired_ServerLess_CloudAutomation` repository!

This project demonstrates how to use **AWS Lambda** and **Boto3** to automate various EC2 and Load Balancer management tasks in a **serverless cloud environment**.

---

## 📂 Repository Details

- **Repository Name**: `heroVired_ServerLess_CloudAutomation`
- **Repository Link**: [GitHub Repo](https://github.com/pradeepkarunya/heroVired_ServerLess_CloudAutomation)

---

## 📘 Assignments Included

### ✅ Assignment 1 – Automated Instance Management Using AWS Lambda and Boto3

**Objective**: Automatically manage EC2 instance states.

- 🟥 **Stops** EC2 instances with tag `Action=Auto-Stop`
- 🟩 **Starts** EC2 instances with tag `Action=Auto-Start`
- Uses AWS Lambda (Python 3.x) with Boto3
- IAM Role with `AmazonEC2FullAccess` required
- Can be triggered manually or scheduled using CloudWatch Events

---

### ✅ Assignment 5 – Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

**Objective**: Automatically tag EC2 instances on launch with:

- `LaunchDate`: Current UTC date
- `Project`: AutoTaggedEC2

**Key Components**:
- Triggered by EC2 launch event
- Uses Boto3 to create tags on the newly launched instance
- Requires IAM permissions for `ec2:CreateTags`

---

### ✅ Assignment 19 – Load Balancer Health Checker

**Objective**: Monitor the health of EC2 instances behind an ELB and send alerts via SNS.

- Checks if any instance is not in `InService` state
- Sends an email alert through Amazon SNS
- Lambda function triggered every 10 minutes via EventBridge
- IAM Role requires:
  - `AmazonEC2ReadOnlyAccess`
  - `AmazonSNSFullAccess`
  - `ElasticLoadBalancingReadOnly`

---

## 🧰 Technologies Used

- **AWS Lambda**
- **Amazon EC2**
- **Elastic Load Balancer (ELB)**
- **Amazon SNS**
- **AWS IAM**
- **Amazon CloudWatch**
- **Boto3 (AWS SDK for Python)**

---

## 🧠 Author

**Pradeep Kumar**  
Senior Cloud & Front-End Developer  
GitHub: [@pradeepkarunya](https://github.com/pradeepkarunya)

---

## 📅 Last Updated

June 2025

---

# 🖥️ Automated EC2 Instance Management using AWS Lambda and Boto3

This project demonstrates how to automatically **start and stop EC2 instances** based on their tags using **AWS Lambda** and **Boto3 (Python SDK)**.

---

## ✅ Assignment 1



Automatically manage EC2 instance states:
- **Stop instances** with the tag `Action=Auto-Stop`
- **Start instances** with the tag `Action=Auto-Start`

---

## 1. EC2 Setup

1. Navigate to **EC2 Dashboard**.
2. **Launch 2 EC2 instances** (free-tier eligible: `t2.micro`).
3. **AMI**: Select **Amazon Linux 2 AMI**.
4. **Instance type**: `t2.micro`
5. **Configure**: Leave defaults.
6. **Add Tags**:
   - **Instance 1**:
     - `Key`: `Action`
     - `Value`: `Auto-Stop`
   - **Instance 2**:
     - `Key`: `Action`
     - `Value`: `Auto-Start`
7. Launch both instances.

---

## 2. IAM Role Setup for Lambda

1. Go to **IAM → Roles → Create Role**
2. **Trusted entity**: AWS service → **Lambda**
3. **Permissions**: Attach the policy: `AmazonEC2FullAccess`
4. **Name**: `LambdaEC2AutomationRole`

---

## 3. Lambda Function Setup

1. Go to **Lambda → Create Function**
2. **Name**: `ManageEC2ByTags`
3. **Runtime**: Python 3.x
4. **Permissions**: Use existing role → `LambdaEC2AutomationRole`

---

## 4. Lambda Function Code (Python + Boto3)

Paste the following code inside the Lambda code editor:

```python
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Auto-Stop instances
    stop_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    stop_instances = [
        instance['InstanceId']
        for reservation in stop_response['Reservations']
        for instance in reservation['Instances']
    ]
    if stop_instances:
        ec2.stop_instances(InstanceIds=stop_instances)
        print(f"Stopped Instances: {stop_instances}")
    else:
        print("No running instances with tag 'Auto-Stop' found.")

    # Auto-Start instances
    start_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )
    start_instances = [
        instance['InstanceId']
        for reservation in start_response['Reservations']
        for instance in reservation['Instances']
    ]
    if start_instances:
        ec2.start_instances(InstanceIds=start_instances)
        print(f"Started Instances: {start_instances}")
    else:
        print("No stopped instances with tag 'Auto-Start' found.")

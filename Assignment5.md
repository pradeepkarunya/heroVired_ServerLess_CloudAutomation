# Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

## 📌 Assignment 5

Automatically tag EC2 instances with the current date and a custom project tag as soon as they are launched. This ensures better resource tracking and management in AWS environments.

---

## ✅ Steps to Implement

### 1. EC2 Setup
- Ensure your AWS account has permissions to launch EC2 instances.

---

### 2. IAM Role for Lambda
- Go to **IAM > Roles > Create Role**
- **Trusted Entity**: AWS Lambda
- **Permissions**: Attach
  - `AmazonEC2FullAccess`
  - (Optional) `CloudWatchLogsFullAccess`
- **Role Name**: `LambdaEC2AutoTagRole`

---

### 3. Create Lambda Function
- Go to **AWS Lambda > Create Function**
- **Function Name**: `AutoTagEC2`
- **Runtime**: Python 3.x
- **Execution Role**: Use existing → `LambdaEC2AutoTagRole`

---

### 4. Lambda Function Code

```python
import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    instances = event['detail']['instance-id']
    
    current_date = datetime.utcnow().strftime('%Y-%m-%d')
    tags = [
        {'Key': 'LaunchDate', 'Value': current_date},
        {'Key': 'Project', 'Value': 'AutoTaggedEC2'}
    ]
    
    ec2.create_tags(Resources=[instances], Tags=tags)
    print(f"Tagged instance {instances} with LaunchDate and Project tags")

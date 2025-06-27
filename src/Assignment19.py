import boto3
import os

elb_client = boto3.client('elb')
sns_client = boto3.client('sns')

# Replace with your ELB name and SNS Topic ARN
ELB_NAME = 'your-elb-name'
SNS_TOPIC_ARN = 'arn:aws:sns:your-region:account-id:ELBHealthAlert'

def lambda_handler(event, context):
    response = elb_client.describe_instance_health(LoadBalancerName=ELB_NAME)
    unhealthy_instances = [inst for inst in response['InstanceStates'] if inst['State'] != 'InService']
    
    if unhealthy_instances:
        message = "Unhealthy Instances Detected:\n"
        for inst in unhealthy_instances:
            message += f"Instance ID: {inst['InstanceId']} | State: {inst['State']}\n"
        
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='ALERT: Unhealthy EC2 Instances in ELB',
            Message=message
        )
        print("Alert sent via SNS.")
    else:
        print("All instances are healthy.")

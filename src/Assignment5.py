import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Extract instance ID
    instances = event['detail']['instance-id']
    
    # Tags
    current_date = datetime.utcnow().strftime('%Y-%m-%d')
    tags = [
        {'Key': 'LaunchDate', 'Value': current_date},
        {'Key': 'Project', 'Value': 'AutoTaggedEC2'}
    ]
    
    # Apply tags
    ec2.create_tags(Resources=[instances], Tags=tags)
    print(f"Tagged instance {instances} with LaunchDate and Project tags")

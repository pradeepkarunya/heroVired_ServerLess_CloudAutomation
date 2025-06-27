import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    tags = event.get("tags", [])

    for tag in tags:
        tag_key = tag.get("key")
        tag_value = tag.get("value")

        # Start stopped instances with this tag
        start_response = ec2.describe_instances(
            Filters=[
                {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
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
            print(f"Started instances for tag {tag_value}: {start_instances}")

        # Stop running instances with this tag
        stop_response = ec2.describe_instances(
            Filters=[
                {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
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
            print(f"Stopped instances for tag {tag_value}: {stop_instances}")

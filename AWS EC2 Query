# searching through instances to find status of ec2

## option 1

import boto3

session = boto3.resource('s3')
ec2 = session.resource('ec2')

def lambda_handler(event, context)
  instances = ec2.instances.filter(
    Filters=[
      {
        'Name': 'instance-state-name', 
        'Values': [
          'stopped', 'terminated'
          ]
      }
    ]
  )

  for instance in instances:
    print (f'EC2 instance '{instance.id}', State: {instance.state['Name']}, Instance Type: {instnace.instance_type}')

##Option 2

import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context)
  instances = ec2.instances.filter(
    Filters=[
      {
        'Name': 'instance-state-name', 
        'Values': [
          'stopped', 'terminated'
          ]
      }
    ]
  )
  for instance in instances:
    print (f'EC2 instance '{instance.id}', State: {instance.state['Name']}, Instance Type: {instnace.instance_type}')
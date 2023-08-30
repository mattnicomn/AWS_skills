import boto3

ec2 = boto3.client('ec2', 'us-gov-west-1')

def get_instance_family(instance_type):
    return instance_type.split('.')[0]

def lambda_handler(event, context):
    

    #setting a variable for list and looping through the list
    instance_family_counts = {}
    
    # Get all stopped instances
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [
                    'stopped',
                ]
            },
        ]
    )

    #Create metric for count attribute to work
    count = 0

    #Create a loop to go through the list of instance types that are in a stopped state in the current account
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_type = instance['InstanceType']
            instance_family = get_instance_family(instance_type)
            
            if instance_family in instance_family_counts:
                instance_family_counts[instance_family] += 1
            else:
                instance_family_counts[instance_family] = 1
                
    sorted_instance_family_counts = sorted(instance_family_counts.items())
        
    for instance_family, count in sorted_instance_family_counts:
        print(f'{instance_family}: {count}')
       
    return {
        'statusCode': 200,
        'body': 'Script execution completed.'
    } 



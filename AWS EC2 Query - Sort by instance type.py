import boto3
import collections
#import json

ec2 = boto3.client('ec2')
response_type = ec2.describe_instance_types()

def lambda_handler(event, context):
 # Get all stopped instances
 stopped_instances = []
 reservations = ec2.describe_instances()
 for reservation in reservations['Reservations']:
  for instance in reservation['Instances']:
   if instance['State']['Name'] == 'stopped':
    stopped_instances.append(instance)

 # Count and sort instances by memory
 instance_counts = collections.defaultdict(int)
 for instance in stopped_instances:
  instance_counts[instance['InstanceType']] += 1

 sorted_instance_counts = sorted(instance_counts.items(), key=lambda x: x[0], reverse=False)

 # Get all instances
 instances = reservations['Reservations']

 # Calculate total memory for each instance type
 instance_types = {}
 for instance in instances:
  for instance_type in instance['Instances']:
   if instance_type['InstanceType'] in instance_types:
    instance_types[instance_type['InstanceType']] += response_type['InstanceTypes'][0]['MemoryInfo']['SizeInMiB']
   else:
    instance_types[instance_type['InstanceType']] = response_type['InstanceTypes'][0]['MemoryInfo']['SizeInMiB']

 sorted_instance_types = sorted(instance_types.items(), key=lambda x: x[1], reverse=False)
 combined_response = dict(InstanceCounts=sorted_instance_counts, InstanceTypes=sorted_instance_types)

 return combined_response
 
######################################################################## other ways outputting responses
# # Combine the two responses in json
# combined_response = {
# 'InstanceCounts': sorted_instance_counts,
# 'InstanceTypes': sorted_instance_types
# }
# #Combine the two responses in a collection, same response
# combined_response = collections.OrderedDict([
#    ("InstanceCounts", sorted_instance_counts),
#    ("InstanceTypes", sorted_instance_types),
#])

# # Combine the two responses json response
# combined_response = json.dumps({
# 'InstanceCounts': sorted_instance_counts,
# 'InstanceTypes': sorted_instance_types
# })
# return combined_response


######################################################################## learning query to find stopped instances and sorting with describe_instance_types()
#def lambda_handler(event, context):
 
# # Get all stopped instances 
# stopped_instances = []
# reservations = ec2.describe_instances(
#     Filters=[
#         {
#             'Name': 'instance-state-name',
#             'Values': ['stopped']
#         }
#     ]
# )
# for reservation in reservations['Reservations']:
#  for instance in reservation['Instances']:
#   stopped_instances.append(instance)
# 
# # Count and sort instances by memory
# instance_counts = collections.defaultdict(int)
# for instance in stopped_instances:
#  instance_counts[instance['InstanceType']] += 1
# 
# sorted_instance_counts = sorted(instance_counts.items(), key=lambda x: x[0], reverse=False)
#
# instances = reservations['Reservations']
#
# instance_types = {}
# for instance in instances:
#  for instance_type in instance['Instances']:
#   if instance_type['InstanceType'] in instance_types:
#     instance_types[instance_type['InstanceType']] += response_type['InstanceTypes'][0]['MemoryInfo']['SizeInMiB']
#   else:
#    instance_types[instance_type['InstanceType']] = response_type['InstanceTypes'][0]['MemoryInfo']['SizeInMiB']
# sorted_instance_types = sorted(instance_types.items(), key=lambda x: x[1], reverse=False)
# #return sorted_instance_types 
# 
# sorted_total = sorted_instance_counts + sorted_instance_types
# 
# # Print the output
# for instance_type, count in sorted_total:
#  print(f'{count} instances of type {instance_type}')

#ec2 = boto3.client('ec2')
#response_type = ec2.describe_instance_types()

############################################################################# learning query to find stopped instances and sorting
#def lambda_handler(event, context):
    
# response = ec2.describe_instances(
#  Filters=[
#       {
#          'Name': 'instance-state-name',
#          'Values': ['stopped']
#       }
#    ]
#  )
 
    #response_all = ec2.describe_instances()
    
# instances = response['Reservations']
    
# instance_types = {}
# for instance in instances:
#  for instance_type in instance['Instances']:
#   if instance_type['InstanceType'] in instance_types:
#     instance_types[instance_type['InstanceType']] += response_type['InstanceTypes'][0]['MemoryInfo']['SizeInMiB']
#   else:
#    instance_types[instance_type['InstanceType']] = response_type['InstanceTypes'][0]['MemoryInfo']['SizeInMiB']
# sorted_instance_types = sorted(instance_types.items(), key=lambda x: x[1], reverse=True)
# return sorted_instance_types
 
############################################################################# Troubleshooting and learning AWS Boto3 resources/requests 
 #def lambda_handler(event, context):

 ##instances = ec2.describe_instances()
  
 ##stopped_instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['stopped']}])
  
  
  # Count the number of instances in each type
 ##instance_counts = {}
 ##for instance in stopped_instances['Reservations']:
  ##for instance_info in instance['Instances']:
   ##instance_type = instance_info['InstanceType']
   ##if instance_type not in instance_counts:
    ##instance_counts[instance_type] = 0
   ##instance_counts[instance_type] += 1
    
  # Sort the instance counts by type
 ##sorted_instance_counts = sorted(instance_counts.items(), key=lambda x: x[0])
  #sorted_types = sorted(types['InstanceTypes'][0]['MemoryInfo'], key=lambda x: x[0])
  # Print the results 
 ##for instance_type, count in sorted_instance_counts:
  ##print('{}: {}'.format(count, instance_type))
   
   
  #stopped_instances.sort(key=lambda type:type[1])
 # Lambda function to find stopped EC2 instances
  #types = ec2.describe_instance_types()
  
  #instance_size = {}
  #for instance_size in stopped_instances['Reservations']:
   #return('{}').format(instance_size) 
   #for instance_info_size in types['InstanceTypes']:
    
    #instance_type_size = instance_info_size['MemoryInfo']
     
 # Sort the instances by instance type and SizeInMiB
 #instancesort = types['InstanceTypes']
 #sorted_instances = sorted(instance_type_size.items(), key=lambda x: (x['MemoryInfo']['SizeInMiB']))
 #sorted_instances = sorted(instance_info_size.items(), key=lambda x: x[0])
 #sorted_ins = sorted(instances['Reservations'], key=lambda x: (x['Instances'][0]['InstanceType'])) 
 #for instance_info_size in sorted_instances:
  #print('{}'.format(instance_info_size))
 #for instance in sorted_ins:
  #print(f"Instance ID: {instance['Instances'][0]['InstanceId']}")

 #for type in sorted_instances:
  #print(f" Instance Type: {type['InstanceType']}  Instance Size: {type['MemoryInfo']['SizeInMiB']}")

 #for i in stopped_instances:
  #maybe a in statement
  #for instance in sorted_ins:
   #for type in sorted_instances:
    #print(f"Instance ID: {instance['Instances'][0]['InstanceId']} Instance Type: {type['InstanceType']}  Instance Size: {type['MemoryInfo']['SizeInMiB']}")
    
  
  #print(f'{instance_type}: {count}')
  
    
 

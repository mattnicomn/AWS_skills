import boto3

s3 = boto3.client('s3')

def lamnda_handler(event, context)

  count = 0
  response =s3.list_objects_v2(bucket=event['bucket'])
  #paginator = s3.get_paginator('list_objects_v2')
  #iterator = paginator.paginate(Bucket=event['bucket']
  
  if 'Contents' in response:
    for object in response['Contents']:
      if object['Key'][-1] != '/':
        count += 1
  return("Number of files: ", count)


  #if 'Contents' in response:
    #for file in iterator:
      #for object in ['Contents']"
        #if object['Key'].endswith('/')
          #count += 1
  #return (f'Number of objects in Bucket: {bucket.name} Key : {file.key}')
#https://stackoverflow.com/questions/42673764/boto3-s3-get-files-without-getting-folders

import boto3,os


### add the bucket as per your need
def addBucket(name,location='eu-west-3'):
    client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("ACCESS_ID"),
    aws_secret_access_key= os.getenv("ACCESS_KEY")
    )

    response = client.create_bucket(
        Bucket=name,
    )

    print (response)


def addEC2():
    ec2 = boto3.client('ec2',region_name='us-east-1',
    
    aws_access_key_id=os.getenv("ACCESS_ID"),
    aws_secret_access_key= os.getenv("ACCESS_KEY")
    )
    instances = ec2.run_instances(
        ImageId='ami-04505e74c0741db8d',                  
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
#     SecurityGroupIds= ['sg-0be1291dabfeeface']           security-wizard-2
)
# for instance in ec2.instances:
#     print(f'EC2 instance "{instance.id}" has been launched')
    print(instances)
def getec2():
    ec2 = boto3.resource('ec2',region_name='us-east-1',
    
    aws_access_key_id=os.getenv("ACCESS_ID"),
    aws_secret_access_key= os.getenv("ACCESS_KEY")
    )
    filters = [
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    for instance in ec2.instances.all():
        print(
            "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
            )
        )
    return ec2.instances.filter(Filters=filters)

def deleteInstance(id):
    ec2 = boto3.resource('ec2',region_name='us-east-1',
    aws_access_key_id=os.getenv("ACCESS_ID"),
    aws_secret_access_key= os.getenv("ACCESS_KEY")
    )
    ec2.instances.filter(InstanceIds = [id]).terminate()


def getBuckets():
    s3 = boto3.client('s3',
    aws_access_key_id=os.getenv("ACCESS_ID"),
    aws_secret_access_key= os.getenv("ACCESS_KEY")
    )
    response = s3.list_buckets()
    print(response)

    return response['Buckets']
def deleteBucket(name):
    s3 = boto3.client('s3',
    aws_access_key_id=os.getenv("ACCESS_ID"),
    aws_secret_access_key= os.getenv("ACCESS_KEY")
    )
    s3.delete_bucket(Bucket=name)


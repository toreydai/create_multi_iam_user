import boto3
iam = boto3.client('iam')

a = 'user0'
b = ''
for i in range(1,10):
  name = a + str(i)
  iam.delete_user(UserName=name)

a = 'user'
b = ''
for i in range(10,51):
  name = a + str(i)
  iam.delete_user(UserName=name)

iam.delete_group(
    GroupName='Workshop_Group'
)

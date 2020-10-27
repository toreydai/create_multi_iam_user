import boto3
iam = boto3.client('iam')

a = 'user0'
for i in range(1,10):
  name = a + str(i)
  iam.delete_login_profile(UserName=name)
  iam.delete_user(UserName=name)

a = 'user'
for i in range(10,51):
  name = a + str(i)
  iam.delete_login_profile(UserName=name)
  iam.delete_user(UserName=name)

iam.delete_group(
    GroupName='Workshop_Group'
)

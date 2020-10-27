import boto3
iam = boto3.client('iam')

iam.create_group(
    GroupName='Workshop_Group',
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/AWSLambdaFullAccess'
    )
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/AmazonS3FullAccess'
    )
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/CloudWatchFullAccess'
    )
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/AmazonDynamoDBFullAccess'
    )
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/AmazonSNSFullAccess'
    )
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/AmazonSQSFullAccess'
    )
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/AWSXrayFullAccess'
    )
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/AmazonKinesisFullAccess'
    )
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/AWSCloudFormationFullAccess'
    )
)

iam.attach_group_policy(
    GroupName='Workshop_Group',
    PolicyArn=(
        'arn:aws-cn:iam::aws:policy/IAMUserChangePassword'
    )
)

a = 'user0'
b = ''
for i in range(1,10):
  name = a + str(i)
  iam.create_user(UserName=name)
  
  iam.create_login_profile(
      UserName=name,
      Password='3}~LKeV3}qZ',
      PasswordResetRequired=True
  )
  
  iam.add_user_to_group(
      GroupName='Workshop_Group',
      UserName=name
  )

c = 'user'
d = ''
for i in range(10,41):
  name = c + str(i)
  iam.create_user(UserName=name)
  
  iam.create_login_profile(
      UserName=name,
      Password='3}~LKeV3}qZ',
      PasswordResetRequired=True
  )
  
  iam.add_user_to_group(
      GroupName='Workshop_Group',
      UserName=name
  )

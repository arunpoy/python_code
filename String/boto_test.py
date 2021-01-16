import boto3
# Creating boto3 handle for iam resource
client = boto3.client('iam')

response = client.list_attached_user_policies(
    UserName='athena-user')


print(response)

policies = [policy['PolicyName'] for policy in response['AttachedPolicies'] ]

print(policies)

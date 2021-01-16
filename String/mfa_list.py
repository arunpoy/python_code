import boto3
# Creating boto3 handle for iam resource
session = boto3.Session(profile_name='default')
IAM_CLIENT = session.client('iam')
mfa_list = []
def get_login(user):


    try:
        response = IAM_CLIENT.get_login_profile(UserName=user)
        if response['LoginProfile']['UserName'] == user:
            get_mfa(user)
    except IAM_CLIENT.exceptions.NoSuchEntityException:
        pass
def get_mfa(user):
    """ Check the mfa devices attached to the user. If no mfa exists, print MFA not enabled.
        Parameters: user (string): Username of IAM user who has login profile enabled.
    """
    response = IAM_CLIENT.list_mfa_devices(UserName=user)
    if response['MFADevices'] != [] and "mfa" in response['MFADevices'][0]['SerialNumber']:
        pass
    else:
        print("MFA not enabled: {}".format(user))
        mfa_list.append(user)
def get_policies_for_users(mfa_list):

    for user in mfa_list:

        List_of_Policies =  IAM_CLIENT.list_attached_user_policies(UserName=user)
        print(List_of_Policies)
        policies = [policy['PolicyName'] for policy in List_of_Policies['AttachedPolicies'] ]
        print("{0},{1}".format(user,','.join(policies)))

if __name__ == '__main__':
# Use boto3 paginator option if number of users is very high.
    DETAILS = IAM_CLIENT.list_users(MaxItems=250)
    for user_detail in DETAILS['Users']:
        get_login(user_detail['UserName'])
    print(mfa_list)
    get_policies_for_users(mfa_list)

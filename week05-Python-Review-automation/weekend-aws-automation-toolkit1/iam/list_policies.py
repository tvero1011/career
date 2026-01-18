import boto3

iam = boto3.client('iam')

def list_iam_policies():
    try:
       response = iam.list_policies(Scope='AWS')
         policies = response.get('Policies', [])

        for policy in policies:
            if policy['PolicyName'] == 'ReadOnlyAccess':
                target_arn = policy['Arn']
                print(target_arn)
                return target_arn

    except Exception as e:
        print(f"An error occurred: {e}")
    return None        

if __name__ == "__main__":
    list_iam_policies()

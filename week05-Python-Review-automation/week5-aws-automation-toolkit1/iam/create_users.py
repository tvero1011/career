import boto3    
from botocore.exceptions import ClientError, NoCredentialsError

def create_iam_user(user_name):
    iam = boto3.client("iam")
    try:
        response = iam.create_user(UserName=user_name)
        print(f"User {user_name} created successfully. ARN: {response['User']['Arn']}")
    
        iam.attach_user_policy(
            UserName=user_name,
            PolicyArn="arn:aws:iam::aws:policy/ReadOnlyAccess"
         )
        print(f"Attached ReadOnlyAccess policy to user {user_name}.")
    
    except NoCredentialsError:
        print("Credentials not available.")
    
    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")

if __name__ == "__main__":
    create_iam_user("new_test_user")  # Replace with desired user name
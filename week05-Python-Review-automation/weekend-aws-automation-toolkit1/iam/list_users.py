import boto3 
from botocore.exceptions import ClientError, NoCredentialsError

def list_iam_users():
    iam = boto3.client("iam")
    try:
        response = iam.List_users()
        users = response.get("Users", [])
        for user in users:
            print(f"User Name: {user['UserName']}, User ID: {user['UserId']}, ARN: {user['Arn']}") 
    except NoCredentialsError:
        print("Credentials not available.") 
    
    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")   

if __name__ == "__main__":
    list_iam_users()
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def delete_iam_user(user_name):
    iam = boto3.client("iam")
    try:
        iam.detach_user_policy(
            UserName=user_name,
            PolicyArn="arn:aws:iam::aws:policy/ReadOnlyAccess"
        )
        print(f"Detached ReadOnlyAccess policy from user {user_name}.")

        iam.delete_user(UserName=user_name)
        print(f"User {user_name} has been deleted successfully.")

        
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    delete_iam_user("user_to_delete") # Replace with the actual user name to delete
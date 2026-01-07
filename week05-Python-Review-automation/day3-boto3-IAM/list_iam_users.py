import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def list_iam_users():
    """
    Lists all IAM users in the AWS account.
    Safe read-only IAM automation.
    """
    try:
        # Create IAM client (global service)
        iam = boto3.client("iam")

        # Call AWS IAM API
        response = iam.list_users()

        # Print full response for learning/debugging
        print("FULL RESPONSE:")
        print(response)

        print("\nIAM Users:")
        for user in response.get("Users", []):
            print(f"- {user['UserName']}")

    except NoCredentialsError:
        print("AWS credentials not found.")

    except ClientError as e:
        print(f"AWS IAM error: {e}")

if __name__ == "__main__":
    list_iam_users()

import boto3
from botocore.exceptions import ClientError

IAM_USER_NAME = "week5-test-user"
POLICY_ARN = "arn:aws:iam::aws:policy/ReadOnlyAccess"

def delete_user():
    """
    Detaches policy and deletes IAM user.
    """
    iam = boto3.client("iam")

    try:
        # Detach policy first (REQUIRED)
        iam.detach_user_policy(
            UserName=IAM_USER_NAME,
            PolicyArn=POLICY_ARN
        )
        print("Policy detached.")

        # Delete IAM user
        iam.delete_user(UserName=IAM_USER_NAME)
        print(f"IAM user '{IAM_USER_NAME}' deleted.")

    except ClientError as e:
        print(f"AWS error: {e}")

if __name__ == "__main__":
    delete_user()

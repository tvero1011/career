import boto3
from botocore.exceptions import ClientError

IAM_USER_NAME = "week5-test-user"

def create_user():
    """
    Creates an IAM user and attaches ReadOnlyAccess policy.
    """
    iam = boto3.client("iam")

    try:
        # Create IAM user
        iam.create_user(UserName=IAM_USER_NAME)
        print(f"IAM user '{IAM_USER_NAME}' created.")

        # Attach AWS managed ReadOnlyAccess policy
        iam.attach_user_policy(
            UserName=IAM_USER_NAME,
            PolicyArn="arn:aws:iam::aws:policy/ReadOnlyAccess"
        )
        print("ReadOnlyAccess policy attached.")

    except ClientError as e:
        print(f"AWS error: {e}")

if __name__ == "__main__":
    create_user()

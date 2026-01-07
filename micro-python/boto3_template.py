from botocore.exceptions import ClientError, NoCredentialsError

try:
    iam.list_users()

except NoCredentialsError:
    print("Credentials not configured")

except ClientError as e:
    code = e.response["Error"]["Code"]
    message = e.response["Error"]["Message"]
    print(f"AWS error {code}: {message}")

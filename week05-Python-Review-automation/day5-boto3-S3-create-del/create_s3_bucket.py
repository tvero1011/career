import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "week5-test-bucket-yourname-12345"

def create_bucket():
    """
    Create an S3 bucket safely.
    """
    s3 = boto3.client("s3")

    try:
        s3.create_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket '{BUCKET_NAME}' created successfully.")

    except ClientError as e:
        print(f"AWS error: {e}")

if __name__ == "__main__":
    create_bucket()

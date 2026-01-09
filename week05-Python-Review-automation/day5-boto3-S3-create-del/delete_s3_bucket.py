import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "week5-test-bucket-yourname-12345"

def delete_bucket():
    """
    Delete an S3 bucket safely.
    """
    s3 = boto3.client("s3")

    try:
        s3.delete_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket '{BUCKET_NAME}' deleted successfully.")

    except ClientError as e:
        print(f"AWS error: {e}")

if __name__ == "__main__":
    delete_bucket()

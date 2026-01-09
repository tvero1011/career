import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def list_buckets():
    try:
        s3 = boto3.client("s3")
        response = s3.list_buckets()
        # print(response)

     # print("S3 Buckets:")
     # for bucket in response.get("Buckets", []):
     #     print(f"- {bucket['Name']}")

    except NoCredentialsError:
        print("AWS credentials not found.")
    except ClientError as e:
        print(f"AWS error: {e}")



if __name__ == "__main__":
    list_buckets()

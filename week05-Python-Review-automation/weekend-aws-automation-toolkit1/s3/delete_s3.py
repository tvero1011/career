import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def delete_s3_bucket(bucket_name):
    s3 = boto3.client("s3")

    try:
        paginator = s3.get_paginator("list_objects_v2")

        for page in paginator.paginate(Bucket=bucket_name):
            if "Contents" in page:
                objects = [{"Key": obj["Key"]} for obj in page["Contents"]]

                s3.delete_objects(
                    Bucket=bucket_name,
                    Delete={"Objects": objects}
                )

        s3.delete_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' deleted successfully.")

    except NoCredentialsError:
        print("AWS credentials not available.")
    except ClientError as e:
        print(f"AWS error: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    delete_s3_bucket("my-unique-bucket-name-12345")

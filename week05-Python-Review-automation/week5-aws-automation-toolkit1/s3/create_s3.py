import boto3
from botocore.exceptions import ClientError, NoCredentialsError 

def create_s3_bucket(bucket_name, region=None):
    s3 = boto3.client("s3", region_name=region)
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name,
                             CreateBucketConfiguration=location)
        print(f"S3 bucket '{bucket_name}' created successfully.")
        
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    create_s3_bucket("my-unique-bucket-name-12345", region="us-west-2")  # Replace with your desired bucket name and region
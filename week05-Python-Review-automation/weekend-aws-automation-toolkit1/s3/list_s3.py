import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def list_s3_buckets():
    s3 = boto3.client("s3")
    try:
        response = s3.list_buckets()
        buckets = response.get('Buckets', [])
        
        if not buckets:
            print("No S3 buckets found.")
            return

        print("S3 Buckets:")
        for bucket in buckets:
            print(f"  - {bucket['Name']}")
            
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    list_s3_buckets()
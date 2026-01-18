import boto3
from botocore.exceptions import ClientError, NoCredentialsError

VPC_CIDR = "10.0.0.0/16"
VPC_NAME = "week6-demo-vpc"

def create_vpc():
    ec2 = boto3.client("ec2")

    try:
        response = ec2.create_vpc(CidrBlock=VPC_CIDR)

        vpc_id = response["Vpc"]["VpcId"]

        ec2.create_tags(
            Resources=[vpc_id],
            Tags=[{"Key": "Name", "Value": VPC_NAME}]
        )

        print(f"VPC created successfully: {vpc_id}")

    except NoCredentialsError:
        print("AWS credentials not available.")     
    except ClientError as e:
        print(f"AWS error: {e}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    create_vpc()

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# Replace CIDR as needed
VPC_CIDR = "10.0.0.0/16"

def create_vpc():
    try:
        ec2 = boto3.client("ec2")
        
        # Create VPC
        response = ec2.create_vpc(CidrBlock=VPC_CIDR)
        vpc_id = response['Vpc']['VpcId']
        print(f"Created VPC with ID: {vpc_id}")
        
        # Tag the VPC
        ec2.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": "CareerC-VPC"}])
        print(f"Tagged VPC {vpc_id} with Name=CareerC-VPC")
        
        # Create a subnet
        subnet_response = ec2.create_subnet(
            VpcId=vpc_id,
            CidrBlock="10.0.1.0/24"
        )
        subnet_id = subnet_response['Subnet']['SubnetId']
        print(f"Created subnet {subnet_id} in VPC {vpc_id}")
        
        # Tag the subnet
        ec2.create_tags(Resources=[subnet_id], Tags=[{"Key": "Name", "Value": "CareerC-Subnet"}])
        print(f"Tagged subnet {subnet_id} with Name=CareerC-Subnet")
        
    except NoCredentialsError:
        print("AWS credentials not available.")
    except ClientError as e:
        print(f"An AWS error occurred: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    create_vpc()

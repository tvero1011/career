import boto3
from botocore.exceptions import ClientError

VPC_ID = "vpc-xxxxxxxx"   # replace with YOUR VPC ID

PUBLIC_SUBNET_CIDR = "10.0.1.0/24"
PRIVATE_SUBNET_CIDR = "10.0.2.0/24"
AVAILABILITY_ZONE = "ap-southeast-1a"  # change if needed

def create_subnets():
    ec2 = boto3.client("ec2")

    try:
        public_subnet = ec2.create_subnet(
            VpcId=VPC_ID,
            CidrBlock=PUBLIC_SUBNET_CIDR,
            AvailabilityZone=AVAILABILITY_ZONE
        )

        public_subnet_id = public_subnet["Subnet"]["SubnetId"]

        ec2.create_tags(
            Resources=[public_subnet_id],
            Tags=[{"Key": "Name", "Value": "week6-public-subnet"}]
        )

        private_subnet = ec2.create_subnet(
            VpcId=VPC_ID,
            CidrBlock=PRIVATE_SUBNET_CIDR,
            AvailabilityZone=AVAILABILITY_ZONE
        )

        private_subnet_id = private_subnet["Subnet"]["SubnetId"]

        ec2.create_tags(
            Resources=[private_subnet_id],
            Tags=[{"Key": "Name", "Value": "week6-private-subnet"}]
        )

        print("Subnets created successfully:")
        print(f"Public Subnet: {public_subnet_id}")
        print(f"Private Subnet: {private_subnet_id}")

    except ClientError as e:
        print(f"AWS error: {e}")

if __name__ == "__main__":
    create_subnets()

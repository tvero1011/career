regions = ["us-east-1", "ap-southeast-1", "eu-west-1"]
ec2_instance = {
    "instance_id": "i-123456",
    "type": "t3.micro",
    "state": "running"
}

for region in regions:
    print(f"Checking resources in {region}")


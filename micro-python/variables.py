name = "tvero"
age = 46
is_cloud_engineer = True

regions = ["us-east-1", "ap-southeast-1", "eu-west-1"]
ec2_instance = {
    "instance_id": "i-123456",
    "type": "t3.micro",
    "state": "running"
}

print(f'{name}, {age}, {is_cloud_engineer}')
name = "tvero"
age = 46
is_cloud_engineer = True
print(type(name), type(age), type(is_cloud_engineer))


regions = ["us-east-1", "ap-southeast-1", "eu-west-1"]
ec2_instance = {
    "instance_id": "i-123456",
    "type": "t3.micro",
    "state": "running"
}
print(regions)
print(ec2_instance["type"])


if ec2_instance["state"] == "running":
    print("Instance is healthy")
else:
    print("Instance is stopped")


for region in regions:
    print(f"Checking resources in {region}")

def describe_instance(instance):
    return f"{instance['instance_id']} is {instance['state']}"

print(describe_instance(ec2_instance))

try:
    print(ec2_instance["launch_time"])
except KeyError:
    print("launch_time not found — safe to continue")
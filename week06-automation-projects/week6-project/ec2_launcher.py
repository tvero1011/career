import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# AWS Account Info
ACCOUNT_ID = "123456789012"
BUDGET_NAME = "CareerC-MonthlyBudget"
CPU_THRESHOLD = 70

# 1️⃣ VPC Creation
def create_vpc():
    ec2 = boto3.client("ec2")
    response = ec2.create_vpc(CidrBlock="10.0.0.0/16")
    vpc_id = response['Vpc']['VpcId']
    ec2.create_tags(Resources=[vpc_id], Tags=[{"Key": "Project", "Value": "CareerC"}])
    print(f"VPC created: {vpc_id}")
    return vpc_id

# 2️⃣ Budget Automation
def create_budget():
    budgets = boto3.client("budgets")
    budget = {
        "BudgetName": BUDGET_NAME,
        "BudgetLimit": {"Amount": "10", "Unit": "USD"},
        "TimeUnit": "MONTHLY",
        "BudgetType": "COST"
    }
    notification = {
        "NotificationType": "ACTUAL",
        "ComparisonOperator": "GREATER_THAN",
        "Threshold": 80,
        "ThresholdType": "PERCENTAGE",
        "NotificationState": "ALARM"
    }
    subscribers = [{"SubscriptionType": "EMAIL", "Address": "your-email@example.com"}]

    budgets.create_budget(
        AccountId=ACCOUNT_ID,
        Budget=budget,
        NotificationsWithSubscribers=[{"Notification": notification, "Subscribers": subscribers}]
    )
    print(f"Budget '{BUDGET_NAME}' created!")

# 3️⃣ Launch EC2 instance
def launch_ec2(vpc_id):
    ec2 = boto3.client("ec2")
    subnet = ec2.create_subnet(VpcId=vpc_id, CidrBlock="10.0.1.0/24")['Subnet']['SubnetId']
    instance = ec2.run_instances(
        ImageId="ami-0c94855ba95c71c99",  # Example Amazon Linux 2 AMI
        InstanceType="t2.micro",
        MaxCount=1,
        MinCount=1,
        SubnetId=subnet
    )['Instances'][0]['InstanceId']
    print(f"EC2 Instance launched: {instance}")
    return instance

# 4️⃣ Monitoring CPU
def create_cpu_alarm(instance_id):
    cloudwatch = boto3.client("cloudwatch")
    alarm_name = f"CareerC-CPU-{instance_id}"
    cloudwatch.put_metric_alarm(
        AlarmName=alarm_name,
        ComparisonOperator="GreaterThanThreshold",
        EvaluationPeriods=1,
        MetricName="CPUUtilization",
        Namespace="AWS/EC2",
        Period=300,
        Statistic="Average",
        Threshold=CPU_THRESHOLD,
        ActionsEnabled=False,
        AlarmDescription=f"CPU alarm for EC2 instance {instance_id}",
        Dimensions=[{"Name": "InstanceId", "Value": instance_id}]
    )
    print(f"CloudWatch alarm created: {alarm_name}")

# Main automation workflow
if __name__ == "__main__":
    try:
        vpc_id = create_vpc()
        create_budget()
        instance_id = launch_ec2(vpc_id)
        create_cpu_alarm(instance_id)
        print("Weekend automation pipeline completed successfully!")

    except NoCredentialsError:
        print("AWS credentials not available.")
    except ClientError as e:
        print(f"AWS error: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

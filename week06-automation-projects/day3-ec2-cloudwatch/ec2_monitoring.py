import boto3
from botocore.exceptions import ClientError, NoCredentialsError

CPU_THRESHOLD = 70  # percent
ALARM_NAME_PREFIX = "CareerC-CPU-Alarm"

def monitor_ec2_instances():
    try:
        ec2 = boto3.client("ec2")
        cloudwatch = boto3.client("cloudwatch")

        # 1️⃣ List all EC2 instances
        response = ec2.describe_instances()
        instance_ids = [
            inst['InstanceId']
            for reservation in response['Reservations']
            for inst in reservation['Instances']
        ]

        if not instance_ids:
            print("No EC2 instances found.")
            return

        print(f"Found EC2 instances: {instance_ids}")

        # 2️⃣ Create CloudWatch CPU alarms
        for i, instance_id in enumerate(instance_ids, start=1):
            alarm_name = f"{ALARM_NAME_PREFIX}-{instance_id}"
            cloudwatch.put_metric_alarm(
                AlarmName=alarm_name,
                ComparisonOperator="GreaterThanThreshold",
                EvaluationPeriods=1,
                MetricName="CPUUtilization",
                Namespace="AWS/EC2",
                Period=300,  # 5 minutes
                Statistic="Average",
                Threshold=CPU_THRESHOLD,
                ActionsEnabled=False,  # No actual action for now
                AlarmDescription=f"CPU alarm for {instance_id}",
                Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
            )
            print(f"Created CloudWatch alarm: {alarm_name}")

    except NoCredentialsError:
        print("AWS credentials not available.")
    except ClientError as e:
        print(f"AWS error: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    monitor_ec2_instances()

import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from datetime import datetime, timedelta

CPU_THRESHOLD = 70  # percent

def fetch_ec2_metrics():
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

        # 2️⃣ Define the time range (last 5 minutes)
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(minutes=5)

        # 3️⃣ Fetch metrics for each instance
        for instance_id in instance_ids:
            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=start_time,
                EndTime=end_time,
                Period=300,  # 5 minutes
                Statistics=['Average']
            )

            if metrics['Datapoints']:
                cpu = metrics['Datapoints'][0]['Average']
                print(f"Instance {instance_id} CPU: {cpu:.2f}%")
                
                if cpu > CPU_THRESHOLD:
                    print(f"⚠️ Warning: CPU of {instance_id} exceeds {CPU_THRESHOLD}%")
            else:
                print(f"No CPU data for {instance_id}")

    except NoCredentialsError:
        print("AWS credentials not available.")
    except ClientError as e:
        print(f"AWS error: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    fetch_ec2_metrics()

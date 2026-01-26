#!/usr/bin/env python3
"""
aws_resource_checker.py
Week 7 — DevOps Portfolio
Checks AWS credentials, Boto3, and basic connectivity
"""

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def check_boto3_version():
    import boto3
    print(f"Boto3 version: {boto3.__version__}")

def check_aws_credentials():
    try:
        # Try to get the current caller identity
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        print("✅ AWS Credentials are configured correctly!")
        print(f"Account: {identity['Account']}")
        print(f"UserId: {identity['UserId']}")
        print(f"ARN: {identity['Arn']}")
    except NoCredentialsError:
        print("❌ AWS credentials not found. Configure them using 'aws configure'.")
    except PartialCredentialsError:
        print("❌ AWS credentials incomplete. Run 'aws configure' to fix.")
    except ClientError as e:
        print(f"❌ AWS Client error: {e}")

def list_s3_buckets():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        buckets = [b['Name'] for b in response.get('Buckets', [])]
        print(f"✅ S3 Buckets found: {buckets if buckets else 'No buckets found.'}")
    except ClientError as e:
        print(f"❌ Could not list S3 buckets: {e}")

if __name__ == "__main__":
    print("=== AWS Resource Checker ===")
    check_boto3_version()
    check_aws_credentials()
    list_s3_buckets()
    print("✅ All checks complete!")

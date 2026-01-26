# AWS Automation Toolkit (Boto3)
## Overview
This project demonstrates AWS automation using Python and Boto3.
It focuses on safe, repeatable automation of IAM and S3 resources.

## Features
- List IAM users
- Create and delete IAM users
- List S3 buckets
- Create and delete S3 buckets
- Safe execution using __main__ guard
- Error handling with botocore exceptions

## Technologies Used
- Python 3
- Boto3
- AWS IAM
- AWS S3

## DevOps Practices Demonstrated
- Infrastructure automation
- Safety-first scripting
- Cleanup of AWS resources

# Week 5 – Python & Boto3 Automation Notes
## Key Patterns Learned
- boto3.client("service")
- API call returns dictionaries
- Use .get("key", []) to avoid crashes
- Wrap AWS calls in try/except
- Use __name__ == "__main__" for safety

## IAM Learnings
- IAM user lifecycle: create → attach policy → delete
- Write actions require cleanup
- AWS-managed policy ARNs are reusable

## S3 Learnings
- Bucket names must be globally unique
- Buckets must be empty before deletion
- Same automation pattern applies across services

## DevOps Insight
- Infrastructure automation
- Safety-first scripting
- Cleanup of AWS resources
- Modular and readable code structure
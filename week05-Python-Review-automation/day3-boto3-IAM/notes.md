# Week 5 Day 3 – IAM Automation Notes

## What this script does
- Connects to AWS IAM using boto3
- Calls list_users API
- Receives response as Python dict
- Safely loops through users
- Prints IAM usernames

## Key learnings
- IAM is a global service
- boto3.client("iam") works like s3 client
- response["Users"] is a list
- Use .get("Users", []) for safety
- Read-only automation first is best practice

## DevOps insight
IAM automation is powerful and dangerous.
Always understand read operations before write/delete.

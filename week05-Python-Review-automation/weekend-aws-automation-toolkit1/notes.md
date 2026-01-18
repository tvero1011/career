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
Once the automation pattern is understood, it applies to any AWS service.
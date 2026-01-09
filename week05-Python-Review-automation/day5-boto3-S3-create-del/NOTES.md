# Week 5 Day 5 – S3 Automation Notes

## What I automated
- Create S3 bucket
- Delete S3 bucket
- Safe, reusable function structure

## Key learnings
- S3 bucket names must be globally unique
- Boto3 patterns are same as IAM: client → call → handle dict → try/except
- Use __main__ guard for safe execution
- Always clean up test resources

## DevOps insight
- Automation pattern = repeatable workflow
- Safe cleanup is critical
- Once you understand the pattern, it works for ANY AWS service

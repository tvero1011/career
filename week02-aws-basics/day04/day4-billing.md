# Week 2 Day 4 — Budget CLI + S3 CLI Basics

## Goal of the Day
Learn how to automate:
- AWS Budgets (create + notifications)
- Basic S3 operations (create bucket, upload, download, delete)
- Understand bucket naming, regions, permissions

This is your first real **AWS automation workflow** touching billing + storage.

# Theory Overview

## AWS Budgets
You can:
- Create cost budgets
- Set alert thresholds
- Trigger email notifications or SNS
- Automate monitoring

## S3 CLI Skills
You will learn:
- Create bucket
- Upload
- Download
- Remove files
- Remove buckets
- Listing bucket contents

S3 is CCP core content and a must for DevOps automation.

# PART 1 — Create a Cost Budget (CLI)

Created budget:
cli-daily-budget
Budget Amount:
$1.00
Budget Type:
COST
Budget Time Unit:
DAILY

### Create budget (CLI):
aws budgets create-budget
--account-id <ACCOUNT-ID>
--budget '{
"BudgetName": "cli-daily-budget",
"BudgetLimit": { "Amount": 1, "Unit": "USD" },
"TimeUnit": "DAILY",
"BudgetType": "COST"
}'

# PART 2 — Add Budget Notification (CLI)

Created SNS email alert:
aws budgets create-notification
--account-id <ACCOUNT-ID>
--budget-name cli-daily-budget
--notification '{
"NotificationType": "FORECASTED",
"ComparisonOperator": "GREATER_THAN",
"Threshold": 80,
"ThresholdType": "PERCENTAGE"
}'
--subscriber '{
"SubscriptionType": "EMAIL",
"Address": "<your-email>"
}'

Alert:
- Type: Forecasted  
- Condition: > 80%  
- Notification: Email  

# PART 3 — Create S3 Bucket (CLI)

Bucket name must be unique globally.
Created:
week2-cli-s3-bucket-<unique-id>

Command:
aws s3 mb s3://week2-cli-s3-bucket-12345

List buckets:
aws s3 ls

# PART 4 — Upload Files to S3 (CLI)

Created test file:
echo "Hello from CLI" > test.txt

Upload:
aws s3 cp test.txt s3://week2-cli-s3-bucket-12345

Verify:
aws s3 ls s3://week2-cli-s3-bucket-12345

# 🛠️ PART 5 — Download Files from S3 (CLI)

aws s3 cp s3://week2-cli-s3-bucket-12345/test.txt downloaded.txt

# PART 6 — Upload Folder (sync)

Created folder:
mkdir upload-folder
echo "file1" > upload-folder/file1.txt
echo "file2" > upload-folder/file2.txt

Sync:
aws s3 sync upload-folder s3://week2-cli-s3-bucket-12345

# PART 7 — Delete Files + Bucket (CLI)

Delete object:
aws s3 rm s3://week2-cli-s3-bucket-12345/test.txt

Delete all:
aws s3 rm s3://week2-cli-s3-bucket-12345 --recursive

Delete bucket:
aws s3 rb s3://week2-cli-s3-bucket-12345

# Summary

Today I learned:
- How to automate AWS Budgets using CLI  
- Creating daily cost alerts  
- How S3 works using CLI  
- Bucket creation, upload, download, sync, delete  
- Real-world DevOps workflows involving storage + cost control  

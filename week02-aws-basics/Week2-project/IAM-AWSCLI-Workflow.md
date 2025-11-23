# Week 2 Weekend Project — Full IAM + CLI Workflow
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

## Goal
Build a complete IAM workflow using **AWS CLI only**.

You will:
1. Create an IAM user (via CLI)
2. Attach policies
3. Create access keys
4. Test permissions
5. List IAM resources
6. Delete everything cleanly
7. Push the documentation to GitHub

This simulates real DevOps automation tasks.

# PREREQUISITES
- AWS CLI installed
- aws configure completed
- IAM admin permissions (your main account)

# PART 1 — Create IAM User (CLI Only)

### Create the user
aws iam create-user --user-name weekend-user

### Verify
aws iam list-users

# PART 2 — Create Login Profile (Optional: If you want console login)

aws iam create-login-profile
--user-name weekend-user
--password "TestPassword123!"
--password-reset-required

# PART 3 — Attach Policy to User

### Attach AWS managed policy (AdministratorAccess)
aws iam attach-user-policy
--user-name weekend-user
--policy-arn arn:aws:iam::aws:policy/AdministratorAccess

### Verify
aws iam list-attached-user-policies --user-name weekend-user

# PART 4 — Create ACCESS KEY (Programmatic Access)

aws iam create-access-key --user-name weekend-user

Save the output:
AccessKeyId: XXXX
SecretAccessKey: XXXX

# PART 5 — Test Using the New Credentials

### Configure temporary profile:
aws configure --profile weekend-test
Paste:
- Access Key
- Secret Key

### Test access (should work):
aws s3 ls --profile weekend-test

# PART 6 — Restrict Permissions (Simulating Real-World Security)

Attach a LIMITED policy:
aws iam attach-user-policy
--user-name weekend-user
--policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess

Detach admin access:
aws iam detach-user-policy
--user-name weekend-user
--policy-arn arn:aws:iam::aws:policy/AdministratorAccess

### Test again:
aws s3 ls --profile weekend-test

### Test EC2 (should fail):
aws ec2 describe-instances --profile weekend-test

Expected output: **AccessDenied**

# PART 7 — Clean Delete Workflow

### 1. Delete access keys:
aws iam list-access-keys --user-name weekend-user
aws iam delete-access-key
--user-name weekend-user
--access-key-id <key>

### 2. Detach all policies:
aws iam list-attached-user-policies --user-name weekend-user
aws iam detach-user-policy
--user-name weekend-user
--policy-arn <policy ARN>

### 3. Delete login profile:
aws iam delete-login-profile --user-name weekend-user

### 4. Delete user:
aws iam delete-user --user-name weekend-user

# PART 8 — Documentation Summary

What I learned:
How IAM users are actually created behind the scenes
How to control permissions using CLI
How to configure multiple AWS profiles
How to test with and without permissions
How to perform clean user removal
How real DevOps teams automate IAM operations

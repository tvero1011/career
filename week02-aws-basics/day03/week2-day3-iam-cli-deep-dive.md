# Week 2 Day 3 — IAM Automation with AWS CLI

## Goal of the Day
Use AWS CLI to manage IAM resources:
- Create users
- Create groups
- Attach policies
- Add users to groups
- Delete users safely
- Understand JSON policy documents

Today is your first real automation day.

#  Theory: Why Automate IAM?

AWS CLI automation allows you to:
- Save time
- Reduce mistakes
- Build infrastructure-as-code habits
- Scale user creation for teams
- Prepare for boto3 automation in Week 5

IAM + CLI is a core CCP exam skill and a real DevOps workflow.

# PART 1 — Create IAM Users (CLI)

Created the following users using CLI:
dev1
dev2
admin1
billing1

Command used:
aws iam create-user --user-name dev1

Created all users similarly.
To list users:
aws iam list-users

# PART 2 — Create IAM Groups (CLI)
Created groups:
developers
admins
billing

Command:
aws iam create-group --group-name developers

List groups:
aws iam list-groups

# PART 3 — Attach Policies to Groups

Developers → EC2 full access:
aws iam attach-group-policy
--group-name developers
--policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess

Admins → Admin Access:
aws iam attach-group-policy
--group-name admins
--policy-arn arn:aws:iam::aws:policy/AdministratorAccess

Billing → Billing:
aws iam attach-group-policy
--group-name billing
--policy-arn arn:aws:iam::aws:policy/job-function/Billing

List attached policies:
aws iam list-attached-group-policies --group-name developers

# PART 4 — Add Users to Groups (CLI)

Add dev1 to developers:
aws iam add-user-to-group --user-name dev1 --group-name developers

Add admin1 to admins:
aws iam add-user-to-group --user-name admin1 --group-name admins

List groups for any user:
aws iam list-groups-for-user --user-name dev1

# PART 5 — Create a Custom Policy (JSON)

Created file:
s3-readonly.json
Content:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": "*"
    }
  ]
}

Upload policy:
aws iam create-policy \
  --policy-name S3ReadOnlyCLI \
  --policy-document file://s3-readonly.json
Attach to developers:
aws iam attach-group-policy \
  --group-name developers \
  --policy-arn arn:aws:iam::<ACCOUNT-ID>:policy/S3ReadOnlyCLI

#PART 6 — Safe IAM Deletion with CLI

Remove policy:
aws iam detach-group-policy --group-name developers --policy-arn <ARN>

Remove user from group:
aws iam remove-user-from-group --user-name dev1 --group-name developers

Delete login profile (only if user has console password):
aws iam delete-login-profile --user-name dev1

Delete access keys:
aws iam delete-access-key --user-name dev1 --access-key-id <KEY-ID>

Finally delete user:
aws iam delete-user --user-name dev1

# Screenshots
<img width="757" height="177" alt="cli-create" src="https://github.com/user-attachments/assets/1c1daf58-4216-4398-9fd1-425353ce735c" />
<img width="637" height="574" alt="cli-list-users" src="https://github.com/user-attachments/assets/222bce9a-708a-40d8-a043-4542ca31c6b6" />
<img width="698" height="448" alt="cli-list-groups" src="https://github.com/user-attachments/assets/1df2db6b-716c-4a4e-ac74-bd855005eb83" />
<img width="758" height="71" alt="cli-delete" src="https://github.com/user-attachments/assets/76f70c68-d9e6-47ad-b195-f9eef4383754" />

#Summary
Today I learned:
How to automate IAM using AWS CLI
Creating users, groups, and policies via commands
Attaching policies and adding users to groups
Creating JSON policy files
Safe deletion workflow for IAM resources

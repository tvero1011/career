I performed a full IAM security hardening exercise on my AWS account.
Key tasks included enforcing MFA on the root account, building structured IAM user groups, and deploying custom JSON IAM policies.
I configured the AWS CLI and executed programmatic IAM operations to validate access controls.
All security configurations, terminal outputs, and screenshots were documented in my GitHub project for auditability.

----Screenshots------

## Root MFA
<img width="692" height="623" alt="root-MFA" src="https://github.com/user-attachments/assets/2a960999-bac0-48d2-a6a9-e678a53fdb4b" />

## IAM password policy
<img width="971" height="605" alt="iam-password-policy" src="https://github.com/user-attachments/assets/6ba5e0dd-a177-4d0f-8273-7f487c217140" />

## IAM architecture diagram
<img width="418" height="667" alt="iam-diag" src="https://github.com/user-attachments/assets/2bc3ad93-bd1f-434f-b807-f4d29dc61de5" />

## IAM Users
<img width="671" height="698" alt="dev-user" src="https://github.com/user-attachments/assets/2cf941b9-1a12-4443-9a40-b290c79d9831" />
<img width="671" height="662" alt="billing-user" src="https://github.com/user-attachments/assets/e354e872-30d7-4316-8d6d-03c3a9be5f4d" />
<img width="678" height="709" alt="admin-user" src="https://github.com/user-attachments/assets/67c434c3-153a-4b43-a0e0-43bc18ec7b78" />

## IAM Users credentials
<img width="681" height="756" alt="dev-user-credentials" src="https://github.com/user-attachments/assets/4cfbb44b-51b6-47e9-8c63-8c118bc6aff4" />
<img width="680" height="680" alt="biiling-user-credentials" src="https://github.com/user-attachments/assets/849281e0-cba8-4c36-b11e-fff08d40abac" />
<img width="675" height="689" alt="admin-user-credentials" src="https://github.com/user-attachments/assets/3db2dde3-4097-4374-bdf0-8f97e0dd6940" />

## IAM Groups
<img width="691" height="631" alt="dev-group-user" src="https://github.com/user-attachments/assets/eaea3391-6534-4856-a0a1-a52722cbc621" />
<img width="696" height="632" alt="billing-group-user" src="https://github.com/user-attachments/assets/c1d3c8fd-4297-42e9-a5ef-0dc312633ece" />
<img width="703" height="652" alt="admin-group-user" src="https://github.com/user-attachments/assets/667684c4-bf29-4c69-b1f2-9c0315d4891a" />

## IAM Groups policy
<img width="753" height="734" alt="dev-group-attach-custompolicy" src="https://github.com/user-attachments/assets/a50ddccf-fb7b-426e-a41e-2b927a175d19" />
<img width="694" height="649" alt="billing-group-policy" src="https://github.com/user-attachments/assets/757f1cf8-781f-4135-a602-cbe320b3c7c2" />
<img width="686" height="650" alt="admin-group-policy" src="https://github.com/user-attachments/assets/dee83382-ca8c-4bdb-a4df-1bb0422bb7bf" />
<img width="695" height="692" alt="dev-group-policy" src="https://github.com/user-attachments/assets/45dd1200-6b76-4776-a62f-3fd78b3687bf" />


## Custom IAM Policy
<img width="766" height="520" alt="policy_S3ReadOnly" src="https://github.com/user-attachments/assets/85f8c92f-23f1-4e44-917c-071ef4367189" />
<img width="763" height="544" alt="policy_EC2StartStop" src="https://github.com/user-attachments/assets/cb48de91-7e1b-43dc-b090-f78e06bce7e6" />

## AWS CLI Output
<img width="637" height="574" alt="cli-list-users" src="https://github.com/user-attachments/assets/15e73537-cad9-4a38-a8e5-a2e8ecb40be4" />
<img width="698" height="448" alt="cli-list-groups" src="https://github.com/user-attachments/assets/69daa52e-d1d2-4df5-a583-e8b839da37fd" />
<img width="503" height="916" alt="cli-budgets" src="https://github.com/user-attachments/assets/f8e314a4-ea09-4df5-81fc-c751f091890f" />

## AWS CLI CREATE-DELETE USERS
<img width="757" height="177" alt="cli-create" src="https://github.com/user-attachments/assets/a75cc9e8-6487-4a5d-95c4-88e959c5d7b3" />
<img width="758" height="71" alt="cli-delete" src="https://github.com/user-attachments/assets/d3de24f2-4ae7-43ef-a1a4-265aa9afa773" />

## Billing Preferences
<img width="675" height="521" alt="billing-pref" src="https://github.com/user-attachments/assets/cbc68933-98b1-4870-862a-cf91b8de11d5" />

## Billing Dashboard – Budgets
<img width="434" height="692" alt="budget-setup" src="https://github.com/user-attachments/assets/a43fb96c-6ab9-4ddf-9fa1-602cf615a561" />


## SNS Subscription
<img width="1080" height="769" alt="sns-subscription" src="https://github.com/user-attachments/assets/be68cce6-b2fb-40a5-a2bb-14e2b286c8e8" />


## CODE BLOCK

# AWS version
aws --version

# Configure AWS CLI
aws configure --profile admin-student

# List IAM users
aws iam list-users --profile admin-student > cli-list-users.jsont
aws iam list-groups --profile admin-student > cli-list-groups.json

# Create Demo CLI User
aws iam create-user --user-name cli-demo --profile admin-student

# Delete Demo User
aws iam create-user --user-name cli-demo --profile admin-student

# Create an IAM group
aws iam create-group --group-name student --profile admin-student

# Verify Identity
aws sts get-caller-identity --profile admin-student

# List Attached Policies
aws iam list-attached-user-policies \
  --user-name cli-demo \
  --profile admin-student

# Attach Policy to Demo User
aws iam attach-user-policy \
  --user-name cli-demo \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess \
  --profile admin-student

# Detach Policy to Demo User
aws iam detach-user-policy \
  --user-name cli-demo \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess \
  --profile admin-student

# Add user to group
aws iam add-user-to-group \
  --user-name cli-test-user \
  --group-name DevOpsGroup

# Describe Budgets
aws sts get-caller-identity --profile admin-student
aws budgets describe-budgets \
  --account-id <ID> \
  --region us-east-1 \
  --profile admin-student

# Catch Errors into File (Debugging)
aws iam list-users --profile admin-student > cli-list-users.json 2>&1

## SECURITY CONFIGURATIONS

Enabled MFA on root account

Removed existing root access keys

Created separate IAM admin user

Created IAM groups for role-based access

Applied least-privilege IAM policies

Created a custom JSON policy for specific permissions

Enforced strong password policy

Enabled AWS Budgets + email alerts

Configured SNS for budget notifications

Verified IAM access via AWS CLI

Ensured no wide “*:*” permission policies

Audited IAM users and removed unused access keys



## Findings

Root account had no MFA enabled (now fixed).

No structured IAM groups existed (added).

Some services had overly permissive IAM settings (corrected).

No billing alert or budget monitoring was configured (now set up).

IAM activity was not being monitored via CLI previously (now validated).

## Recommendations

Continue enforcing least-privilege for every new user or service.

Use IAM roles instead of long-term access keys whenever possible.

Rotate credentials every 90 days.

Periodically review IAM policies for unused permissions.

Enable CloudTrail and CloudWatch alarms in Week 11 for full auditing.

Use tagging standards (Owner, Environment, Purpose) to improve cost management.

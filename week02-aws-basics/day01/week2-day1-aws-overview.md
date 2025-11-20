# Week 2 Day 1 — IAM Advanced

##  Goal of the Day
Deepen understanding of:
- IAM users, groups, roles, policies  
- Inline vs managed policies  
- Policy evaluation logic  
- STS + temporary credentials  
- IAM best practices

Hands-on:
- Create IAM groups and attach policies
- Create custom IAM policy (JSON)
- Role creation + trust policy
- Review IAM security best practices


# IAM Theory Summary

## IAM Users  
Identity representing a human.

## IAM Groups  
Collection of users that share permissions.

Examples:
Admins
Developers
Billing


## IAM Roles  
Identity *without password*. Used by:
- EC2
- Lambda
- AWS services
- External users

Contains:
- Permission policy  
- Trust policy (who can assume the role)

# Managed vs Inline Policies

### Managed (recommended)
- Reusable
- Versioned
- AWS-maintained or customer-managed

### Inline (not recommended)
- Attached to a single principal only

# Policy Evaluation Logic

AWS checks:
1. **Explicit Deny** → always wins  
2. **Explicit Allow** → granted only if no deny  
3. **Default Deny** → everything denied unless allowed  

# PART 1 — Create IAM Groups

Created groups:
admin-group
developer-group
billing-group

Attached policies:
Admin: AdministratorAccess
Developer: AmazonEC2FullAccess
Billing: Billing

# PART 2 — Create IAM Users

Users created today:
admin-user
dev-user
billing-user

Added to groups:
admin-user → admin-group
dev-user → developer-group
billing-user → billing-group

Enabled MFA:
- Virtual MFA App → enforced

# PART 3 — Create a Custom Policy (JSON)

Policy name:
DevReadOnlyS3
JSON:
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

Attached to:
developer-group

# PART 4 — Create an IAM Role

Role name:
EC2-S3-Access-Role
Trust relationship:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "ec2.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}

Permissions attached:
AmazonS3ReadOnlyAccess
Use case: Allows EC2 instance to read S3 buckets.

# IAM Best Practices Implemented
Enforced MFA on all users
Least privilege access
Used groups instead of attaching policies directly to users
Avoided inline policies
Created role instead of access keys for EC2

# Screenshots
## Groups
<img width="696" height="632" alt="billing-group-user" src="https://github.com/user-attachments/assets/d2743836-388d-47c8-bdd2-07745d070ab6" />
<img width="703" height="652" alt="admin-group-user" src="https://github.com/user-attachments/assets/313dd784-640d-4280-9467-953dafd51bc8" />
<img width="691" height="631" alt="dev-group-user" src="https://github.com/user-attachments/assets/cdde6546-52de-4ebe-bb37-e6ab59aca424" />

## Users
<img width="671" height="698" alt="dev-user" src="https://github.com/user-attachments/assets/a8900b49-5011-4428-aece-5d60e5dccb68" />
<img width="671" height="662" alt="billing-user" src="https://github.com/user-attachments/assets/e0841b28-d79f-409d-a9cd-1d21f718795c" />
<img width="678" height="709" alt="admin-user" src="https://github.com/user-attachments/assets/261cdadc-45a5-458d-b067-39bc964ce152" />

## Policy
<img width="695" height="692" alt="dev-group-policy" src="https://github.com/user-attachments/assets/8c964c22-789a-41a5-831d-d04d4e4056cd" />
<img width="694" height="649" alt="billing-group-policy" src="https://github.com/user-attachments/assets/bdf6329c-5cf0-4470-8d31-888ca057184a" />
<img width="686" height="650" alt="admin-group-policy" src="https://github.com/user-attachments/assets/fa2cc8d1-09bd-429c-9c39-65d4468c9cff" />
<img width="753" height="734" alt="dev-group-attach-custompolicy" src="https://github.com/user-attachments/assets/d55c8eb5-5530-42d9-8d95-d2acc6dfd7fa" />

## Credentials
<img width="675" height="689" alt="admin-user-credentials" src="https://github.com/user-attachments/assets/17a3e6a6-e586-43ca-b157-ff25dc23f9e5" />
<img width="681" height="756" alt="dev-user-credentials" src="https://github.com/user-attachments/assets/eb4de065-6543-4362-9e00-995bbdf210fe" />
<img width="680" height="680" alt="biiling-user-credentials" src="https://github.com/user-attachments/assets/93b14341-f09d-46c0-b650-53e81ac5820a" />


# Summary
Today I mastered IAM beyond basics:
Created groups, users, roles
Attached both AWS-managed and custom policies
Understood IAM best practices and policy evaluation logic
Prepared for CLI automation (Day 2–4)

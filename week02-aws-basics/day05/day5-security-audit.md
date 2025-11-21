# Week 2 Day 5 — AWS Organizations + Consolidated Billing

## Goal of the Day
Understand:
- AWS Organizations structure
- Management Account vs Member Accounts
- Consolidated Billing
- Service Control Policies (SCP)
- Best practices for multi-account setups
- How this connects to CCP exam + DevOps workflows

No CLI today — pure theory.

# PART 1 — What is AWS Organizations?

AWS Organizations = service to **group and manage multiple AWS accounts**.

You create:
- **Management Account** (root of all)
- **Member Accounts** (child accounts)

Allows:
- Centralized billing
- Centralized guardrails
- Centralized security
- Separation of workloads

# PART 2 — Organization Structure

Hierarchy looks like this:
Organization
│
├── Management Account
│
├── Organizational Units (OU)
│ ├── Dev OU
│ │ ├── dev-account-1
│ │ ├── dev-account-2
│ │
│ ├── Prod OU
│ ├── prod-account-1
│ ├── prod-account-2
│
└── Security OU
├── logging-account
├── audit-account

# PART 3 — Key Concepts

### 1. **Root**
Top of the org. Every OU and account sits under it.

### 2. **Management Account**
- Formerly called “Master Account”
- FULL control
- Pays all bills
- Cannot be restricted by SCP

### 3. **Member Accounts**
- Created or invited
- Can be restricted by SCP
- Separated for isolation + security

### 4. **Organizational Units (OU)**
Folders for grouping accounts.

Use cases:
- Separate **dev**, **test**, **prod**
- Apply different guardrails

# PART 4 — Consolidated Billing (High-Value CCP Topic)

Benefits:
1. **One bill** for all accounts  
2. **No extra cost**  
3. **Share discounts**:
   - Savings Plans  
   - Reserved Instances  
   - Volume discounts  
4. **Centralized budget + billing alerts**

### Example:

If Dev account uses 200 GB of S3  
and Prod account uses 500 GB

Total = 700 GB  
Billing tier is applied to combined usage → cheaper.


# PART 5 — Service Control Policies (SCP)

SCPs are **organization-level guardrails**.
What they do:
- Restrict what accounts *can do*
- Apply at root, OU, or account level

Important notes:
- They DO NOT grant permissions
- They ONLY DENY
- They apply to **all IAM users + roles in that account**

### Example SCP (Deny Leaving Org)
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "DenyLeavingOrganization",
"Effect": "Deny",
"Action": "organizations:LeaveOrganization",
"Resource": "*"
}
]
}

# PART 6 — Real DevOps Use Cases

### 1. Security Account  
Stores logs from all accounts via CloudTrail, Config.

### 2. Sandbox Accounts  
Developers test without touching prod.

### 3. Prod Isolated  
Production in its own OU with strict SCP.

### 4. Centralized Cost Control  
Budgets + alerts applied at Org level.

# 📘 NOTES for CCP Exam

Exam loves asking:
- Who pays the bill?  
  → Management account  
- Does consolidated billing cost extra?  
  → No  
- Do SCPs override IAM policies?  
  → Yes (SCP denies win over IAM allows)
- Do SCPs apply to management accounts?  
  → No  
- What happens if you deny `ec2:*` in SCP?  
  → No one in that account can use EC2

# SUMMARY

Today I learned:
- Organizations structure (root → OU → accounts)  
- Management vs Member accounts  
- How consolidated billing works  
- Sharing discounts  
- SCP purpose + examples  
- Real DevOps use cases for multi-account setups  

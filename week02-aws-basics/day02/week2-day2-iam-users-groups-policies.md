# Week 2 Day 2 — AWS CLI Installation

## Goal of the Day
Install, configure, and verify AWS CLI on your local machine.
Learn:
- What AWS CLI is
- Programmatic access
- Access keys
- AWS credentials file
- CLI configuration profiles

Hands-on:
- Install AWS CLI v2
- Configure credentials (`aws configure`)
- Verify access with sample commands
- Create & use named profiles

# Theory: What is AWS CLI?

AWS CLI is a command-line tool to:
- Manage AWS resources
- Automate workflows
- Run scripts (Bash/Python)
- Replace manual console actions
It uses programmatic credentials (Access Key + Secret Key), stored securely in:

~/.aws/credentials
~/.aws/config

# PART 1 — Install AWS CLI v2

## For Windows:
Downloaded MSI → Installed  
Verify:
aws --version

## For macOS:
brew install awscli

## For Linux:
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip
unzip awscliv2.zip
sudo ./aws/install

# PART 2 — Create IAM Programmatic User

Created IAM user:
cli-user

Enabled:
- Programmatic access (Access key)

Attached policy:
AdministratorAccess (temporary for learning)

Downloaded:
- Access Key ID
- Secret Access Key

Stored securely.

# PART 3 — Configure AWS CLI

Ran:
aws configure
Entered:
- AWS Access Key  
- AWS Secret Access Key  
- Default region: `ap-southeast-1`
- Output format: `json`

CLI automatically created:

~/.aws/credentials
~/.aws/config

# PART 4 — Verify Installation

Verified identity:
aws sts get-caller-identity

Output:
- User ARN
- Account ID

Checked S3 (even if empty):
aws s3 ls

Checked region:
aws configure list

# PART 5 — Create a Named Profile

Created:
dev-profile

Command:
aws configure --profile dev-profile

Verify:
aws sts get-caller-identity --profile dev-profile

# Useful Commands Learned

aws help
aws <service> help
aws ec2 describe-instances
aws iam list-users
aws s3 ls

# Summary
Today I successfully:
- Installed AWS CLI on my system  
- Created a programmatic IAM user  
- Configured access keys  
- Verified the CLI works  
- Learned how profiles and AWS config files work  

# Week 5 Day 4 – IAM User Automation

## What I automated
- Created IAM user via Python
- Attached AWS managed ReadOnlyAccess policy
- Detached policy
- Deleted IAM user safely

## Key IAM rules learned
- Users cannot be deleted with policies attached
- Detach policies before delete
- IAM write actions are dangerous without cleanup

## DevOps insight
IAM automation must follow correct dependency order.
Always automate cleanup to avoid security risks.
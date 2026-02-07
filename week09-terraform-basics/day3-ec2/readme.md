# Week 9 – Day 3: EC2 in VPC with Terraform

## Architecture
- Custom VPC
- Public subnet
- EC2 with Security Group
- IAM Role (no hardcoded credentials)

## Security
- SSH restricted to my IP
- HTTP open to public
- IAM role attached to EC2

## SAA Key Takeaways
- EC2 must live in a subnet
- Security Groups are stateful
- IAM roles replace access keys

## Interview Notes
This setup demonstrates secure, repeatable EC2 deployment using IaC.

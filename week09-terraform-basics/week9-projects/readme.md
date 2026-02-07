# Week 9 Weekend Project — Reusable EC2 Module + Security Groups

## Architecture Decisions
- EC2 instance is created via reusable module
- Security group is separate module for reusability
- Variables make the module environment-agnostic
- Outputs provide instance ID and public IP for other modules or automation

## SAA Considerations
- Security: least privilege SG rules, private subnets optional
- Scalability: module can be reused for multiple instances or ASG
- HA: deploy across multiple AZs in future by changing subnet variables
- Predictability: Terraform plan shows all changes before apply

## Usage
- Update `vpc_id`, `subnet_id`, `ami_id` in root module
- Run `terraform init`, `terraform plan`, `terraform apply`
- Outputs show EC2 ID and public IP

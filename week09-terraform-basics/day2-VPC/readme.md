# Week 9 – Day 2: VPC with Terraform

## Architecture
- Custom VPC (10.0.0.0/16)
- Public subnet (10.0.1.0/24)
- Internet Gateway
- Public route table

## Terraform Resources Used
- aws_vpc
- aws_subnet
- aws_internet_gateway
- aws_route_table

## SAA Key Takeaways
- Public subnet requires IGW routing
- Subnets control IP allocation
- Terraform enforces repeatable networking

## Cost Considerations
- VPC and IGW are free
- NAT Gateways incur cost (not used)

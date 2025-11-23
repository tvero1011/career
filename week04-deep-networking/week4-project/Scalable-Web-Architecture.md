# Week 4 Weekend Project — Scalable Web Architecture

## Objective
This project builds a fully functional, highly available, auto-healing web architecture using:
- **VPC**
- **Public & Private Subnets**
- **Internet Gateway**
- **NAT Gateway**
- **Application Load Balancer (ALB)**
- **Target Groups**
- **Auto Scaling Group (ASG)**
- **EC2 instances (private subnets)**

This mirrors a real-world AWS production setup.

## Final Architecture Diagram
<img width="1024" height="1536" alt="9e900f74-1a2f-476e-a34f-34ea2c843697" src="https://github.com/user-attachments/assets/33c5d737-ac43-47bc-8124-7272e9f8d971" />

# 1. VPC + Subnets
- VPC created (CIDR /16)
- 2 public + 2 private subnets
- Public subnets route: IGW
- Private subnets route: NAT Gateway

# 2. Launch Template
- AMI used: week3-nginx-ami
- Instance type: t2.micro
- Security group: allow ALB only
- User data:

#!/bin/bash
sudo yum install -y nginx
sudo systemctl start nginx
echo "<h1>Server: $(hostname)</h1>" > /usr/share/nginx/html/index.html


# 3. Auto Scaling Group
- Subnets: private
- Min=2, desired=2, max=4
- Attached to target group
- Health checks: EC2 + ELB

# 4. Application Load Balancer
- Internet-facing
- Hosts public traffic
- Listener 80 → target group

# 5. Verification
- ALB DNS loads Nginx page
- Refresh shows different instances
- ASG scales when CPU increases

# 6. Screenshots
- VPC
- <img width="710" height="379" alt="vpc" src="https://github.com/user-attachments/assets/28185bf7-f079-4926-8811-a2bb063b9792" />

- Subnets
- <img width="722" height="233" alt="subnets" src="https://github.com/user-attachments/assets/c3cb483e-2def-44cc-a1a3-a8a38e959d74" />

- Route tables
- <img width="723" height="225" alt="routes" src="https://github.com/user-attachments/assets/2aa1bf9f-e6d9-42e7-b137-8b60e37f371e" />

- IGW
- <img width="715" height="199" alt="igw" src="https://github.com/user-attachments/assets/49fab2dd-9c1a-4bf3-9ee5-45160143ddb6" />

- NAT Gateway
- <img width="725" height="363" alt="nat" src="https://github.com/user-attachments/assets/bf81e4f3-d4c9-4daa-9e14-ce8f72be5564" />

- ALB
- <img width="688" height="486" alt="alb" src="https://github.com/user-attachments/assets/be090991-11eb-41c2-ad11-40c9af8cb404" />

- Target Group
- <img width="702" height="488" alt="tg" src="https://github.com/user-attachments/assets/40f4e0ad-7cc0-4763-bda0-48f2de567d35" />

- ASG
<img width="669" height="752" alt="asg" src="https://github.com/user-attachments/assets/a94dd27e-bdcc-4a41-b884-a1eb10cc67f7" />

# 7. Summary
This architecture is used in real companies for highly available and fault-tolerant web applications.
I now understand:
- VPC networking
- Load Balancing
- Auto Scaling
- NAT + IGW
- Web traffic flow in AWS

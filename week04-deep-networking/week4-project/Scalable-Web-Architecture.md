# Week 4 Weekend Project — Scalable Web Architecture

## Objective
Build a production-grade scalable architecture using VPC, ALB, ASG, and NAT.

## Final Architecture Diagram
<insert image here>

---

# 1. VPC + Subnets
- VPC created (CIDR /16)
- 2 public + 2 private subnets
- Public subnets route: IGW
- Private subnets route: NAT Gateway

---

# 2. Launch Template
- AMI used: week3-nginx-ami
- Instance type: t2.micro
- Security group: allow ALB only
- User data:
bash
Copy code
#!/bin/bash
sudo yum install -y nginx
sudo systemctl start nginx
echo "<h1>Server: $(hostname)</h1>" > /usr/share/nginx/html/index.html
yaml
Copy code
---

# 3. Auto Scaling Group
- Subnets: private
- Min=2, desired=2, max=4
- Attached to target group
- Health checks: EC2 + ELB

---

# 4. Application Load Balancer
- Internet-facing
- Hosts public traffic
- Listener 80 → target group

---

# 5. Verification
- ALB DNS loads Nginx page
- Refresh shows different instances
- ASG scales when CPU increases

---

# 6. Screenshots
<Insert screenshots of:
- VPC
- Subnets
- Route tables
- IGW
- NAT Gateway
- ALB
- Target Group
- ASG
>

---

# 7. Summary
This architecture is used in real companies for highly available and fault-tolerant web applications.
I now understand:
- VPC networking
- Load Balancing
- Auto Scaling
- NAT + IGW
- Web traffic flow in AWS
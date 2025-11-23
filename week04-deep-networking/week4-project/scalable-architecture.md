# Week 4 Project — Scalable Web Architecture on AWS

![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

This project builds a fully functional, highly available, auto-healing web architecture on AWS. It demonstrates modern cloud design patterns using:
- VPC (custom networking)
- Public & Private Subnets
- Internet Gateway (IGW)
- NAT Gateway
- Application Load Balancer (ALB)
- Target Groups
- Launch Templates
- Auto Scaling Groups (ASG)
- EC2 in private subnets

---

## Architecture Overview

<img width="1024" height="1536" alt="9e900f74-1a2f-476e-a34f-34ea2c843697" src="https://github.com/user-attachments/assets/06922295-9c25-4897-9e30-ffca55ca0784" />

This represents a production-style AWS web architecture supporting **high availability**, **automatic scaling**, and **secure private networking**.

## Project Components

| Component | Purpose |
|----------|----------|
| **VPC (10.0.0.0/16)** | Custom network space |
| **Public Subnets** | Host ALB + NAT Gateway |
| **Private Subnets** | Host EC2 App Servers |
| **Internet Gateway** | Allows inbound/outbound internet for ALB & NAT |
| **NAT Gateway** | Provides outbound-only internet for EC2 in private subnets |
| **ALB** | Public entry point, distributes traffic |
| **Target Group** | Performs health checks and routes to EC2 |
| **Launch Template** | Defines EC2 blueprint for ASG |
| **Auto Scaling Group** | Automatically creates, replaces, and scales EC2 |

---

## Step-by-Step Build

### **Create VPC & Subnets**
- Create VPC: `10.0.0.0/16`
- Create 2 Public Subnets (AZ A, B)
- Create 2 Private Subnets (AZ A, B)

✔ Public Subnets → Route to **IGW**  
✔ Private Subnets → Route to **NAT Gateway**

---

### **Internet Gateway (IGW)**
- Create IGW
- Attach it to your VPC

---

### **NAT Gateway**
- Create in Public Subnet A
- Allocate Elastic IP
- Add route in Private Route Table:
```
0.0.0.0/0 → NAT Gateway
```

---

### **Route Tables**

#### Public Route Table
```
0.0.0.0/0 → Internet Gateway
```

#### Private Route Table
```
0.0.0.0/0 → NAT Gateway
```

### **Create Application Load Balancer**
- Type: Application Load Balancer
- Scheme: Internet-facing
- Subnets: Public Subnet A & B

**ALB Security Group**:
```
Allow HTTP (80) from 0.0.0.0/0
```
---

### **Create Target Group**
- Type: Instance
- Port: 80
- Health Check Path: `/`

---

### **Create Launch Template**
- Name: `App-LT`
- AMI used: amazon-linux
- Instance type: t2.micro
- Security group: allow ALB only

---

**User Data:**
```bash
#!/bin/bash
sudo yum install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx
echo "<h1>Server: $(hostname)</h1>" | sudo tee /usr/share/nginx/html/index.html
```

**Security Group:**
```
Allow HTTP (80) FROM ALB-SG only
```

---

### **8️⃣ Create Auto Scaling Group**
- Attach Launch Template
- Desired Capacity: 2
- Minimum: 2
- Maximum: 4
- Subnets: Private A & Private B
- Attach Target Group

ASG should automatically launch **two EC2 instances**.

---

### **9️⃣ Clean Up Temporary EC2 Instances**
If you used temporary EC2 for testing:
- Deregister from Target Group
- Terminate instance

ASG will maintain your desired instance count.

---

## Testing Checklist

### ALB DNS Test
Open:
```
http://your-alb-dns.amazonaws.com
```
You should see hostname responses switching between servers.

### Auto-Healing Test
1. Terminate an ASG EC2 instance
2. ASG launches a new one automatically
3. Target Group turns **healthy** again

### Multi-AZ High Availability Test
Confirm:
- EC2 instance in Private Subnet A
- EC2 instance in Private Subnet B

---

## Key Learnings
- Difference between IGW & NAT Gateway
- Designing multi-AZ architectures
- How ALB + ASG provide high availability
- Using Launch Templates to automate EC2 builds
- Understanding health checks & auto-healing
- Proper use of private/public route tables
- Why EC2 in private subnets require NAT

---

## 📸 Screenshots / Evidence
<img width="710" height="379" alt="vpc" src="https://github.com/user-attachments/assets/cfe38525-5e5e-4f38-b967-0e661f02e990" />
<img width="722" height="233" alt="subnets" src="https://github.com/user-attachments/assets/543f998f-b581-45a5-97cb-164e4a4068e8" />
<img width="723" height="225" alt="routes" src="https://github.com/user-attachments/assets/3e98d605-426d-412d-a8ea-a5eb7b6480e3" />
<img width="715" height="199" alt="igw" src="https://github.com/user-attachments/assets/df4e9032-298c-4cae-8108-baa28794b98c" />
<img width="725" height="363" alt="nat" src="https://github.com/user-attachments/assets/3736d28e-84c2-458b-bb84-c97cf22ab9a4" />
<img width="702" height="488" alt="tg" src="https://github.com/user-attachments/assets/9582f421-1595-4437-8535-ec3c601b5626" />
<img width="688" height="486" alt="alb" src="https://github.com/user-attachments/assets/4f2860b3-a3e1-4e8e-bd08-a434ca9c46a2" />
<img width="669" height="752" alt="asg" src="https://github.com/user-attachments/assets/74f78d6f-4dd0-4056-b1f2-050f3302e599" />


## Project Completed
You have successfully built a **production-style**, **scalable**, **fault-tolerant** web architecture on AWS.

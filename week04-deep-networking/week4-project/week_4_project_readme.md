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

## 📘 Architecture Overview

```
Internet
   │
   ▼
Application Load Balancer (Public Subnets)
   │
   ▼
Target Group
   │
   ▼
Auto Scaling Group
 ┌───────┴────────┐
 ▼                ▼
EC2 (Private A)  EC2 (Private B)
   │                │
   └───────┬────────┘
           ▼
     NAT Gateway (Public Subnet)
           ▼
        Internet
```

This represents a production-style AWS web architecture supporting **high availability**, **automatic scaling**, and **secure private networking**.

---

## 📁 Project Components

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

## 🧱 Step-by-Step Build

### **1️⃣ Create VPC & Subnets**
- Create VPC: `10.0.0.0/16`
- Create 2 Public Subnets (AZ A, B)
- Create 2 Private Subnets (AZ A, B)

✔ Public Subnets → Route to **IGW**  
✔ Private Subnets → Route to **NAT Gateway**

---

### **2️⃣ Internet Gateway (IGW)**
- Create IGW
- Attach it to your VPC

---

### **3️⃣ NAT Gateway**
- Create in Public Subnet A
- Allocate Elastic IP
- Add route in Private Route Table:
```
0.0.0.0/0 → NAT Gateway
```

---

### **4️⃣ Route Tables**

#### Public Route Table
```
0.0.0.0/0 → Internet Gateway
```

#### Private Route Table
```
0.0.0.0/0 → NAT Gateway
```

---

### **5️⃣ Create Application Load Balancer**
- Type: Application Load Balancer
- Scheme: Internet-facing
- Subnets: Public Subnet A & B

**ALB Security Group**:
```
Allow HTTP (80) from 0.0.0.0/0
```

---

### **6️⃣ Create Target Group**
- Type: Instance
- Port: 80
- Health Check Path: `/`

---

### **7️⃣ Create Launch Template**
Name: `App-LT`

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

## 🔍 Testing Checklist

### ✔ ALB DNS Test
Open:
```
http://your-alb-dns.amazonaws.com
```
You should see hostname responses switching between servers.

### ✔ Auto-Healing Test
1. Terminate an ASG EC2 instance
2. ASG launches a new one automatically
3. Target Group turns **healthy** again

### ✔ Multi-AZ High Availability Test
Confirm:
- EC2 instance in Private Subnet A
- EC2 instance in Private Subnet B

---

## 🧠 Key Learnings
- Difference between IGW & NAT Gateway
- Designing multi-AZ architectures
- How ALB + ASG provide high availability
- Using Launch Templates to automate EC2 builds
- Understanding health checks & auto-healing
- Proper use of private/public route tables
- Why EC2 in private subnets require NAT

---

## 📸 Screenshots / Evidence
(Add your screenshots below)

---

## ✅ Project Completed
You have successfully built a **production-style**, **scalable**, **fault-tolerant** web architecture on AWS.

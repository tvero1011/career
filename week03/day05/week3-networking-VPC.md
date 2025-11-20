# AWS Week 3 Day 5 — VPC Networking Lab  
Public Subnet + Private Subnet + NAT Gateway + Bastion Host

## 🔥 Goal
Build a secure 2-tier AWS network from scratch using:
- A public subnet with a bastion host (SSH entry point)
- A private subnet with an internal-only EC2 instance
- A NAT Gateway allowing private EC2 access to the internet
- Routing tables and security groups configured properly

ASCII Architecture Diagram

                        ┌──────────────────────────────────────────────┐
                        │                AWS VPC (10.0.0.0/16)         │
                        │                 Name: week3-vpc              │
                        └──────────────────────────────────────────────┘
                                         │
 ┌──────────────────────────────────────────────────────────────────────────────────┐
 │                              Internet Gateway (IGW)                               │
 │                               Attached to VPC                                      │
 └──────────────────────────────────────────────────────────────────────────────────┘
                                         │
                                         │ 0.0.0.0/0
                                         ▼

        ┌────────────────────────────────────────────────────────────────────────┐
        │                        Public Subnet (10.0.1.0/24)                     │
        │                         Name: week3-public-subnet                      │
        │                         Auto-assign public IP: YES                     │
        └────────────────────────────────────────────────────────────────────────┘

                        ┌───────────────────────────────────────┐
                        │       Bastion Host EC2                │
                        │       Name: week3-bastion             │
                        │       Public IP: YES                  │
                        │       SG: week3-public-sg             │
                        │       - SSH (22) My IP                │
                        └───────────────────────────────────────┘
                                         │
                                         │ SSH allowed
                                         ▼

        ┌────────────────────────────────────────────────────────────────────────┐
        │                 NAT Gateway (Elastic IP Attached)                      │
        │                 Lives in PUBLIC subnet                                 │
        │                 Allows PRIVATE instances to access internet            │
        └────────────────────────────────────────────────────────────────────────┘
                                         │
                                 0.0.0.0/0 via NAT
                                         │
                                         ▼

        ┌────────────────────────────────────────────────────────────────────────┐
        │                     Private Subnet (10.0.2.0/24)                       │
        │                      Name: week3-private-subnet                        │
        │                      Auto-assign public IP: NO                          │
        └────────────────────────────────────────────────────────────────────────┘
        
                        ┌───────────────────────────────────────┐
                        │       Private EC2 Instance            │
                        │       Name: week3-private-ec2         │
                        │       Public IP: NO                   │
                        │       SG: week3-private-sg            │
                        │       - SSH ONLY from bastion SG      │
                        └───────────────────────────────────────┘

                                         ▲
                                         │ Internal SSH only
                                         │
                        Bastion Host ────┘


────────────────────────────────────────────────────────────────────────────────────
                     ROUTE TABLE SUMMARY
────────────────────────────────────────────────────────────────────────────────────

Public Route Table:
- Subnet: week3-public-subnet
- Routes:
  - 10.0.0.0/16 → local
  - 0.0.0.0/0   → IGW

Private Route Table:
- Subnet: week3-private-subnet
- Routes:
  - 10.0.0.0/16 → local
  - 0.0.0.0/0   → NAT Gateway

────────────────────────────────────────────────────────────────────────────────────
                     SECURITY GROUP SUMMARY
────────────────────────────────────────────────────────────────────────────────────

week3-public-sg (for Bastion):
- Inbound:
  - SSH (22) — My IP
  - HTTP (80) — Anywhere
- Outbound: All allowed

week3-private-sg (for Private EC2):
- Inbound:
  - SSH (22) — Source: week3-public-sg
- Outbound:
  - All allowed (used for NAT internet)

────────────────────────────────────────────────────────────────────────────────────



## 🏗️ Architecture Overview
This lab creates the following architecture:

- **VPC:** 10.0.0.0/16  
- **Subnets:**
  - Public Subnet: 10.0.1.0/24  
  - Private Subnet: 10.0.2.0/24  
- **Internet Gateway:** Provides outbound access for public subnet  
- **NAT Gateway:** Allows private instance to reach internet  
- **Route Tables:**
  - Public RT → IGW  
  - Private RT → NAT Gateway  
- **Instances:**
  - `week3-bastion` (public EC2)
  - `week3-private-ec2` (private EC2)
- **Security Groups:**
  - `week3-public-sg`  
    - SSH (22) — My IP  
    - HTTP (80) — Anywhere  
  - `week3-private-sg`  
    - SSH (22) — Source: week3-public-sg 

## 🧪 Test Results
See test-results.md for complete outputs.

---

## 📡 Architecture Diagram
See `architecture-diagram.png`.

---

## 📘 What I Learned

### 🔹 VPC Basics  
How IP ranges and subnetting work in AWS.

### 🔹 Public vs Private Subnets  
- Public subnet → IGW route  
- Private subnet → no public access, uses NAT

### 🔹 NAT Gateway  
Allows private instances to access internet securely.

### 🔹 Bastion Host  
Used as a “jump server” to reach the private EC2.

### 🔹 Security  
- Restricting SSH only from My IP  
- Private EC2 only accessible through bastion SG

### 🔹 Troubleshooting Skills  
- Checking routes  
- Verifying SGs  
- Debugging NAT / IGW flow

---

## 🏁 Final Outcome
You now know how to build **real AWS production-style VPC architecture**, which is used in 90% of cloud engineering jobs.

This documentation is now part of your DevOps portfolio.     

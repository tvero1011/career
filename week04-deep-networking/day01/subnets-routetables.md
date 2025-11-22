📘 **Week 4 — Day 1

Subnets + Route Tables (VPC Deep Dive)**

✅ 1. Overview

Today you will configure a more advanced VPC layout.
You will create public and private subnets, associate route tables, and understand how traffic flows inside AWS networking.

This is foundational for the ALB + ASG integration coming later this week.

🏗️ 2. Architecture for Today

Your target layout:

VPC (10.0.0.0/16)
│
├── Public Subnet 1 (10.0.1.0/24)
├── Public Subnet 2 (10.0.2.0/24)
│     └── Uses Route Table → Internet Gateway
│
├── Private Subnet 1 (10.0.3.0/24)
└── Private Subnet 2 (10.0.4.0/24)
      └── Uses Route Table → NAT Gateway (Week 4 Day 2)


Today you build:

VPC

4 subnets

Route table for public subnets

Route table for private subnets

Attachments & associations

🧩 3. Actions Performed
3.1 Create VPC

Go to VPC Console

Create VPC

Name: week4-vpc

IPv4 CIDR: 10.0.0.0/16

Tenancy: Default

3.2 Create Subnets
Public Subnets
Name	AZ	CIDR
public-subnet-1	ap-southeast-1a	10.0.1.0/24
public-subnet-2	ap-southeast-1b	10.0.2.0/24
Private Subnets
Name	AZ	CIDR
private-subnet-1	ap-southeast-1a	10.0.3.0/24
private-subnet-2	ap-southeast-1b	10.0.4.0/24
3.3 Create Route Tables
🔵 Public Route Table

Name: public-rt

Associate to:

public-subnet-1

public-subnet-2

Add route:

0.0.0.0/0 → Internet Gateway (IGW attached later)

🟢 Private Route Table

Name: private-rt

Associate to:

private-subnet-1

private-subnet-2

No outbound route yet

NAT gateway will be added tomorrow (Week 4 Day 2)

3.4 Attach Internet Gateway

Create IGW: week4-igw

Attach to week4-vpc

Add route to public route table

Destination: 0.0.0.0/0
Target: Internet Gateway (week4-igw)

🧪 4. Verification Steps
✔️ Verify VPC & CIDR
VPC: 10.0.0.0/16

✔️ Verify Subnets

Public: 10.0.1.0/24, 10.0.2.0/24
Private: 10.0.3.0/24, 10.0.4.0/24

✔️ Public Subnets → IGW
✔️ Private Subnets → no outbound internet yet

Everything should match this:

Public RT → IGW
Private RT → (empty for now)

💾 5. Files Pushed to GitHub
📄 week4-day1-vpc-subnets.md

VPC creation steps

Subnet tables

Route table diagrams

IGW configuration

Traffic flow explanation

🖼️ vpc-subnet-architecture.png

Clean diagram of the layout

🎞️ subnet-routing.gif

GIF demonstrating subnet & route table setup

🧠 6. What You Learned Today

How to design proper VPC CIDR blocks

Differences between public vs private subnets

How route tables control traffic

How IGW enables internet access

Layout that prepares for NAT → ALB → ASG this week
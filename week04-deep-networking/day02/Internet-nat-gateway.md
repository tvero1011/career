# Week 4 — Day 2: Internet Gateway + NAT Gateway

## 1. Overview

Today’s lesson focused on understanding and configuring two key AWS networking components:
Internet Gateway (IGW) → Provides internet access for public subnets
NAT Gateway (NAT-GW) → Provides outbound internet access for private subnets
These are critical for designing a 2-tier or 3-tier architecture.

## 2. Key Concepts
### Internet Gateway (IGW)

A horizontally scaled, redundant AWS component.
Allows:
Public inbound traffic → EC2
Public outbound traffic ← EC2
Must be attached to a VPC.

Analogy
IGW is a door from your house to the outside world.
Without a door → no one can enter or leave.

### NAT Gateway

Used by private subnets.
Allows private instances to reach:
The internet (e.g., updates, API calls)
Does NOT allow inbound internet traffic.

Analogy
A NAT Gateway is like a one-way window:
Instances inside can look out (make requests)
But nothing outside can see or reach in.

## 3. Architecture



             Internet
                 │
               (IGW)
                 │
        ─────────┴──────────┐
       │                    │
 Public Subnet           Private Subnet
  EC2 (web)               EC2 (app/db)
      │                       │
   Internet                  NAT-GW

## 4. Steps I Completed Today

### 4.1 Attached an Internet Gateway
Created IGW: my-vpc-igw
Attached it to my VPC
(If not attached → no public access)

###4.2 Configured Public Subnet Route Table
Route Table: public-rt
Added route:
Destination	Target
0.0.0.0/0	Internet Gateway (igw-xxxxxx)
Associated public subnet(s):
public-subnet-1
public-subnet-2
Result → Public EC2 can receive public traffic.

### 4.3 Created a NAT Gateway
Steps:
Launched NAT Gateway in a public subnet
Assigned Elastic IP (EIP)
Named it: natgw-main

### 4.4 Configured Private Subnet Route Table
Route Table: private-rt
Added route:
Destination	Target
0.0.0.0/0	NAT Gateway (nat-xxxxxx)
Associated private subnets:
private-subnet-1
private-subnet-2
Result → Private EC2 can update software but stays hidden from the internet.

## 5. Security Group Logic

Public EC2 SG (web-sg)
Inbound:
80/443 → 0.0.0.0/0
22 → my IP

Outbound:
All → 0.0.0.0/0
Private EC2 SG (app/db-sg)

Inbound:
Only allow web-sg on port 3306 (MySQL) or application ports
No public inbound

Outbound:
Allow all (required for NAT)

## 6. Validation Steps

Test 1: Public instance
Should have internet → YES
ping google.com works

Test 2: Private instance
Direct internet access? → NO
(Correct behavior)

Outbound access via NAT? → YES
sudo yum update worked
curl http://aws.amazon.com worked

## 7. Common Issues & Fixes
Problem	Cause	Fix
No internet on public EC2	Wrong route table	Add IGW route
Private EC2 cannot update	NAT in wrong subnet	NAT must be in public subnet
NAT Gateway stuck in “Pending”	No Elastic IP assigned	Allocate EIP
Public subnet acts private	Missing IGW	Create & attach IGW

## 8. Summary

Today I successfully configured:

✔ Internet Gateway
✔ Route table for public subnets
✔ NAT Gateway
✔ Route table for private subnets
✔ Verified outbound/inbound behaviors

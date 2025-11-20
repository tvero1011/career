# Week 3 Day 2 — Security Groups (AWS Networking)

## Goal of the Day
Understand and configure AWS Security Groups, including:
- Inbound & outbound rules
- Allowing SSH correctly
- Allowing HTTP for web servers
- Using My IP vs Anywhere
- Security Group-to-Security Group communication
- Testing rules with EC2 instances

This is one of the most important networking fundamentals for DevOps engineers.

# PART 1 — Launch EC2 for Testing

### EC2 Settings:
Name: week3-sg-test
AMI: Amazon Linux 2
Instance Type: t2.micro
Key Pair: my-ec2-key
Security Group: week3-sg-main (created during launch)

After launch, copied the **Public IP** and SSH’d into it:
ssh -i my-ec2-key.pem ec2-user@<public-ip>

# PART 2 — Initial Security Group Configuration

Security Group created: **week3-sg-main**

### Inbound Rules:
| Type | Port | Source | Purpose |
|------|------|--------|---------|
| SSH  | 22   | My IP  | Secure remote login |
| HTTP | 80   | Anywhere (0.0.0.0/0) | Public web access |

### Outbound Rules:
- All traffic allowed (AWS default)

# TEST 1 — SSH Access

Before allowing SSH from My IP:
ssh -i key.pem ec2-user@<public-ip>

Expected: **SUCCESS**
Why?
Because SG rule allows SSH only from your home IP → secure.

# TEST 2 — HTTP Access (Web Traffic)

I installed Nginx just to test HTTP rule:
sudo amazon-linux-extras enable nginx1
sudo yum install nginx -y
sudo systemctl start nginx

Opened browser:
http://<public-ip>

Expected:  
Page loads because HTTP (80) from Anywhere is allowed.

# PART 3 — SG-to-SG Communication

Created a **second** EC2:
Name: week3-backend-ec2
Security Group: week3-sg-backend

Backend SG rules:
- Inbound:
  - SSH (22) from **week3-sg-main**
- Outbound:
  - All allowed

This means:
- Public EC2 → can SSH into backend EC2
- Internet → **cannot** SSH to backend EC2
- Backend is protected (private-style)

### Test SSH from EC2 → EC2
From the first instance:
ssh ec2-user@<backend-private-ip>

Expected:  
✔ SSH succeeds because SG rule allows SG-to-SG.

# Real-World SG Principles Learned

### Least privilege  
Never open unnecessary ports.

### My IP for SSH  
Most secure method for remote login.

### SG-to-SG is powerful  
Used in production for:
- web tier → app tier  
- app tier → database tier  

### Outbound is usually open  
Used by:
- package installs  
- OS updates  
- API calls  

### SGs are stateful  
If inbound is allowed, return traffic is automatically allowed.

# Key Concepts Mastered

### 1. **Inbound vs Outbound**
Inbound = who can access you  
Outbound = who you access

### 2. **CIDR blocks**
- 0.0.0.0/0 = public internet
- /32 = one IP (My IP)
- private CIDRs (10.x, 172.x, 192.168.x)

### 3. **SSH security**
- Never open SSH to the world
- Always restrict to your IP

### 4. **HTTP/HTTPS rules**
Web needs to be open
App/DB does NOT need to be open

### 5. **SG chaining**
Web SG → App SG → DB SG  
(Production model)


# Test Summary

| Test | Expected | Result |
|------|----------|--------|
| SSH into main EC2 | Allowed (My IP) | PASS |
| Nginx HTTP access | Allowed (0.0.0.0/0) | PASS |
| Backend SSH from laptop | Blocked | PASS |
| Backend SSH from main EC2 | Allowed (SG-to-SG) | PASS |

# Bonus — Commands Used

sudo yum update -y
sudo amazon-linux-extras enable nginx1
sudo yum install nginx -y
sudo systemctl start nginx

Check internal networking:
hostname -I
curl localhost


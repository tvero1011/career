# Week 3 Day 1 — EC2 Launch + SSH Connection

## Goal of the Day
Launch an EC2 instance and connect to it using SSH securely.
Understand:
- AMIs
- Instance types
- Key pairs
- Security groups
- Public vs private IP
- SSH best practices

# PART 1 — Launching the EC2 Instance
## EC2 Launch Configuration

**Name:**  
week3-ec2
**AMI (Linux Distribution):**  
- Amazon Linux 2 **or** Ubuntu 22.04  
(Used: Amazon Linux 2)
**Instance Type:**  
t2.micro (Free Tier)
**Key Pair:**  
week3-keypair.pem
Purpose: Allows SSH access using private key.

# Security Group Settings
Created SG:
week3-ec2-sg

Inbound Rules:
SSH — port 22 — Source: My IP

Why?  
✔ Best practice: Allow SSH only from your computer’s IP.

Outbound:  
All traffic: Allowed (default)

# Network Settings
VPC:  
week3-vpc

Subnet:  
week3-public-subnet

Auto-assign Public IP:  
ENABLED

Purpose: Instance must have a public IP to allow SSH from the internet.

# Launch
Clicked **Launch Instance** and successfully deployed EC2.

# PART 2 — SSH CONNECTION (TERMINAL)
### Commands:
chmod 400 week3-keypair.pem
ssh -i week3-keypair.pem ec2-user@PUBLIC_IP
sudo dnf update -y
sudo dnf install -y git nginx tree
sudo systemctl start nginx

### Give key correct permissions
chmod 400 week3-keypair.pem

### Connect to EC2  
For Amazon Linux:
ssh -i week3-keypair.pem ec2-user@<PUBLIC-IP>

For Ubuntu:
ssh -i week3-keypair.pem ubuntu@<PUBLIC-IP>

Replace `<PUBLIC-IP>` with the instance’s public IPv4 address.

# Verification Inside EC2

After SSH login ran:
hostname
uname -a
whoami

Outputs confirmed:
- Logged in as `ec2-user`
- Instance is Amazon Linux 2
- SSH working properly

# TROUBLESHOOTING NOTES

### SSH Timeout
- Security Group must allow port 22 from **your IP**
- Instance must be in **public subnet**
- Public IP must be **assigned**
- Route table must point to **Internet Gateway**

### Permission Denied (publickey)
- Wrong username (Ubuntu vs Amazon Linux)
- Key file not `chmod 400`

# Screenshots
<img width="641" height="424" alt="ssh-connection" src="https://github.com/user-attachments/assets/efebc2cb-1807-492e-887d-8a7eb6af24d6" />
<img width="736" height="278" alt="nginx-welcome" src="https://github.com/user-attachments/assets/060776fe-0172-4c28-9ea3-8dd60717bf9b" />
<img width="722" height="257" alt="ec2-launch" src="https://github.com/user-attachments/assets/167b10aa-33ce-4a6d-a139-2d976da3ed88" />
<img width="795" height="645" alt="ec2-details" src="https://github.com/user-attachments/assets/12dc32ea-1402-474d-ba2c-cbf3b803578b" />

# Final Outcome
By completing Day 1, I successfully:
- Launched my first EC2 instance inside a custom VPC  
- Configured a secure SSH connection  
- Verified network accessibility and Linux environment  

This sets the foundation for web server deployment, snapshots, and VPC networking in the next days.


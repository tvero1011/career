# Week 3 Day 5 — Test Results

## 1. SSH Tests
### Bastion → Private EC2
Command:
ssh -i my-key.pem ec2-user@10.0.2.10  
Result: SUCCESS

## 2. Private EC2 Internet Test
Command:
curl google.com  
Result: HTML response received → NAT gateway working

## 3. Nginx Test
Command:
sudo systemctl status nginx  
Result: active (running)

## 4. Security Group Test
- Private EC2 SSH reachable ONLY from bastion SG → PASS
- No public IP on private instance → PASS

## Summary
All networking components functioning as expected.

## commands-used.sh

# Connect to Bastion Host
ssh -i my-key.pem ec2-user@<public-bastion-ip>

# From Bastion → Private EC2
ssh -i my-key.pem ec2-user@<private-ec2-ip>

# Install Nginx on Private Instance
sudo yum install nginx -y
sudo systemctl start nginx

# Check routes (optional)
ip route

# Test internet connectivity
curl google.com
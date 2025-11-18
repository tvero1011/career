# Week 3 Day 1 — EC2 Launch + SSH

## 1. EC2 Launch
- AMI: Amazon Linux 2023
- Instance type: t2.micro
- Key pair: week3-keypair
- Security group: SSH port 22 from My IP

### Screenshots
<img width="722" height="257" alt="ec2-launch" src="https://github.com/user-attachments/assets/97d5a8f8-649a-47b8-9937-45cce74e60b8" />
<img width="795" height="645" alt="ec2-details" src="https://github.com/user-attachments/assets/3968cb31-b1bd-47a8-bcfc-c0f7c572b433" />


## 2. SSH Connection
### Commands:
chmod 400 week3-keypair.pem
ssh -i week3-keypair.pem ec2-user@PUBLIC_IP
sudo dnf update -y
sudo dnf install -y git nginx tree
sudo systemctl start nginx

#Edit Inbound Rules → Add rule
EC2 Instance - IAM admin-user

✔ Type: HTTP
✔ Port: 80
✔ Source: Anywhere 0.0.0.0/0


### Screenshots:
<img width="641" height="424" alt="ssh-connection" src="https://github.com/user-attachments/assets/6e64e673-4<img width="736" height="278" alt="nginx-welcome" src="https://github.com/user-attachments/assets/7d5f87d9-4f03-4930-85e7-00b72cc63e2c" />
b85-4cee-81b7-26df7056789a" />

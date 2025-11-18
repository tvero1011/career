# Week 3 Day 1 — EC2 Launch + SSH

## 1. EC2 Launch
- AMI: Amazon Linux 2023
- Instance type: t2.micro
- Key pair: week3-keypair
- Security group: SSH port 22 from My IP

### Screenshots
![EC2 Launch](images/week3/ec2-launch.png)
![EC2 Details](images/week3/ec2-details.png)

---

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
```markdown
![SSH Connection](images/week3/ssh-connection.png)
![NGINX Welcome](images/week3/nginx-welcome.png)
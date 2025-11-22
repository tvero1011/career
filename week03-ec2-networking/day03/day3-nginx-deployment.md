# Week 3 Day 3 — NGINX Deployment on EC2

## Goal of the Day
Deploy a public web server on EC2 using:
- Security groups
- Linux commands
- Nginx installation
- Custom HTML deployment
- Basic troubleshooting

This is important because **NGINX deployment is one of the most common DevOps tasks** and part of nearly every real cloud project.

# PART 1 — Launch EC2 Instance

## EC2 Settings:

Name: week3-nginx-server
AMI: Amazon Linux 2
Instance Type: t2.micro
Key Pair: my-ec2-key

Network Settings:
Allow SSH (22) from My IP
Allow HTTP (80) from Anywhere

After launch:
- copied the **Public IPv4 address**
- SSH’d into the instance
ssh -i my-ec2-key.pem ec2-user@<public-ip>

# PART 2 — Update Server

Before installing anything, updated packages:
sudo yum update -y

# PART 3 — Install Nginx

Checked if Amazon Linux 2 has nginx repo:
sudo amazon-linux-extras enable nginx1
sudo yum clean metadata
sudo yum install -y nginx

Started Nginx:
sudo systemctl start nginx
sudo systemctl enable nginx

Verified service:
systemctl status nginx

# TEST 1 — Check Web Server in Browser
Opened:
http://<public-ip>

Result:
Nginx default homepage displayed successfully.

# PART 4 — Deploy Custom HTML Page

Created custom page:
echo "<h1>Hello from Week 3 Day 3 — Nginx Server!</h1>"
| sudo tee /usr/share/nginx/html/index.html

Reloaded nginx:
sudo systemctl reload nginx

Tested again in browser:
http://<public-ip>
Now it shows the custom message.

# TEST 2 — Verify HTTP Security Group

Security group inbound rules:
- SSH (22) — My IP
- HTTP (80) — Anywhere
Outbound: ALL allowed
Both correct.

# Troubleshooting Notes

### If webpage doesn’t load:
- Check security group port 80
- 
- Check Nginx service status:
sudo systemctl status nginx

- Check firewall (Amazon Linux usually off)
- Ensure you are using public IP, not private IP

# What I Learned

### Nginx Basics  
- How to install and manage services  
- How to start, stop, reload services  

### Linux SysAdmin Skills  
- Editing files  
- Using `systemctl`  
- Modifying web directories  

### Networking Concepts  
- Firewalls/Security Groups  
- Public IPs  
- HTTP traffic flow  

### Deployment Workflow  
A real-world deploy process:
1. Launch server  
2. Configure packages  
3. Deploy application files  
4. Test  
5. Troubleshoot

## Screenshots
<img width="541" height="215" alt="welcome-nginx" src="https://github.com/user-attachments/assets/0dedaf8f-5ea5-41c1-9a51-e7ead9224d8c" />
<img width="353" height="146" alt="custom-page" src="https://github.com/user-attachments/assets/fe78f069-9258-477b-af02-d5573cc52aaa" />

# Bonus: Commands Used

sudo yum update -y
sudo amazon-linux-extras enable nginx1
sudo yum install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx
echo "<h1>Hello from Week 3 Day 3 — Nginx Server!</h1>" | sudo tee /usr/share/nginx/html/index.html
sudo systemctl reload nginx

   

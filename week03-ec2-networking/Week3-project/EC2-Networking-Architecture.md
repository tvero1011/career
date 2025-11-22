# Week 3 — Weekend Project: EC2 + Networking

# Project Goal
By the end of this weekend, you will have:
- A public EC2 web server running Nginx
- A custom AMI created from that EC2
- A snapshot of its root volume
- A backup EC2 launched from the AMI
- A simple 3-tier AWS architecture (Web → App → Storage)

This completes Week 3: EC2 + Networking Foundations.

# PART 1 — Public Web Server Setup
## Launch EC2 (Public Subnet)
Configuration:
AMI: Amazon Linux 2
Instance Type: t2.micro
VPC: your VPC
Subnet: Public subnet
Auto-assign Public IP: Enabled
Security Group:
SSH (22) — My IP
HTTP (80) — Anywhere
SSH into instance:
ssh -i my-key.pem ec2-user@<public-ip>

# PART 2 — Install and Configure Nginx
sudo yum update -y
sudo amazon-linux-extras install nginx1 -y
sudo systemctl start nginx
sudo systemctl enable nginx

Test in browser:
http://<public-ip>
You should see the Nginx welcome page.

# PART 3 — Create a Custom AMI

From AWS Console:
EC2 → Instances
Select your web server
Actions → Image → Create image
Name: week3-nginx-ami

Verify via CLI:
aws ec2 describe-images --owners self

# PART 4 — Create Snapshot of Root Volume

Get volume ID:
aws ec2 describe-volumes \
--filters Name=attachment.instance-id,Values=<instance-id>

Create snapshot:
aws ec2 create-snapshot \
  --volume-id <volume-id> \
  --description "Week 3 root volume snapshot"

List snapshots:
aws ec2 describe-snapshots --owner-ids self

# PART 5 — Launch New EC2 from AMI

EC2 → AMIs → select your AMI → Launch instance from AMI
Settings:
Name: week3-ami-test-server
Same SG (SSH + HTTP)
Same VPC / public subnet
After it boots:
Open:
http://<new-public-ip>

If Nginx appears without installing again, your AMI works.

# PART 6 — Private EC2 (App Tier)

Launch another EC2:
Subnet: Private subnet
Auto-assign public IP: Disabled
SG rule:
SSH allowed only from public EC2 SG
SSH into private instance via public EC2:
On Public EC2:
ssh ec2-user@<private-ip>

If successful → networking is working.

# PART 7 — S3 Bucket (Storage Tier)

Create bucket:
aws s3 mb s3://week3-tier-storage-<unique>

Upload test file:
echo "Hello Tier 3" > test.txt
aws s3 cp test.txt s3://week3-tier-storage-<unique>/

# PART 8 — Architecture Diagram (3-Tier)

Include this diagram in your repo:

                 +-----------------------------+
                 |          Internet           |
                 +--------------+--------------+
                                |
                                v
              +-------------------------------------+
              |    Public EC2 (Web Tier - Nginx)    |
              +---------------+----------------------+
                              |
                              v
              +-------------------------------------+
              |  Private EC2 (App Tier / Backend)    |
              +---------------+----------------------+
                              |
                              v
                 +------------------------------+
                 |       S3 Bucket (Data Tier) |
                 +------------------------------+


# PART 9 — Summary of Learnings
• Launched and configured a public EC2 web server
• Installed Nginx and tested HTTP connectivity
• Created a custom AMI from your EC2 instance
• Created a snapshot of the EBS root volume
• Launched a new EC2 from your AMI (proof of success)
• Built a private EC2 and tested network reachability
• Created S3 bucket for storage layer
• Designed a simple 3-tier architecture
• Completed Week 3 networking foundations

# Week 3 Day 4 — AMIs & Snapshots

## Goal of the Day
Learn how to:
- Create a custom AMI from an EC2 server
- Launch new instances from that AMI
- Understand how snapshots store EBS data
- Restore system states using AMIs/snapshots
- Build your first “golden image”

# PART 1 — Preparing Your EC2 Instance

I used an existing EC2 instance and installed a simple web server:
sudo yum install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx

Then I customized `index.html`:
sudo bash -c 'echo "<h1>Hello from my custom AMI!</h1>" > /usr/share/nginx/html/index.html'

I verified:
- Nginx works  
- Custom web page appears on public IP  

**This becomes the base for my AMI.**

# PART 2 — Create the AMI

AWS Console → EC2 → Instances → Select the instance → *Actions* → Image → “Create image”.

**Settings:**
- AMI Name: `nginx-custom-v1`
- Description: “EC2 with nginx preinstalled + custom homepage”
- No reboot: *unchecked* (default, safer)

**Result:**
AMI created successfully and appears under:
**EC2 → AMIs → Owned by me**

# PART 3 — Snapshot Verification

When I created the AMI, AWS automatically created:
- Root volume snapshot  
- Any additional volume snapshots
-  <img width="720" height="234" alt="ami-instance" src="https://github.com/user-attachments/assets/6c701d6e-e612-4d45-9de5-9fbc1495f390" />


# PART 4 — Launching an Instance From AMI (Cloning)

To test the image, I launched a new instance:
Steps:
1. EC2 → AMIs → Select `nginx-custom-v1`
2. Click **Launch instance from AMI**
3. Settings:
   - Name: Web-Server-From-AMI
   - InstanceType: t2.micro
   - Key Pair: my-ec2-key
   - Security Group:
     - Selected existing SG with port 80 open
4. Launch instance

#  PART 5 — Test the New Instance

Once the instance was running:
1. Copied its **Public IP**
2. Opened browser:
http://<public-ip>

**If the AMI works, you see your custom Nginx homepage immediately.**  
No installation required — everything is preconfigured.
I also SSH'd into the instance:
ssh -i my-key.pem ec2-user@<public-ip>

Then checked that nginx was already installed:
systemctl status nginx

✔ It was already active — means AMI worked.

# PART 6 — Snapshot Restore (Optional Exercise)

I also tested restoring snapshot:

1. EC2 → Snapshots → Select snapshot  
2. Actions → “Create volume”  
3. Attached volume to EC2  
4. Mounted the volume and verified files
This proves snapshots contain full disk state.

# What I Learned

### 1. AMIs Are Complete System Images
Contain:
- OS
- Packages
- Configurations
- App files
- Boot config

Used to clone servers instantly.

### 2. Snapshots Store the Disk State
AMIs depend on snapshots.
Snapshots = backups of EBS volumes.

### 3. Golden AMIs
DevOps teams build AMIs for:
- Application servers
- Security baseline
- Hardened OS builds
- Preconfigured Docker hosts
- CI/CD auto-scaling templates

### 4. AMIs save huge deployment time
Using AMI:
- New server ready in 10–20 seconds
- No manual installs
- No config drift

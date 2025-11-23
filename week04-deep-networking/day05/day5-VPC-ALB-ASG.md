## Integrating VPC + ALB + ASG (Full Architecture Assembly)

### Objective
Today you will combine all components you built earlier this week:
- VPC with public + private subnets  
- Internet Gateway + NAT Gateway  
- Application Load Balancer (ALB)  
- Auto Scaling Group (ASG)  
- Proper security groups  
- A working web app behind ALB  

This creates a **production-style scalable architecture.**

# 1. Final Architecture Flow

Users → ALB (public subnets) → Target Group → ASG → EC2 (private subnets)
Private subnets → NAT Gateway → Internet (for updates)

# 2. Review of Required Components

### ✔ Public Subnets
- Route: `0.0.0.0/0` via **Internet Gateway**

### ✔ Private Subnets
- Route: `0.0.0.0/0` via **NAT Gateway**

### ✔ Security Groups
- **ALB SG** → Allow HTTP (80) from anywhere  
- **EC2/ASG SG** → Allow HTTP **from ALB SG only**  

**Never allow 0.0.0.0/0 on private EC2 instances.**

# 3. Integration Steps (What I Completed)

### 🔹 Step 1 — Verified VPC structure
- [ ] VPC CIDR:  
- [ ] 2 Public Subnets IDs:  
- [ ] 2 Private Subnets IDs:  
- [ ] Route Tables configured correctly  

### 🔹 Step 2 — Verified NAT + IGW
- [ ] Internet Gateway attached  
- [ ] NAT Gateway active  
- [ ] Private subnets route → NAT  

### 🔹 Step 3 — Target Group
- [ ] Type: Instance  
- [ ] Port: 80  
- [ ] Health checks: `/`  

### 🔹 Step 4 — ALB Setup
- [ ] Internet-facing  
- [ ] Subnets: public only  
- [ ] SG: allow 80 from anywhere  
- [ ] Listener: HTTP 80 → Target Group  

### 🔹 Step 5 — Auto Scaling Group
- [ ] Launch Template used (with Nginx user-data)  
- [ ] Subnets: private only  
- [ ] Attach Target Group  
- [ ] Min/Desired/Max set  

### 🔹 Step 6 — Validation
- [ ] ALB DNS tested  
- [ ] Refresh → different EC2 hostnames  
- [ ] Target group shows **healthy** instances  

# 4. Verification Screenshots

- [ ] VPC dashboard  
- [ ] Subnet list  
- [ ] Route tables (public + private)  
- [ ] NAT Gateway  
- [ ] ALB configuration  
- [ ] ALB listener rules  
- [ ] Target group health check screen  
- [ ] Auto Scaling Group dashboard  
- [ ] EC2 instances in private subnets  

# 6. Summary

Today I successfully integrated:
- VPC networking  
- ALB load balancing  
- Auto Scaling  
- NAT for private EC2 outbound traffic  

This completes the **foundation of modern AWS production architecture**.

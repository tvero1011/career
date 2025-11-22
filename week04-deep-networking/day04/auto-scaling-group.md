## Auto Scaling Group (ASG) — Setup & Documentation

### 🎯 Objective
Today’s goal is to configure an **Auto Scaling Group (ASG)** using:
- A Launch Template  
- Private subnets  
- A Target Group  
- Scaling behavior based on demand  

This makes your architecture **fault-tolerant and scalable**, just like real production systems.

---

# 1. What Auto Scaling Group Does
- Ensures your application always has healthy EC2 instances  
- Automatically replaces failed instances  
- Scales up during high traffic  
- Scales down to reduce cost  

---

# 2. Requirements Before Starting
You should already have:
- ✔ Launch Template (with Nginx + user-data)  
- ✔ VPC with 2 private subnets  
- ✔ Target Group (Week 4 Day 3)  
- ✔ NAT Gateway (private subnet internet access)  

---

# 3. ASG Configuration Steps (What I Completed)

### 🔹 Step 1 — Create Auto Scaling Group
- [ ] Chose **Launch Template**  
- [ ] Selected **private subnets only**  
- [ ] Attached Target Group  
- [ ] Enabled **ELB health checks**  

### 🔹 Step 2 — Configure Desired Capacity
- [ ] Minimum size: 2  
- [ ] Desired capacity: 2  
- [ ] Maximum size: 4  

### 🔹 Step 3 — Add Scaling Policies (Optional but recommended)
- [ ] Target tracking: CPU > 60% → scale out  
- [ ] CPU < 40% → scale in  
- [ ] Cooldown period: 120 seconds  

---

# 4. ASG Verification

### ✔ Check 1 — Instances launched  
- [ ] ASG created 2 instances  
- [ ] Instances are inside the **private subnets**  
- [ ] Security group allows HTTP from ALB SG only  

### ✔ Check 2 — Target Group Health  
- [ ] Both instances show **healthy**  
- [ ] Instances are registered automatically  

### ✔ Check 3 — Scaling Test (Optional)
Run on EC2:

yes > /dev/null &

css
Copy code

- [ ] CPU increases  
- [ ] ASG scales up  

Stop test:

killall yes

yaml
Copy code

- [ ] ASG scales down  

---

# 5. Screenshots to Include

Create folder:
week4/screenshots/

yaml
Copy code

Add screenshots of:

- [ ] Launch Template  
- [ ] ASG creation wizard  
- [ ] ASG dashboard  
- [ ] Scaling policies  
- [ ] EC2 instances list  
- [ ] Target group health checks  

---

# 6. Notes & Observations
_Write down what you learned, any errors, fixes, or insights._

-  
-  
-  

---

# 7. Summary

Today I configured:
- Launch Template  
- Auto Scaling Group in private subnets  
- Integration with ALB Target Group  
- Scaling behavior for load increases  

This completes the core of a **production-ready AWS scalable architecture** for Week 4.

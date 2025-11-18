# Week 3 — Day 2: Security Groups + Key Pair

## 1. What I Did Today
- Studied AWS Security Group fundamentals.
- Created two security groups: **web-sg** and **app-sg**.
- Configured inbound rules for HTTP, HTTPS, SSH, and port 3000.
- Learned SG-to-SG referencing (important for multi-tier architecture).
- Created a new key pair (`week3-app-keypair.pem`) for secure SSH access.
- Took screenshots and documented everything.

---

## 2. Security Groups Created

### 🔹 web-sg (Public Web Server)
**Inbound Rules:**
22 — SSH — My IP
80 — HTTP — 0.0.0.0/0
443 — HTTPS — 0.0.0.0/0

yaml
Copy code

---

### 🔹 app-sg (Backend App Group)
**Inbound Rules:**
3000 — TCP — Source: web-sg

yaml
Copy code

This means only EC2 instances inside **web-sg** can connect to the backend app on port 3000.

---

## 3. Screenshots

Upload your screenshots to:
week3/images/

yaml
Copy code

Then paste them below:

### web-sg inbound rules  
![web-sg](images/day2-web-sg.png)

### app-sg inbound rules  
![db-sg](images/day2-app-sg.png)

### app-sg rule showing "Source = web-sg"  
![sg-source](images/day2-sg-source.png)

### key pair created  
![keypair](images/day2-keypair.png)

*(GitHub automatically generates image links when you upload screenshots.)*

---

## 4. Key Pair Details
Key Pair Name: week3-app-keypair
Type: RSA
Format: .pem
Purpose: Used for SSH login to EC2 instances

yaml
Copy code

---

## 5. Notes & Learnings
- Security Groups are **stateful** — return traffic is automatically allowed.
- SGs cannot block traffic (no deny rules).
- Best practice: SSH (22) should always be locked to **My IP**, never 0.0.0.0/0.
- SG-to-SG referencing is how real AWS architectures securely connect layers.
- app-sg becomes more secure because it does *not* allow public access.

---

## 6. Summary (3–4 sentences)
Today I learned how AWS Security Groups work and how to configure them for real architectures. I created a public-facing security group for web traffic and a private application security group restricted to web-sg. I also generated a new SSH key pair for secure access. All configurations and screenshots were documented in GitHub.

---
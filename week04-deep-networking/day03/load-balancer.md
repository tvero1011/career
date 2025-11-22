Week 4 — Day 3: Application Load Balancer (ALB)

Career C — Deep Networking + Load Balancer + Auto Scaling

1. Overview

Today’s goal was to learn and configure an Application Load Balancer (ALB) in AWS.
This service distributes incoming traffic to multiple EC2 instances for high availability and fault tolerance.

2. Why ALB?

Balances load between multiple EC2 servers

Automatically checks instance health

Only sends traffic to healthy instances

Works at Layer 7 (HTTP/HTTPS), enabling routing by path & hostname

Essential for scalable web architectures

Analogy

Think of ALB as a receptionist at a building:

Visitors = user requests

Receptionist = ALB

Offices (rooms) = EC2 instances

If one office is closed (unhealthy), the receptionist sends visitors to an open office.

3. Architecture
User → ALB → Target Group → EC2 Instances (web servers)

4. Steps I Completed Today
4.1 Create a Target Group

Type: Instances

Protocol: HTTP

Port: 80

VPC: my main VPC

Health check: /

Healthy threshold: 2

Timeout: 5 seconds

Added instances:

webserver-1

webserver-2

4.2 Create an Application Load Balancer

Type: Internet-facing

Protocol: HTTP (80)

Chose 2 public subnets

Attached SG: alb-sg

inbound: HTTP 80 from 0.0.0.0/0

outbound: all

Listener

HTTP:80 → Forward to target group

4.3 Security Groups Used
ALB Security Group (alb-sg)

Inbound:

Port	Source	Purpose
80	0.0.0.0/0	Allow public HTTP

Outbound:

Port	Destination	Purpose
ALL	0.0.0.0/0	Allow traffic to instances
Web Server SG (web-sg)

Inbound:

Port	Source	Purpose
80	alb-sg	Accept only ALB traffic
22	My IP	SSH access

Why no inbound from public?
Because ALB is the only entry point.

5. Health Checks

Configured the target group health checks:

Path: /

Unhealthy threshold: 2

If an instance stops responding, ALB stops sending traffic to it.

Tested → Turned off nginx on instance1 → ALB routed only to instance2.

6. Testing

I tested using the ALB DNS:

http://my-load-balancer-123456.region.elb.amazonaws.com


Refreshing the page alternates responses between EC2 servers.

7. Common Errors I Encountered
Error	Cause	Fix
503: No healthy targets	EC2 not responding on port 80	Installed nginx & opened port 80
Timeout	Wrong SG rules	Allowed ALB → EC2
Health check failed	Wrong path	Changed to /
8. Commands Used

Check nginx:

sudo systemctl status nginx


Restart nginx:

sudo systemctl restart nginx


Check listening ports:

sudo netstat -tulpn | grep 80

9. Screenshots I Added

ALB dashboard

Target group health checks

Listener configuration

Security groups

Architecture diagram

10. Summary

Today I successfully built and documented an Application Load Balancer and connected it to multiple EC2 instances via a target group.
This is a key component before creating an Auto Scaling Group (ASG) tomorrow.
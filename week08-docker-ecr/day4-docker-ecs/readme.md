# Week 8 Day 4 – Docker to ECS Concept Mapping

## What I Learned
- Docker images must be stored in ECR for AWS
- ECS does not replace Docker, it runs Docker containers
- ECS Task Definition = instructions to run a container
- ECS Service handles scaling and availability

## AWS Exam Key Points
- ECS pulls images from ECR
- containerPort maps to ALB Target Group
- ALB Listener forwards traffic to ECS containers
- Security Group must allow inbound traffic

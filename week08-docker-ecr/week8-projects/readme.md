# Career C + AWS SAA
## Week 8 – Docker + ECR Weekend Project
### Exam-Ready Container Deployment

---

## Objective

This project demonstrates my ability to:

- Containerize an application using Docker
- Store container images securely in Amazon Elastic Container Registry (ECR)
- Understand how Amazon ECS pulls images from ECR
- Apply AWS Solutions Architect Associate (SAA) architecture concepts

This project is designed to be practical, production-relevant, and aligned with SAA exam scenarios.

---

## Architecture Overview

Local Development  
→ Docker Image  
→ Amazon ECR (Private Repository)  
→ Amazon ECS Task  
→ Application Container  

---

## Core Concepts (SAA Focus)

- Docker images are built using Dockerfiles
- Amazon ECR stores Docker images securely (private by default)
- ECS pulls images from ECR (ECS does not build images)
- `EXPOSE` defines the containerPort
- External traffic is routed via:
  - Local: `-p hostPort:containerPort`
  - AWS: ALB → Target Group → containerPort
- Security Groups control inbound traffic
- IAM roles control access to ECR

---

## Project Structure

week08-docker-ecr/
├── Dockerfile
├── app.py
├── requirements.txt
└── README.md

---

## Application Overview

- Python Flask application
- Stateless design (safe for horizontal scaling)
- Health endpoint for load balancer checks

### Endpoints

| Endpoint | Purpose |
|--------|--------|
| `/` | Application response |
| `/health` | Health check for ALB / ECS |

---

## Dockerfile Summary (Exam-Relevant)

FROM python:3.11-slim  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  
COPY app.py .  
EXPOSE 5000  
CMD ["python", "app.py"]

### Key Notes

- `EXPOSE 5000` documents the containerPort
- Application listens on `0.0.0.0` to receive external traffic
- No local state is stored in the container

---

## Local Build & Run

docker build -t career-c-app .  
docker run -p 5000:5000 career-c-app  

Access the application:

http://localhost:5000  

Health check:

http://localhost:5000/health  

---

## Amazon ECR Workflow

### Create Repository

aws ecr create-repository --repository-name career-c-app  

### Authenticate Docker

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com  

### Tag & Push Image

docker tag career-c-app:latest <ECR_URI>:latest  
docker push <ECR_URI>:latest  

---

## IAM Permissions (Critical for SAA)

Required permissions:

- ecr:GetAuthorizationToken
- ecr:BatchCheckLayerAvailability
- ecr:PutImage
- ecr:GetDownloadUrlForLayer

Exam Reminder:  
If ECS cannot pull the image, the issue is IAM permissions, not Docker.

---

## AWS Deployment Mapping

Docker → Package application  
ECR → Store container images  
ECS → Run containers  
ALB → Expose application publicly  
Security Groups → Control inbound traffic  
IAM Role → Allow ECS to pull image  

---

## SAA Exam Triggers to Remember

- ECS does not build container images
- ECS pulls images from ECR
- EXPOSE does not open ports publicly
- ALB forwards traffic to containerPort
- Security Groups control access
- IAM controls ECR permissions

---

## What This Project Demonstrates

- Real Docker containerization
- Secure image storage with Amazon ECR
- Exam-ready understanding of ECS container workflows
- Clear AWS architecture reasoning
- Interview-ready container deployment explanation



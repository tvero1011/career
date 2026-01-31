# Week 8 Day 3 – Container Networking + Ports (Docker + SAA)

## Key Concepts
- Containers have isolated network namespaces
- EXPOSE documents container port (internal)
- -p maps container port → host port (external access)
- ECS containerPort in Task Definition mirrors Docker EXPOSE
- ALB + Security Group maps host traffic → container port

## Hands-On
- docker run -d --name myapp -p 5000:5000 my-first-image
- docker ps / docker inspect myapp
- Accessed app via host port 5000

## AWS Exam Context
- ECS containers listen on containerPort
- ALB maps external port to containerPort
- Security Group must allow incoming traffic

# Week 8 Day 5 – Docker Compose + Multi-Container (Docker + SAA)

## Key Concepts
- Multi-container apps: web + database / cache
- Docker Compose defines services + shared network
- containerPort in ECS = Dockerfile EXPOSE
- ALB → containerPort, Security Group must allow traffic

## Hands-On Steps
1. Create docker-compose.yml for web + redis
2. Run: `docker-compose up -d`
3. Access web app: http://localhost:8080
4. Inspect network: `docker network ls` / `docker network inspect <network_name>`

## AWS Exam Context
- ECS Task can contain multiple containers
- Sidecar containers don’t need public ports
- Web container port → ALB target group → SG inbound

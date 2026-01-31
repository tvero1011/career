# Week 8 Day 2 – Dockerfiles 

## Key Concepts
- Dockerfile defines how a Docker image is built
- FROM specifies the base image
- RUN executes commands at build time
- CMD defines the default container startup command

## Hands-On
Built and ran a custom Docker image locally using Python.

## AWS Exam Context
Dockerfiles are used to build images that are stored in Amazon ECR and deployed using ECS, EKS, or Fargate.

## Commands Used
- docker build -t my-first-image .
- docker run my-first-image


# Week 7 — DevOps Foundations: CI/CD Fundamentals

## Overview

This week focuses on **CI/CD (Continuous Integration / Continuous Deployment)** and setting up a basic cloud development environment.  
**Goal:** Automate AWS tasks and demonstrate DevOps competency for hiring purposes.

---

## CI/CD — What It Is

- **Continuous Integration (CI):** Automatically tests and prepares code whenever changes are pushed to GitHub.
- **Continuous Deployment (CD):** Automatically deploys changes to servers or environments.

> CI/CD ensures code changes are **reliable, repeatable, and error-free**.

---

## Why CI/CD Matters

- Reduces manual work and human error  
- Ensures infrastructure changes are consistent  
- Connects Python/Boto3 automation with real deployment pipelines  

This project demonstrates practical DevOps skills suitable for hire in Dubai/Europe.

---

## CI/CD Concepts in This Project

- **Pipeline:** Series of automated steps  
- **Stages:** Build → Test → Deploy  
- **Jobs:** Individual tasks  
- **Triggers:** Push to GitHub triggers scripts  
- **Environment:** AWS EC2 (dev environment)

---

## Project Workflow Diagram

![CI/CD Flow](ci-cd-flow.png)

**Flow:**

Developer → GitHub Repository
→ GitHub Actions Pipeline
→ Run Python Automation Scripts
→ AWS Infrastructure

---

## Scripts & Automation

**scripts/setup_env.sh**
- Installs Git, Python3, and Boto3 on AWS EC2  
- Prepares the environment for automation

**scripts/aws_resource_checker.py**
- Checks AWS credentials and connectivity  
- Verifies Python/Boto3 installation

---

## How to Run

1. Launch a **free-tier AWS EC2 instance**  
2. Run `setup_env.sh` to prepare environment  
3. Execute `aws_resource_checker.py` to verify AWS connectivity  
4. Use GitHub Actions workflow (next week) to automate scripts  

---

## Skills Demonstrated

- CI/CD fundamentals  
- AWS EC2 provisioning  
- Python/Boto3 automation  
- GitHub version control  
- Portfolio-ready documentation for hiring

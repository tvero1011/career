#!/bin/bash
# ==============================
# Week 7 — DevOps Portfolio Setup
# setup_env.sh
# Prepares EC2 instance with Git, Python3, Pip, and Boto3
# ==============================

# Update package lists
echo "Updating packages..."
sudo yum update -y

# Install Git
echo "Installing Git..."
sudo yum install git -y

# Install Python3 and Pip
echo "Installing Python3 and Pip..."
sudo yum install python3 -y
sudo python3 -m ensurepip --upgrade

# Upgrade pip
echo "Upgrading pip..."
sudo python3 -m pip install --upgrade pip

# Install Boto3
echo "Installing Boto3..."
pip3 install boto3 --user

# Optional: Install AWS CLI (if not already installed)
echo "Installing AWS CLI v2..."
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
rm -rf awscliv2.zip aws

# Verify installations
echo "Verifying installations..."
git --version
python3 --version
pip3 --version
python3 -m pip show boto3
aws --version

echo "✅ EC2 environment setup complete!"

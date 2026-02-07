variable "aws_region" {
  description = "Region where resources will be deployed"
  type        = string
  default     = "ap-southeast-1"
}

variable "vpc_id" {
  description = "The VPC ID where the security group will be created"
  type        = string
}

variable "subnet_id" {
  description = "The Subnet ID where the EC2 will be launched"
  type        = string
}

variable "ami_id" {
  description = "The AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}
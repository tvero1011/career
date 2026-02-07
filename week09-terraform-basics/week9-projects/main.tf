provider "aws" {
  region = var.aws_region
}

module "web_sg" {
  source  = "./modules/security_group"
  vpc_id  = var.vpc_id        # Points to Root variable
  sg_name = "Web-Security-Group"
}

module "web_ec2" {
  source        = "./modules/ec2"
  ami_id        = var.ami_id        # Points to Root variable
  instance_type = var.instance_type # Points to Root variable
  subnet_id     = var.subnet_id     # Points to Root variable
  sg_id         = module.web_sg.sg_id
}
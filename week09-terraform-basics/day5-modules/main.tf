module "web_ec2" {
  source        = "./modules/ec2"
  ami_id        = "ami-xxxxxxxx"
  instance_type = "t3.micro"
  subnet_id     = "subnet-xxxx"
}

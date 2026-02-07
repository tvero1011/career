output "web_server_public_ip" {
  description = "The public IP of the web server"
  value       = module.web_ec2.instance_public_ip
}

output "web_server_sg_id" {
  description = "The ID of the security group created"
  value       = module.web_sg.sg_id
}
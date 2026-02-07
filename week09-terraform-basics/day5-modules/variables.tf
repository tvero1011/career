variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "enable_public_ip" {
  type    = bool
  default = true
}

variable "allowed_ports" {
  type    = list(number)
  default = [22, 80]
}

variable "vpc_id" {
  type = string
}

variable "allowed_ports" {
  type = list(number)
  default = [22, 80]
}

variable "sg_name" {
  type = string
}

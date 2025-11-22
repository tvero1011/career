# Notes — Week 3 Day 5 Networking Lab

- NAT Gateway only works in PUBLIC subnet.
- Private EC2 must have route 0.0.0.0/0 → NAT Gateway.
- Bastion must have inbound SSH from My IP only.
- Private EC2 must have inbound SSH from bastion security group.
- NAT Gateway requires an Elastic IP.
- Private instances NEVER get public IP.

Common mistakes:
- Forgot to associate private subnet with private route table.
- Misconfigured SGs prevent SSH.
- NAT in wrong subnet.
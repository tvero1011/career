#[ EC2 Instance (Running) ]

[ EBS Volume (Hard Drive) ] ———> [ Snapshot (Backup of Drive) ]
[ AMI (Bootable Template) ]
[ New EC2 Instance (Clone) ]

#Reﬂection:
"Today I learned that an AMI is just a snapshot with metadata. This allows for ‘Immutable
Infrastructure'—instead of patching old servers, we just bake a new AMI and replace them
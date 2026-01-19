# Week 6 — Day 5: Automation Report

## Overview
This report summarizes all automation scripts created this week:

### Day 1: VPC Creation
- Script: `day1_vpc_creation.py`
- Task: Create VPC, subnet, and tags
- Status: ✅ Tested in AWS console

### Day 2: Budget Automation
- Script: `day2_budget_automation.py`
- Task: Create monthly budget with alert
- Status: ✅ Verified in AWS Budgets console

### Day 3: EC2 Monitoring (CloudWatch)
- Script: `day3_ec2_monitoring.py`
- Task: List EC2 instances, create CPU alarms
- Status: ✅ Alarms appear in CloudWatch

### Day 4: EC2 Monitoring v2
- Script: `day4_ec2_monitoring_v2.py`
- Task: Enhanced alarms, added tags
- Status: ✅ Alarms verified, tags applied

### Day : EC2 Monitoring Metrics
- Script: `day5_ec2_metrics.py`
- Task: Fetch CloudWatch metrics for EC2 instances



## Lessons Learned
- Using **boto3 clients** to automate AWS services is powerful
- Catching **exceptions** prevents script failures
- **Tags and descriptive names** are important for maintainability
- **Combining scripts** will make the weekend project easier

## Next Step
- Weekend Project: **Automated EC2 Launcher Script**
- Combine VPC, Budget, EC2 monitoring scripts into one pipeline

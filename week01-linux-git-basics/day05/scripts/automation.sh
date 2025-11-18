#!/bin/bash

mkdir -p logs

mv *.log logs/ 2>/dev/null

echo "Automation run at: $(date)"  >> logs/run.log

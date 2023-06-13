#!/bin/bash

SESSION_LIMIT=50
SESSION_DELAY=0.5

current_sessions=$(aws devicefarm list-test-grid-sessions --project-arn arn:aws:devicefarm:us-west-2:482218046771:testgrid-project:0d0a9d1b-c4b0-4393-a4c1-e07e25686ceb --status ACTIVE --region us-west-2 --output json | jq '.testGridSessions | length')

while [ "$current_sessions" -ge "$SESSION_LIMIT" ]
do
    sleep $SESSION_DELAY
    current_sessions=$(aws devicefarm list-test-grid-sessions --project-arn arn:aws:devicefarm:us-west-2:482218046771:testgrid-project:0d0a9d1b-c4b0-4393-a4c1-e07e25686ceb --status ACTIVE --region us-west-2 --output json | jq '.testGridSessions | length')
done

for ((i=0; i<50; i++))
do
    # Execute a command
    echo "Current session count: $current_sessions"
    aws ecs run-task --cluster 'selenium-automation' --region 'us-west-2' --task-definition df-test:1 --overrides '{"containerOverrides": [{ "name": "script_exec","command": ["device_farm_test.py"]}]}' --network-configuration "awsvpcConfiguration={subnets=[subnet-0ff95d294ee1f78fb, subnet-0badb53dbf918db64],securityGroups=[sg-04d00d4998f010d0c],assignPublicIp=ENABLED}" --launch-type FARGATE
    sleep $SESSION_DELAY
done

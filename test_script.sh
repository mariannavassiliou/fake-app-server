#!/bin/bash

clear
docker build -t fake-server-app .
sleep 5
docker run -d -p 5001:5000 fake-server-app

OUTPUT=$(docker ps -q | grep "$name")
echo $OUTPUT
result=$( docker images -q fake-server-app )

if [[ -n "$result" ]]; then
  echo 'Container image successfully created'
  dockerId=$( docker ps -a -q  )
  cd tests/
  python3 -m pytest functional
  docker stop $dockerId
else
  echo 'Container image does not exist'
fi

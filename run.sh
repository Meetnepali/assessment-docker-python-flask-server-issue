#!/bin/bash
source install.sh
docker build -t flask-database-app .
docker-compose up
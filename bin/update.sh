#!/bin/sh

cd /home/rizkyalfikri/app/fastapi-docker-compose
echo "Updating services..."
git fetch origin 
git reset --hard origin/main

echo "Building new Docker containers..."
docker compose -f docker-compose.prod.yaml build

echo "Deploying updated services..."
docker compose -f docker-compose.prod.yaml up -d --no-deps --build

echo "Services updated."
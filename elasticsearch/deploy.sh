#!/bin/bash

echo "Stopping existing services..."
docker-compose down

echo "Pulling latest versions of images..."
docker-compose pull

echo "Building services..."
docker-compose build

echo "Starting services..."
docker-compose up -d

#!/bin/bash

echo "Stopping services..."
docker-compose down

echo "Removing unused Docker images..."
docker system prune -f

echo "Removing unused Docker volumes..."
docker volume prune -f

echo "Cleanup completed."

#!/bin/bash

# Increase vm.max_map_count for Elasticsearch
# The following command adjusts the kernel parameter `vm.max_map_count`
# to ensure that Elasticsearch can function properly. Elasticsearch
# requires a larger number of memory map areas to operate efficiently.
# By setting the value to 262144, we allow sufficient memory map areas
# for Elasticsearch to handle its indexing and search operations.
sudo sysctl vm.max_map_count=262144

echo "Stopping existing services..."
docker-compose down

echo "Pulling latest versions of images..."
docker-compose pull

echo "Building services..."
docker-compose build

echo "Starting services..."
docker-compose up -d

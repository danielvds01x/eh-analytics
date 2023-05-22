#!/bin/bash

# Get the clickhouse image
docker pull clickhouse/clickhouse-server:23.4.2.11-alpine

# Get the directory path of the script
script_dir=$(dirname "$(realpath "$0")")

# Set the desired subdirectory names for ClickHouse data and logs
data_dir="ch_data"
logs_dir="ch_logs"

# Create the directories for ClickHouse data and logs
mkdir -p "$script_dir/$data_dir"
mkdir -p "$script_dir/$logs_dir"

# Run the Docker container with volume mounts
docker run -d \
    --rm -e CLICKHOUSE_DB=testdb \
    -e CLICKHOUSE_USER=username \
    -e CLICKHOUSE_DEFAULT_ACCESS_MANAGEMENT=1 \
    -e CLICKHOUSE_PASSWORD=password \
    -p 8123:8123 \
    -v "$script_dir/$data_dir":/var/lib/clickhouse/ \
    -v "$script_dir/$logs_dir":/var/log/clickhouse-server/ \
    --name some-clickhouse-server --ulimit nofile=262144:262144 \
    clickhouse/clickhouse-server



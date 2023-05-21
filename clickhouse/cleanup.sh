#!/bin/sh

docker container stop some-clickhouse-server

docker container rm some-clickhouse-server

#!/bin/bash

# Get the parent directory
CURRENT_DIR=$(pwd)
PARENT_DIR=$(dirname "$CURRENT_DIR")

# The command to start the application
docker compose -f $PARENT_DIR/docker-compose.yml stop
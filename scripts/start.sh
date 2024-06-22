#!/bin/bash

# This script assumes the containers have already been created

# Get the parent directory
CURRENT_DIR=$(pwd)
PARENT_DIR=$(dirname "$CURRENT_DIR")

# The command to start the application
docker compose -f $PARENT_DIR/docker-compose.yml up -d

# Enter into the container
docker exec -it clientboards-be /bin/bash
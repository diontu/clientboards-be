#!/bin/bash

# Get the parent directory
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# The command to start the application
docker compose -f $PARENT_DIR/docker-compose.yml stop
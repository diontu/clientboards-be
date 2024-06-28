#!/bin/bash

# This script assumes the containers have already been created

# Get the parent directory
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

DOCKER_COMPOSE_COMMAND="docker compose -f $PARENT_DIR/docker-compose.yml up -d"
DOCKER_EXECUTE_COMMAND="docker exec -it clientboards-be-container /bin/bash"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Running on Linux"
    $($DOCKER_COMPOSE_COMMAND)
    $($DOCKER_EXECUTE_COMMAND)
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Running on macOS"
    $($DOCKER_COMPOSE_COMMAND)
    $($DOCKER_EXECUTE_COMMAND)
elif [[ "$OSTYPE" == "cygwin" ]]; then
    echo "Running on Cygwin (POSIX compatibility layer on Windows)"
    $($DOCKER_COMPOSE_COMMAND)
    $($DOCKER_EXECUTE_COMMAND)
elif [[ "$OSTYPE" == "msys" ]]; then
    echo "Running on MinGW (Minimalist GNU for Windows)"
    PREFIXED_WINDOWS_DOCKER_COMPOSE_COMMAND="winpty $DOCKER_COMPOSE_COMMAND"
    PREFIXED_WINDOWS_DOCKER_EXECUTE_COMMAND="winpty $DOCKER_EXECUTE_COMMAND"
    eval $PREFIXED_WINDOWS_DOCKER_COMPOSE_COMMAND
    eval $PREFIXED_WINDOWS_DOCKER_EXECUTE_COMMAND
elif [[ "$OSTYPE" == "win32" ]]; then
    echo "Running on Windows"
    PREFIXED_WINDOWS_DOCKER_COMPOSE_COMMAND="winpty $DOCKER_COMPOSE_COMMAND"
    PREFIXED_WINDOWS_DOCKER_EXECUTE_COMMAND="winpty $DOCKER_EXECUTE_COMMAND"
    eval $PREFIXED_WINDOWS_DOCKER_COMPOSE_COMMAND
    eval $PREFIXED_WINDOWS_DOCKER_EXECUTE_COMMAND
else
    echo "Unknown OS"
    # Default case
fi
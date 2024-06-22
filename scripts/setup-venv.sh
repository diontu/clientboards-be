#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

# Function to check if venv is installed
check_venv_installed() {
    python3 -m venv --help > /dev/null 2>&1
    return $?
}

# Function to check if the venv folder exists
check_venv_folder_exists() {
    if [ -d "$PARENT_DIR/.venv" ]; then
        return 0
    else
        return 1
    fi
}

# Function to install venv if it is not installed
install_venv() {
    echo "venv is not installed or .venv folder does not exist. Creating virtual environment..."
    python3 -m venv "$PARENT_DIR/.venv"
    if [ -d "$PARENT_DIR/.venv" ]; then
        echo "Virtual environment successfully created in '$PARENT_DIR/.venv'."

        # Set execute permissions for the activate script
        chmod +x "$PARENT_DIR/.venv/bin/activate"
    else
        echo "Failed to create virtual environment. Please check your setup and try again."
        exit 1
    fi
}

# Main script
if check_venv_installed && check_venv_folder_exists; then
    echo "venv is already installed and .venv folder exists."
else
    install_venv
fi
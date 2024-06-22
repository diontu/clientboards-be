#!/bin/bash

# Install cURL
apt-get -y update; apt-get -y install curl


# Install venv
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
${SCRIPT_DIR}/setup-venv.sh

# activate venv
source ${PARENT_DIR}/.venv/bin/activate

# Install dependencies
pip3 install --upgrade pip; pip3 install -r requirements.txt

# Run the application
python3 manage.py runserver 0.0.0.0:8000
#!/bin/bash

# Install cURL
apt-get -y update; apt-get -y install curl; apt-get install -y bash
apt-get -y install sqlite3

# Install venv
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
${SCRIPT_DIR}/setup-venv.sh

# Install dependencies
pip3 install --upgrade pip; pip3 install -r requirements.txt

# Activate venv
source ${PARENT_DIR}/.venv/bin/activate

# Install dependencies
pip3 install --upgrade pip; pip3 install -r requirements.txt

# Setup custom commands
cp ${PARENT_DIR}/scripts/dev/custom-commands.sh /root/.bashrc
source /root/.bashrc

# Migrate the database
python3 manage.py makemigrations; python3 manage.py migrate

# Run the celery worker before starting the application and
celery -A clientboards worker -l info --logfile=./.logs/celery.log & 

# Run the application
python3 manage.py runserver 0.0.0.0:8000
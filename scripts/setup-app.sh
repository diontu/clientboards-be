#!/bin/bash

# Install cURL
apt-get -y update; apt-get -y install curl

# Install dependencies
pip3 install -r requirements.txt

# Run the application
python3 manage.py runserver 0.0.0.0:8000
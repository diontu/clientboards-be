#!/bin/bash

echo "Custom commands have loaded successfully!"

# Add your custom commands here
pm() {
    python3 manage.py "$@"
}
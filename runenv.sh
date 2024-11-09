#!/bin/bash

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source venv/bin/activate
echo "Virtual environment activated."

# Install the requirements
pip install -r requirements.txt
echo "Requirements installed."

# Your command to run the local environment
echo "Starting the local environment..."

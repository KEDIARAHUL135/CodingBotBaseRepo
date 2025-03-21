#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check for Python installation
if ! command -v python &> /dev/null
then
    echo "python could not be found. Please install Python 3 and try again."
    exit 1
fi

# Create a virtual environment in the 'venv' directory
echo "Creating virtual environment..."
python -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
# shellcheck disable=SC1091
source venv/bin/activate

# Upgrade pip in the virtual environment
echo "Upgrading pip..."
pip install --upgrade pip

# Install Poetry within the virtual environment
echo "Installing Poetry..."
pip install poetry

# Run Poetry install to resolve and install dependencies
echo "Installing project dependencies with Poetry..."
poetry install

echo "Environment setup complete."
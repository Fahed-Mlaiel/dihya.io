#!/bin/bash

# Exit on any error
set -e

# Check if the script is run with root or sudo privileges which is not recommended for security reasons
if [ "$(id -u)" == "0" ]; then
   echo "This script should not be run as root or with sudo privileges. Exiting."
   exit 1
fi

# Function to generate backend module
generate_backend_module() {
    echo "Generating backend module..."
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py collectstatic --noinput
    deactivate
    cd ..
}

# Function to generate frontend module
generate_frontend_module() {
    echo "Generating frontend module..."
    cd frontend
    npm install
    npm run build
    cd ..
}

# Function to generate plugins
generate_plugins() {
    echo "Generating plugins..."
    # Assuming plugins are Node.js modules
    cd plugins
    npm install
    npm run build
    cd ..
}

# Function to generate documentation
generate_docs() {
    echo "Generating documentation..."
    cd docs
    # Assuming documentation is built with a tool like Sphinx or MkDocs
    mkdocs build
    cd ..
}

# Function to setup internationalization (i18n)
setup_i18n() {
    echo "Setting up internationalization..."
    # Assuming i18n setup involves some scripts or commands
    cd i18n
    # Custom i18n setup commands here
    cd ..
}

# Main execution flow
echo "Starting the seed process..."

generate_backend_module
generate_frontend_module
generate_plugins
generate_docs
setup_i18n

echo "Seed process completed successfully."
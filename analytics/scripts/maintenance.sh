#!/bin/bash

# Exit on any error
set -e

# Configuration variables
FRONTEND_DIR="frontend"
BACKEND_DIR="backend"
DOCS_DIR="docs"
I18N_DIR="i18n"
PLUGINS_DIR="plugins"

# Function to check if a directory exists
check_dir() {
  if [ ! -d "$1" ]; then
    echo "Directory $1 does not exist. Creating..."
    mkdir -p "$1"
  fi
}

# Function to build the frontend
build_frontend() {
  echo "Building frontend..."
  cd "$FRONTEND_DIR"
  npm install
  npm run build
  cd -
}

# Function to build the backend
build_backend() {
  echo "Building backend..."
  cd "$BACKEND_DIR"
  npm install
  npm run build
  cd -
}

# Function to generate documentation
generate_docs() {
  echo "Generating documentation..."
  cd "$DOCS_DIR"
  # Assuming a tool like JSDoc or Sphinx is used for documentation
  make html
  cd -
}

# Function to update internationalization files
update_i18n() {
  echo "Updating internationalization files..."
  cd "$I18N_DIR"
  # Assuming a tool like i18next is used for i18n
  npm run update
  cd -
}

# Function to build plugins
build_plugins() {
  echo "Building plugins..."
  cd "$PLUGINS_DIR"
  npm install
  npm run build
  cd -
}

# Main execution flow
echo "Starting maintenance script..."

# Check directories
check_dir "$FRONTEND_DIR"
check_dir "$BACKEND_DIR"
check_dir "$DOCS_DIR"
check_dir "$I18N_DIR"
check_dir "$PLUGINS_DIR"

# Build and maintain modules
build_frontend
build_backend
generate_docs
update_i18n
build_plugins

echo "Maintenance script completed successfully."
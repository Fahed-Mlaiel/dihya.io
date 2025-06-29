#!/bin/bash

# backup.sh
# Script for backing up analytics modules including backend, frontend, plugins, docs, and i18n files.

# Exit on any error
set -e

# Configuration
BACKUP_DIR="/path/to/backup/directory"
ANALYTICS_DIR="/path/to/analytics/modules"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_NAME="analytics_backup_$TIMESTAMP.tar.gz"

# Functions
function backup_module() {
    local module_path=$1
    local module_name=$(basename "$module_path")

    echo "Backing up $module_name..."
    tar -czf "$BACKUP_DIR/$module_name"_"$TIMESTAMP.tar.gz" -C "$module_path" .
}

# Ensure the backup directory exists
mkdir -p "$BACKUP_DIR"

# Start backup process
echo "Starting backup of analytics modules..."

# Backend
backup_module "$ANALYTICS_DIR/backend"

# Frontend
backup_module "$ANALYTICS_DIR/frontend"

# Plugins
backup_module "$ANALYTICS_DIR/plugins"

# Documentation
backup_module "$ANALYTICS_DIR/docs"

# Internationalization (i18n)
backup_module "$ANALYTICS_DIR/i18n"

# Final message
echo "Backup completed successfully. Files are stored in $BACKUP_DIR"

# End of script
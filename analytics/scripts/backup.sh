#!/bin/bash

# backup.sh
# Script to backup application modules: backend, frontend, plugins, docs, i18n.

# Exit on any error
set -e

# Configuration
BACKUP_DIR="/path/to/backup/directory"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_NAME="app_backup_$TIMESTAMP"
LOG_FILE="$BACKUP_DIR/backup_$TIMESTAMP.log"

# Function to backup a directory
backup_module() {
    local module_path=$1
    local module_name=$2

    echo "Backing up $module_name"
    tar -czf "$BACKUP_DIR/$BACKUP_NAME/$module_name.tar.gz" -C "$module_path" .
}

# Create backup directory with timestamp
mkdir -p "$BACKUP_DIR/$BACKUP_NAME"

# Redirect all output to log file
exec &> "$LOG_FILE"

# Backup Backend
backup_module "/path/to/backend" "backend"

# Backup Frontend
backup_module "/path/to/frontend" "frontend"

# Backup Plugins
backup_module "/path/to/plugins" "plugins"

# Backup Docs
backup_module "/path/to/docs" "docs"

# Backup i18n
backup_module "/path/to/i18n" "i18n"

# All done
echo "Backup completed successfully."

# End of script
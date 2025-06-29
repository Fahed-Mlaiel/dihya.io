#!/bin/bash

# Ce script est destiné à restaurer les modules analytics d'une application.
# Il inclut le backend, le frontend, les plugins, la documentation et les fichiers de localisation (i18n).

# Configuration
BACKUP_DIR="/path/to/backup"
LOG_DIR="/path/to/logs"
RESTORE_DIR="/path/to/restore"
TIMESTAMP=$(date +%Y%m%d%H%M%S)
LOG_FILE="${LOG_DIR}/restore_${TIMESTAMP}.log"

# Fonctions
log() {
    echo "$(date +%Y-%m-%d\ %H:%M:%S) - $1" | tee -a "${LOG_FILE}"
}

check_dir() {
    if [ ! -d "$1" ]; then
        log "Le répertoire $1 n'existe pas. Création en cours..."
        mkdir -p "$1"
    fi
}

restore_files() {
    local source=$1
    local destination=$2
    log "Restauration des fichiers de ${source} vers ${destination}..."
    rsync -av --delete "${source}/" "${destination}/" >> "${LOG_FILE}" 2>&1
}

# Vérification des répertoires
check_dir "${BACKUP_DIR}"
check_dir "${LOG_DIR}"
check_dir "${RESTORE_DIR}"

# Restauration des modules
log "Début de la restauration des modules analytics."

# Restauration du backend
restore_files "${BACKUP_DIR}/backend" "${RESTORE_DIR}/backend"

# Restauration du frontend
restore_files "${BACKUP_DIR}/frontend" "${RESTORE_DIR}/frontend"

# Restauration des plugins
restore_files "${BACKUP_DIR}/plugins" "${RESTORE_DIR}/plugins"

# Restauration de la documentation
restore_files "${BACKUP_DIR}/docs" "${RESTORE_DIR}/docs"

# Restauration des fichiers i18n
restore_files "${BACKUP_DIR}/i18n" "${RESTORE_DIR}/i18n"

log "Restauration terminée avec succès."

# Nettoyage des anciens fichiers de log
find "${LOG_DIR}" -name 'restore_*.log' -mtime +30 -exec rm {} \;

exit 0
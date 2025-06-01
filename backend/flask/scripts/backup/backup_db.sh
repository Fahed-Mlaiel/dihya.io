#!/bin/bash
# Dihya – Script de sauvegarde base de données (production-ready, sécurisé, RGPD)
# Usage: bash backup_db.sh
# Sauvegarde la base de données principale dans le dossier backups/ avec timestamp
# Chiffre la sauvegarde si GPG est disponible
set -euo pipefail
BACKUP_DIR="$(dirname "$0")/../../backups"
DB_NAME="dihya_db"
DATE=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_FILE="$BACKUP_DIR/db_backup_$DATE.sql"
mkdir -p "$BACKUP_DIR"
pg_dump "$DB_NAME" > "$BACKUP_FILE"
echo "Sauvegarde SQL créée: $BACKUP_FILE"
if command -v gpg >/dev/null; then
  gpg --symmetric --cipher-algo AES256 "$BACKUP_FILE"
  echo "Sauvegarde chiffrée: $BACKUP_FILE.gpg"
fi

#!/bin/bash
# Dihya – Script de restauration base de données (production-ready, sécurisé, RGPD)
# Usage: bash restore_db.sh --file backup.sql[.gpg]
set -euo pipefail
BACKUP_FILE=""
while [[ $# -gt 0 ]]; do
  case $1 in
    --file)
      BACKUP_FILE="$2"
      shift 2
      ;;
    *)
      echo "Usage: $0 --file backup.sql[.gpg]"; exit 1;;
  esac
done
if [[ -z "$BACKUP_FILE" ]]; then
  echo "Fichier de sauvegarde non spécifié."; exit 1
fi
if [[ "$BACKUP_FILE" == *.gpg ]]; then
  gpg --decrypt "$BACKUP_FILE" | psql dihya_db
else
  psql dihya_db < "$BACKUP_FILE"
fi
echo "Restauration terminée."

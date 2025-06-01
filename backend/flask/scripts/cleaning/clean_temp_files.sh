#!/bin/bash
# Dihya – Script de nettoyage des fichiers temporaires et logs (sécurité, RGPD)
# Usage: bash clean_temp_files.sh
set -euo pipefail
CLEAN_DIRS=("/tmp/dihya" "$(dirname "$0")/../../app/tmp" "$(dirname "$0")/../../logs")
for DIR in "${CLEAN_DIRS[@]}"; do
  if [[ -d "$DIR" ]]; then
    find "$DIR" -type f -name '*.tmp' -delete
    find "$DIR" -type f -name '*.log' -mtime +30 -delete
    echo "Nettoyé: $DIR"
  fi
done

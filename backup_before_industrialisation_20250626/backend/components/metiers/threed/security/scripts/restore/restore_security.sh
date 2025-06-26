#!/bin/bash
# restore_security.sh – Restauration avancée des données de sécurité
# Usage : bash restore_security.sh /chemin/vers/backup.tar.gz

set -e
BACKUP_FILE=${1}
if [ ! -f "$BACKUP_FILE" ]; then
  echo "[ERREUR] Fichier de backup introuvable : $BACKUP_FILE" >&2
  exit 1
fi
tar xzf "$BACKUP_FILE" -C /
echo "[OK] Restauration sécurité terminée."

#!/bin/bash
# backup_security.sh – Sauvegarde avancée des données sensibles (clé en main)
# Usage : bash backup_security.sh /chemin/vers/dossier_cible

set -e
BACKUP_DIR=${1:-/backup/security}
DATE=$(date +%Y-%m-%d_%H-%M-%S)
DEST="$BACKUP_DIR/security_backup_$DATE.tar.gz"

mkdir -p "$BACKUP_DIR"
tar czf "$DEST" /workspaces/dihya.io/backend/components/metiers/juridique/security/
echo "[OK] Sauvegarde sécurité créée : $DEST"

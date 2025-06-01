#!/bin/bash
# Dihya – Script RGPD: purge des données utilisateur (droit à l'oubli)
# Usage: bash purge_user_data.sh --user-id <id>
set -euo pipefail
USER_ID=""
while [[ $# -gt 0 ]]; do
  case $1 in
    --user-id)
      USER_ID="$2"
      shift 2
      ;;
    *)
      echo "Usage: $0 --user-id <id>"; exit 1;;
  esac
done
if [[ -z "$USER_ID" ]]; then
  echo "ID utilisateur requis."; exit 1
fi
# Exemple: suppression dans la base (adapter selon ORM)
psql dihya_db -c "DELETE FROM users WHERE id='$USER_ID';"
echo "Données utilisateur $USER_ID purgées."

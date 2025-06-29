#!/bin/bash
# purge_data_script.sh – Purge sécurisée des données sensibles (RGPD)
# Usage : bash purge_data_script.sh /chemin/vers/dossier

set -e
TARGET=${1}
if [ -z "$TARGET" ]; then
  echo "Usage: $0 /chemin/vers/dossier" >&2
  exit 1
fi
find "$TARGET" -type f -name '*.sensitive' -exec shred -u {} \;
echo "[OK] Purge RGPD terminée dans $TARGET"

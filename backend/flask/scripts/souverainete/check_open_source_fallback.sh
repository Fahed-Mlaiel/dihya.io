#!/bin/bash
# Dihya – Script de vérification fallback IA open source (souveraineté numérique)
# Usage: bash check_open_source_fallback.sh
set -euo pipefail
FALLBACKS=("mixtral" "llama" "mistral")
for F in "${FALLBACKS[@]}"; do
  if pgrep -f "$F" >/dev/null; then
    echo "[OK] Fallback $F actif."
  else
    echo "[ALERTE] Fallback $F inactif !"; exit 2
  fi
done

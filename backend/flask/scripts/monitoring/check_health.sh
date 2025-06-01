#!/bin/bash
# Dihya – Script de healthcheck backend Flask
# Usage: bash check_health.sh
# Vérifie l’état de santé de l’API Flask (endpoint /api/health)
set -euo pipefail
API_URL="http://localhost:5000/api/health"
STATUS=$(curl -s "$API_URL" | grep 'ok')
if [[ -n "$STATUS" ]]; then
  echo "API Flask opérationnelle."
  exit 0
else
  echo "Erreur: API Flask non accessible ou en erreur."
  exit 1
fi

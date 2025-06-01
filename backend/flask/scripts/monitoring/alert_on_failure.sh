#!/bin/bash
# Dihya – Script d’alerte en cas d’échec de healthcheck
# Usage: bash alert_on_failure.sh
set -euo pipefail
if ! bash "$(dirname "$0")/check_health.sh"; then
  echo "[ALERTE] API Flask en erreur – $(date)" | mail -s "Alerte Dihya API" admin@dihya.local
fi

#!/bin/bash
# custom_alert_script.sh – Alerte sécurité personnalisée (exemple)
# Usage : bash custom_alert_script.sh

LOGFILE="/workspaces/dihya.io/backend/components/metiers/administration_publique/security/audit/audit_report_$(date +%Y-%m-%d).log"
THRESHOLD=5
COUNT=$(grep -c "Accès refusé" "$LOGFILE" || true)
if [ "$COUNT" -ge "$THRESHOLD" ]; then
  echo "[ALERTE] Trop d’accès refusés détectés ($COUNT) !" | mail -s "Alerte Sécurité administration_publique" admin@dihya.io
fi

#!/bin/bash
# audit_security.sh – Audit automatisé de la sécurité (permissions, logs, intégrité)

LOGFILE="/workspaces/dihya.io/backend/components/metiers/beaute/security/audit/audit_report_$(date +%Y-%m-%d).log"
echo "[AUDIT] Démarrage audit sécurité $(date)" > "$LOGFILE"

# Vérification des permissions critiques
find /workspaces/dihya.io/backend/components/metiers/beaute/security/ -type f -exec stat -c "%n %a" {} \; >> "$LOGFILE"

# Vérification de l’intégrité (hash)
find /workspaces/dihya.io/backend/components/metiers/beaute/security/ -type f -exec sha256sum {} \; >> "$LOGFILE"

echo "[AUDIT] Fin audit sécurité $(date)" >> "$LOGFILE"
echo "[OK] Rapport d’audit généré : $LOGFILE"

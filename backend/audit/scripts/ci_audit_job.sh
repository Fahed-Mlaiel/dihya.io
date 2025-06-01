#!/bin/bash
# Script CI/CD pour automatiser l’exécution de tous les audits Dihya et générer un rapport global
set -e
cd "$(dirname "$0")"

REPORT_DIR="../reports"
mkdir -p "$REPORT_DIR"

for script in check_integrity audit_rgpd audit_accessibilite audit_logs audit_plugins audit_webhooks; do
  echo "===== Exécution de $script ====="
  python3 main.py $script
  mv ${script}_report.csv "$REPORT_DIR/" 2>/dev/null || true
  mv ${script}_report.json "$REPORT_DIR/" 2>/dev/null || true
  echo "===== Fin $script =====\n"
done

# Fusionne tous les rapports JSON en un rapport global
jq -s '.' "$REPORT_DIR"/*_report.json > "$REPORT_DIR/rapport_global_audit.json" || echo '[WARN] Fusion JSON échouée (jq manquant?)'
# Fusionne tous les CSV en un rapport global
head -n 1 "$REPORT_DIR/check_integrity_report.csv" > "$REPORT_DIR/rapport_global_audit.csv"
grep -h -v '^file' "$REPORT_DIR"/*_report.csv >> "$REPORT_DIR/rapport_global_audit.csv"

echo "\nTous les audits CI/CD sont terminés. Rapport global généré dans $REPORT_DIR."

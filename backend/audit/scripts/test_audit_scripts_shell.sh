#!/bin/bash
# Tests unitaires ultra avancés pour scripts shell d’audit (run_all_audits.sh, ci_audit_job.sh)
# Vérifie l’exécution, la génération des rapports, la robustesse RGPD/auditabilité

set -e
cd "$(dirname "$0")"

# Nettoyage
rm -f ../reports/*_report.csv ../reports/*_report.json ../reports/rapport_global_audit.* 2>/dev/null || true

# Exécution des scripts
bash run_all_audits.sh
bash ci_audit_job.sh

# Vérification des rapports globaux
for f in rapport_global_audit.csv rapport_global_audit.json; do
  if [ ! -f "../reports/$f" ]; then
    echo "❌ Rapport $f manquant" >&2
    exit 1
  fi
  if ! grep -q -iE 'rapport|report' "../reports/$f"; then
    echo "❌ Rapport $f vide ou mal formé" >&2
    exit 1
  fi
  # Vérification RGPD (pas de données personnelles)
  if grep -iE 'nom réel|adresse|phone|téléphone|numéro|@gmail.com|@yahoo.com|dupont|durand|smith' "../reports/$f"; then
    echo "❌ Donnée personnelle détectée dans $f" >&2
    exit 1
  fi
  echo "✅ Rapport $f OK"
done

echo "✅ Tous les tests shell d’audit sont passés."

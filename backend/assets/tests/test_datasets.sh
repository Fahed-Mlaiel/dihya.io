#!/bin/bash
# Test automatisé des datasets (structure, RGPD, multilingue, anonymisation)
set -e
cd "$(dirname "$0")"
REPORT="test_datasets_report.txt"
echo "# Rapport d’audit des jeux de données – $(date)" > "$REPORT"

# Test JSON
for f in *.json; do
  jq . "$f" >/dev/null && echo "[OK] $f : JSON valide" || echo "[FAIL] $f : JSON invalide"
done

# Test CSV
for f in *.csv; do
  head -n 1 "$f" | grep -q ',' && echo "[OK] $f : CSV valide" || echo "[FAIL] $f : CSV invalide"
done

# Test YAML
for f in *.yaml; do
  python3 -c 'import yaml,sys; yaml.safe_load(open(sys.argv[1]))' "$f" && echo "[OK] $f : YAML valide" || echo "[FAIL] $f : YAML invalide"
done

# Vérification anonymisation
for f in *.json *.csv *.yaml; do
  grep -i -E 'nom|name|email|adresse|address|phone|téléphone|tel|numéro' "$f" && echo "[WARN] $f : Vérifier anonymisation" || echo "[OK] $f : Pas de données personnelles détectées"
done

# Vérification multilingue
for f in *.json *.yaml; do
  grep -q 'lang' "$f" && echo "[OK] $f : champ langue présent" >> "$REPORT" || echo "[WARN] $f : champ langue absent" >> "$REPORT"
done

echo "Audit terminé. Rapport : $REPORT"

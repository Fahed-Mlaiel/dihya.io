#!/bin/bash
# test_configs.sh – CI/CD : tests configs backend (lint YAML/JSON/TOML, RGPD, sécurité)
set -e

cd "$(dirname "$0")"

# Lint YAML
for yml in *.yaml; do
  yamllint "$yml" || { echo "[ERREUR] $yml : YAML invalide"; exit 1; }
  echo "[OK] $yml : YAML valide"
done

# Lint JSON
for js in *.json; do
  jq . "$js" > /dev/null || { echo "[ERREUR] $js : JSON invalide"; exit 1; }
  echo "[OK] $js : JSON valide"
done

# Lint TOML
for toml in *.toml; do
  python3 -c "import tomllib; tomllib.load(open('$toml', 'rb'))" || { echo "[ERREUR] $toml : TOML invalide"; exit 1; }
  echo "[OK] $toml : TOML valide"
done

echo "Tous les tests de configs sont passés."

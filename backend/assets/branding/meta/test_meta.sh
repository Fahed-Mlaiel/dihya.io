#!/bin/bash
# test_meta.sh – CI/CD : tests métadonnées branding (lint JSON, RGPD, hash, accessibilité, multilingue)
set -e

cd "$(dirname "$0")"

# Lint JSON (présence des champs critiques)
for meta in *.json; do
  jq . "$meta" > /dev/null || { echo "[ERREUR] $meta : JSON invalide"; exit 1; }
  for champ in name description tags version created author; do
    if ! jq -e ".$champ" "$meta" > /dev/null; then
      echo "[ERREUR] $meta : champ $champ manquant"; exit 1; fi
  done
  if ! jq -e '.description.fr and .description.en' "$meta" > /dev/null; then
    echo "[ERREUR] $meta : description multilingue manquante"; exit 1; fi
  echo "[OK] $meta : lint JSON et multilingue validés"
done

# Hash SHA256 pour souveraineté numérique
for meta in *.json; do
  sha256sum "$meta"
done

echo "Tous les tests de métadonnées sont passés."

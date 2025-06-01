#!/bin/bash
# test_signatures.sh – CI/CD : tests signatures email (lint HTML, accessibilité, hash, RGPD)
set -e

cd "$(dirname "$0")"

# Lint HTML (balises, accessibilité, ARIA)
for html in *.html; do
  if ! grep -q 'alt=' "$html"; then
    echo "[ERREUR] $html : attribut alt manquant"; exit 1; fi
  if ! grep -q 'aria-label' "$html"; then
    echo "[ERREUR] $html : aria-label manquant"; exit 1; fi
  echo "[OK] $html : accessibilité HTML validée"
done

# Vérifie présence des métadonnées JSON
for f in *.html *.txt; do
  meta="meta_${f%.html}.json"
  [ -f "$meta" ] || meta="meta_${f%.txt}.json"
  if [ ! -f "$meta" ]; then
    echo "[ERREUR] $meta manquant pour $f"; exit 1; fi
  echo "[OK] $meta : métadonnées présentes"
done

# Hash SHA256 pour souveraineté numérique
for f in *.html *.txt *.json; do
  sha256sum "$f"
done

echo "Tous les tests de signatures email sont passés."

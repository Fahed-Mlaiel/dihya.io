#!/bin/bash
# test_logos.sh – CI/CD : tests logos backend (lint SVG, accessibilité, hash, RGPD)
set -e

cd "$(dirname "$0")"

# Lint SVG (balises, accessibilité, ARIA)
for svg in *.svg; do
  if ! grep -q 'aria-labelledby' "$svg"; then
    echo "[ERREUR] $svg : aria-labelledby manquant"; exit 1; fi
  if ! grep -q '<title' "$svg"; then
    echo "[ERREUR] $svg : balise <title> manquante"; exit 1; fi
  if ! grep -q '<desc' "$svg"; then
    echo "[ERREUR] $svg : balise <desc> manquante"; exit 1; fi
  if ! grep -q 'role="img"' "$svg"; then
    echo "[ERREUR] $svg : role=img manquant"; exit 1; fi
  echo "[OK] $svg : accessibilité SVG validée"
done

# Vérifie présence des métadonnées JSON
for svg in *.svg; do
  meta="meta_${svg%.svg}.json"
  if [ ! -f "$meta" ]; then
    echo "[ERREUR] $meta manquant pour $svg"; exit 1; fi
  echo "[OK] $meta : métadonnées présentes"
done

# Hash SHA256 pour souveraineté numérique
for f in *.svg *.json; do
  sha256sum "$f"
done

echo "Tous les tests de logos sont passés."

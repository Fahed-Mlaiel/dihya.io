#!/bin/bash
# test_keys.sh – CI/CD : tests clés publiques (lint PEM, hash SHA256)
set -e

cd "$(dirname "$0")"

for key in *.pem; do
  if ! grep -q 'BEGIN PUBLIC KEY' "$key"; then
    echo "[ERREUR] $key : format PEM invalide (en-tête manquant)"; exit 1; fi
  if ! grep -q 'END PUBLIC KEY' "$key"; then
    echo "[ERREUR] $key : format PEM invalide (footer manquant)"; exit 1; fi
  echo "[OK] $key : format PEM valide"
  sha256sum "$key"
done

echo "Tous les tests de clés publiques sont passés."

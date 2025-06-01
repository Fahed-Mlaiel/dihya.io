#!/bin/bash
# Test automatisé des migrations SQL (PostgreSQL)
set -e
cd "$(dirname "$0")"

for f in *.sql; do
  echo "Testing migration $f..."
  psql -U dihya -d dihya -f "$f"
done

echo "Toutes les migrations SQL ont été appliquées avec succès."

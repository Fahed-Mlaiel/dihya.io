#!/bin/bash
# test_snippets.sh – CI/CD : tests automatisés pour tous les snippets Python
set -e

cd "$(dirname "$0")"

for snip in *_snippet.py; do
  echo "[TEST] $snip"
  python3 "$snip"
done

echo "Tous les tests de snippets sont passés."

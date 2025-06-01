#!/bin/bash
# test_plugins.sh – CI/CD : tests plugins dynamiques vr_ar (lint, hooks, RGPD, audit, i18n, accessibilité)
set -e

cd "$(dirname "$0")"

for plugin in plugin_*.py; do
  echo "[TEST] $plugin"
  python3 "$plugin"
done

echo "Tous les tests de plugins dynamiques sont passés."

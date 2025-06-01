#!/bin/bash
# Script batch pour exécuter tous les audits ultra avancés Dihya (intégrité, RGPD, accessibilité, logs, plugins, webhooks)
set -e
cd "$(dirname "$0")"

for script in check_integrity audit_rgpd audit_accessibilite audit_logs audit_plugins audit_webhooks; do
  echo "\n===== Exécution de $script ====="
  python3 main.py $script
  echo "===== Fin $script =====\n"
done

echo "\nTous les audits ont été exécutés. Rapports CSV/JSON générés."

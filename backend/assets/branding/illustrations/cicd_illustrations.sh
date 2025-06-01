#!/bin/bash
# Intégration CI/CD ultra avancée pour illustrations backend Dihya
# - Audit Python
# - Audit Node.js
# - Génération rapport global

set -e
cd "$(dirname "$0")"

python3 audit_illustrations.py
node audit_illustrations.js

cat audit_illustrations_report.json > report_illustrations_global.json

echo "CI/CD illustrations backend Dihya : OK"

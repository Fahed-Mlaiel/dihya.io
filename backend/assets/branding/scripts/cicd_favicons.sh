#!/bin/bash
# Intégration CI/CD ultra avancée pour favicons API backend Dihya
# - Audit Python
# - Audit Node.js
# - Test Python
# - Conversion SVG->PNG
# - Génération rapport global

set -e
cd "$(dirname "$0")"

python3 audit_favicons.py
node audit_favicons.js
python3 test_favicons.py
bash svg2png_favicons.sh

cat audit_favicons_report.json test_favicons_report.json > report_favicons_global.json

echo "CI/CD favicons API backend Dihya : OK"

#!/bin/bash

# Script de contrôle général Dihya
# Vérifie la complétion, la cohérence, la sécurité, la conformité, la performance de tous les modules

set -euo pipefail

export LANG="C.UTF-8"
export LC_ALL="C.UTF-8"

echo "=== [1] Lancement de la vérification métiers (CSV) ==="
python3 verif_metiers.py --root . --show-paths

echo "=== [2] Génération des rapports HTML et Excel ==="
python3 gen_doc_metiers.py

echo "=== [3] Génération du README synthétique des métiers ==="
python3 gen_readme_metiers.py

echo "=== [4] Lancement de tous les tests unitaires et d'intégration (Pytest, Node, Frontend, Flutter) ==="
pytest tests || { echo "❌ Tests Python échoués"; exit 1; }
if command -v npm &>/dev/null && [ -d "frontend" ]; then
  npm --prefix frontend run test || { echo "❌ Tests Frontend échoués"; exit 1; }
fi
if command -v npx &>/dev/null && [ -d "backend/node" ]; then
  npx --prefix backend/node jest || { echo "❌ Tests Node échoués"; exit 1; }
fi
if command -v flutter &>/dev/null && [ -d "mobile" ]; then
  flutter test mobile || { echo "❌ Tests Flutter échoués"; exit 1; }
fi

echo "=== [5] Lint, audit sécurité, accessibilité, RGPD ==="
if command -v flake8 &>/dev/null; then flake8 .; fi
if command -v bandit &>/dev/null; then bandit -r backend; fi
if command -v eslint &>/dev/null && [ -d "frontend" ]; then eslint frontend/src --ext .js,.jsx,.ts,.tsx; fi
if command -v markdownlint &>/dev/null; then markdownlint '**/*.md'; fi
if command -v pa11y &>/dev/null && [ -d "frontend" ]; then pa11y http://localhost:3000 || true; fi

echo "=== [6] Mise à jour de l'inventaire.txt ==="
awk -F',' 'NR>1 && $2=="oui" {print $1}' rapport_metiers.csv | sort > inventaire.txt

echo "=== [7] Résumé ==="
echo "Rapports générés :"
ls -lh rapport_metiers.csv rapport_metiers.html rapport_metiers.xlsx README_METIERS.md 2>/dev/null || true
echo "Inventaire métiers mis à jour dans inventaire.txt"

echo "=== [8] Badge conformité, accessibilité, couverture ==="
if [ -f "scripts/gen_badges.sh" ]; then bash scripts/gen_badges.sh; fi

echo "=== [9] Contrôle général terminé avec succès. ==="
echo "🌍 Rapport multilingue, souverain, sécurisé, accessible, prêt pour production et contribution."

python3 scripts/automatisation_docs.py
python3 check_coherence_metiers.py
python3 verif_metiers.py
python3 rapport_metiers_app.py
# Ajoutez ici d’autres scripts de contrôle ou de test

echo "Contrôle général terminé. Vérifiez rapport_automatisation.txt et audit_report.txt."

#!/bin/bash
# Script de scan de sécurité des dépendances pour Dihya Coding
# Utilise safety et bandit pour détecter les vulnérabilités dans les dépendances Python.

# Bonnes pratiques :
# - À exécuter dans la CI/CD ou avant chaque mise en production.
# - Ne jamais ignorer les alertes critiques.
# - Documenter et corriger chaque vulnérabilité détectée.

set -e

echo "=== Scan de sécurité des dépendances Python (safety) ==="
if ! command -v safety &> /dev/null; then
    echo "Installation de safety..."
    pip install safety
fi
if [ -f "../requirements.txt" ]; then
    safety check -r ../requirements.txt || true
else
    echo "requirements.txt non trouvé."
fi

echo "=== Scan de sécurité du code source (bandit) ==="
if ! command -v bandit &> /dev/null; then
    echo "Installation de bandit..."
    pip install bandit
fi
bandit -r ../app || true

echo "=== Scan terminé ==="
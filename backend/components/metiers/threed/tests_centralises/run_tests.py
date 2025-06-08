#!/usr/bin/env python3
"""
Entrée professionnelle pour les tests centralisés Threed.
Ajoute le chemin du module threed au sys.path avant d’exécuter pytest.
"""
import sys
import os
import subprocess

# Ajoute la racine du projet au PYTHONPATH (niveau /workspaces/dihya.io)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..'))
os.environ['PYTHONPATH'] = PROJECT_ROOT

# Lancement de pytest en mode module sur le dossier de tests centralisés avec --import-mode=importlib
result = subprocess.call([
    sys.executable, '-m', 'pytest', os.path.dirname(__file__), '--import-mode=importlib', '--maxfail=20', '--disable-warnings', '-v'
])
sys.exit(result)

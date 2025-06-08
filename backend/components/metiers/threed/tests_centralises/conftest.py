# conftest.py – Injection dynamique du PYTHONPATH pour tests centralisés threed
import sys
import os

# Ajoute la racine du projet au PYTHONPATH (niveau /workspaces/dihya.io)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

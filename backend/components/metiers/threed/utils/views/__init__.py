# __init__.py – Point d'entrée Python pour les utilitaires views du module threed
# Synchronisé avec l'entrée JS pour CI/CD, audit, conformité

import importlib
import os
import sys

subdirs = ['api', 'templates', 'admin', 'public', 'partials', 'conformity', 'threed']
current_dir = os.path.dirname(__file__)

for sub in subdirs:
    sub_path = os.path.join(current_dir, sub)
    if os.path.isdir(sub_path) and os.path.exists(os.path.join(sub_path, '__init__.py')):
        sys.path.insert(0, sub_path)
        importlib.import_module(sub)

# Suppression des références directes à views.py
# Tout doit passer par les sous-dossiers (ex: threed/)

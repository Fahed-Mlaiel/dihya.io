"""
Initialisation racine des blueprints (Python)
Importe dynamiquement tous les sous-dossiers métiers et expose leurs blueprints.
"""
import importlib
import os
import sys

__all__ = []
current_dir = os.path.dirname(__file__)
for name in os.listdir(current_dir):
    subdir = os.path.join(current_dir, name)
    if os.path.isdir(subdir) and os.path.exists(os.path.join(subdir, '__init__.py')):
        module = importlib.import_module(f'.{name}', __package__)
        globals()[name] = module
        __all__.append(name)

# Exemple d'utilisation :
# from blueprints import api, devops, webApp, mobileApp

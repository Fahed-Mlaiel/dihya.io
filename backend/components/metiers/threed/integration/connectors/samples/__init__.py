# __init__.py – Initialisation avancée du dossier samples (connectors)

"""
Ce fichier permet l’import dynamique, l’auto-discovery et l’extension future des exemples de connecteurs Threed.
- Prêt pour l’industrialisation, l’audit, la RGPD, l’accessibilité, la documentation et l’intégration CI/CD.
- Peut être enrichi pour charger dynamiquement tous les exemples Python présents dans ce dossier.
"""

import os
import importlib

__all__ = []

# Découverte dynamique des modules d’exemple
for file in os.listdir(os.path.dirname(__file__)):
    if file.startswith("example_") and file.endswith(".py"):
        module_name = file[:-3]
        module = importlib.import_module(f".{{}}".format(module_name), __package__)
        globals()[module_name] = module
        __all__.append(module_name)

# Import dynamique des sous-dossiers d'exemples (adapters, exporters, importers, plugins)
for subdir in ["adapters", "exporters", "importers", "plugins"]:
    try:
        module = importlib.import_module(f".{subdir}", __package__)
        globals()[subdir] = module
        __all__.append(subdir)
    except Exception:
        pass

# __init__.py du dossier tests_centralises

"""
Ce module permet d’importer dynamiquement tous les tests centralisés des modules métiers.
Il prépare l’environnement pour une exécution groupée, automatisée et extensible.
"""

from pathlib import Path
import importlib

__all__ = []
for module in Path(__file__).parent.parent.iterdir():
    tc = module / "tests_centralises"
    if module.is_dir() and tc.exists() and (tc / "__init__.py").exists():
        try:
            importlib.import_module(f"..{module.name}.tests_centralises", __package__)
            __all__.append(f"{module.name}.tests_centralises")
        except Exception:
            pass

del Path, importlib

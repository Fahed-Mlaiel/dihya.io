# __init__.py – Initialisation avancée du dossier helpers (legacy/tests_centralises)
import os
import importlib
__all__ = []
for subdir in ["core", "validators"]:
    try:
        module = importlib.import_module(f".{subdir}", __package__)
        globals()[subdir] = module
        __all__.append(subdir)
    except Exception:
        pass

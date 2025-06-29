"""
Initialisation des scripts DevOps (Python)
Découverte automatique de tous les scripts de build/déploiement
"""
import importlib
import os

__all__ = []
current_dir = os.path.dirname(__file__)
for f in os.listdir(current_dir):
    if f.endswith('.py') and f != '__init__.py':
        mod = importlib.import_module(f'.{f[:-3]}', __package__)
        globals()[f[:-3]] = mod
        __all__.append(f[:-3])

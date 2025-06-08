# Point d’entrée ultra avancé Python pour tous les samples
import importlib
import os

modules = [
    'access', 'audit', 'compliance', 'helpers', 'monitoring', 'policy', 'rbac', 'rgpd', 'scripts', 'validators'
]

for mod in modules:
    try:
        globals()[mod] = importlib.import_module(f'.{mod}', __package__)
    except Exception:
        pass

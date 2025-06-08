# Point d’entrée ultra avancé pour validators rgpd
import os
import importlib.util

__all__ = []
for f in os.listdir(os.path.dirname(__file__)):
    if f.startswith('sample_rgpd') and f.endswith('.py') and f != '__init__.py':
        mod_name = f[:-3]
        spec = importlib.util.spec_from_file_location(mod_name, os.path.join(os.path.dirname(__file__), f))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        globals()[mod_name] = mod
        __all__.append(mod_name)

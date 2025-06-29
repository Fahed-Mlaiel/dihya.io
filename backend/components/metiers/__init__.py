# Initialisation du package metiers

from pathlib import Path
import importlib

# Import dynamique de tous les sous-modules métiers
__all__ = []
for module in Path(__file__).parent.iterdir():
    if module.is_dir() and (module / "__init__.py").exists():
        try:
            importlib.import_module(f".{{}}".format(module.name), __package__)
            __all__.append(module.name)
        except Exception:
            pass  # On ignore les modules non importables

del Path, importlib

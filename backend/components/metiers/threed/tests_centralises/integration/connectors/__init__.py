# __init__.py – Tests d'intégration Connectors
import os
import importlib
__all__ = []
for subdir in ["adapters", "exporters", "importers", "plugins", "samples"]:
    try:
        module = importlib.import_module(f".{subdir}", __package__)
        globals()[subdir] = module
        __all__.append(subdir)
    except Exception:
        pass

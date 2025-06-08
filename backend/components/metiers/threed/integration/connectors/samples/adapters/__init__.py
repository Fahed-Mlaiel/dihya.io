# __init__.py – Initialisation avancée des exemples d'adapters

"""
Import dynamique, auto-discovery, extension future pour les exemples d'adapters Threed.
"""
import os
import importlib
__all__ = []
for file in os.listdir(os.path.dirname(__file__)):
    if file.startswith("example_") and file.endswith(".py"):
        module_name = file[:-3]
        module = importlib.import_module(f".{{}}".format(module_name), __package__)
        globals()[module_name] = module
        __all__.append(module_name)

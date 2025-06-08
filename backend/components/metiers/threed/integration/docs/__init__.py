"""
__init__.py – Initialisation ultra avancée du module docs integration Threed
"""
import importlib
import pkgutil
import os
import sys
__all__ = []
package_dir = os.path.dirname(__file__)
for finder, name, ispkg in pkgutil.iter_modules([package_dir]):
    if not name.startswith("_"):
        module = importlib.import_module(f"{__name__}.{name}")
        globals()[name] = module
        __all__.append(name)
# Import dynamique des modules de documentation commençant par doc_
for file in os.listdir(os.path.dirname(__file__)):
    if file.startswith("doc_") and file.endswith(".py"):
        module_name = file[:-3]
        module = importlib.import_module(f".{{}}".format(module_name), __package__)
        globals()[module_name] = module
        __all__.append(module_name)
if "pytest" in sys.modules or "unittest" in sys.modules:
    for finder, name, ispkg in pkgutil.iter_modules([package_dir]):
        if name.endswith("_test") or name.startswith("test_"):
            importlib.import_module(f"{__name__}.{name}")
def register_plugin(plugin):
    if hasattr(plugin, "register"):
        plugin.register(globals())
def audit():
    pass
def rgpd_check():
    pass
def accessibility_check():
    pass
def multilingual_init():
    pass
def generate_docs():
    pass

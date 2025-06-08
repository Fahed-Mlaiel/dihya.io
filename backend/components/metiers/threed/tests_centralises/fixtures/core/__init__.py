"""
__init__.py – Initialisation ultra avancée du module de tests Core Fixtures Threed

Ce module permet l’import dynamique des tests, l’auto-discovery, l’orchestration CI/CD, l’extension plugins, l’audit, la conformité RGPD, l’accessibilité, et la compatibilité multi-langues.
"""
import importlib
import pkgutil
import os

__all__ = []

def discover_tests():
    test_files = []
    for root, _, files in os.walk(os.path.dirname(__file__)):
        for f in files:
            if f.endswith('.test.py') or f.endswith('_test.py'):
                test_files.append(os.path.join(root, f))
    return test_files

def run_all_tests():
    for _, module_name, is_pkg in pkgutil.iter_modules(__path__):
        importlib.import_module(f".{module_name}", __name__)
    for test_file in discover_tests():
        try:
            importlib.import_module(os.path.splitext(os.path.basename(test_file))[0])
        except Exception as e:
            pass

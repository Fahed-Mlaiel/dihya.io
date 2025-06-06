"""
__init__.py – Initialisation avancée du module de tests Views Threed

Ce module permet l’import dynamique des tests, l’auto-discovery, et l’intégration CI/CD.
"""

import importlib
import pkgutil

def discover_tests():
    """Découverte automatique des tests du sous-module."""
    return [name for _, name, _ in pkgutil.iter_modules(__path__)]

def run_all_tests():
    """Point d’entrée pour exécuter tous les tests du sous-module."""
    for test in discover_tests():
        importlib.import_module(f".{test}", __name__)

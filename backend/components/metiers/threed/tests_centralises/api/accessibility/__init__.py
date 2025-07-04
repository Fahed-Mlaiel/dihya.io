"""
__init__.py – Initialisation avancée du sous-module accessibility (tests API)
Ce module permet l’import dynamique des tests, l’auto-discovery, et l’intégration CI/CD.
"""

import importlib
import pkgutil
import glob


def discover_tests():
    """Découverte automatique des tests du sous-module."""
    return [name for _, name, _ in pkgutil.iter_modules(__path__)]


def discover_tests_helpers():
    """Découverte automatique des tests et helpers pour accessibility."""
    return glob.glob('*.test.py')


def run_all_tests():
    """Point d’entrée pour exécuter tous les tests du sous-module."""
    for test in discover_tests():
        importlib.import_module(f".{{test}}", __name__)

    # Intégration CI/CD possible ici

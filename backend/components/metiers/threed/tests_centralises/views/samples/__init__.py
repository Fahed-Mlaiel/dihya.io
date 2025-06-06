"""
__init__.py – Initialisation avancée du sous-module de tests views/samples (Threed)
Ce module permet l’import dynamique des tests, l’auto-discovery, et l’intégration CI/CD.
"""
import importlib
import pkgutil
import glob

# Découverte automatique des tests et helpers pour views/samples
def discover_tests():
    return glob.glob('*.test.py')

def run_all_tests():
    """Point d’entrée pour exécuter tous les tests du sous-module."""
    for test in discover_tests():
        importlib.import_module(f".{{test}}", __name__)

# Initialisation du module de tests views/core
# Découverte automatique des tests, helpers, etc.
import glob

def discover_tests():
    return glob.glob('*.test.py')

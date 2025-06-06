# Initialisation du module de tests templates/core
# Découverte automatique des tests, helpers, etc.
import glob

def discover_tests():
    return glob.glob('*.test.py')

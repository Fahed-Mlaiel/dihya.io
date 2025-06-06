# Initialisation du module de tests views/helpers
# Découverte automatique des tests, helpers, etc.
import glob

def discover_tests():
    return glob.glob('*.test.py')

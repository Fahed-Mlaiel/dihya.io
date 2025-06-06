# Initialisation du module de tests utils/ai
# Découverte automatique des tests, helpers, etc.
import glob

def discover_tests():
    return glob.glob('*.test.py')

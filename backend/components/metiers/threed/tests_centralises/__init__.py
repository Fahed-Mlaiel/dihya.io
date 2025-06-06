# Initialisation du module de tests centralisés threed
# Découverte automatique de tous les tests, helpers, etc.
import glob

def discover_tests():
    return glob.glob('**/*.test.py', recursive=True)

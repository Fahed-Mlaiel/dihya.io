# Découverte automatique des tests et helpers pour middlewares
import glob

def discover_tests():
    return glob.glob('*.test.py')

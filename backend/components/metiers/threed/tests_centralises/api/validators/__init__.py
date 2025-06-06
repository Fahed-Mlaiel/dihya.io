# Découverte automatique des tests et helpers pour validators
import glob

def discover_tests():
    return glob.glob('*.test.py')

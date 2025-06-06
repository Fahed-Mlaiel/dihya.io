# Découverte automatique des tests et helpers pour samples
import glob

def discover_tests():
    return glob.glob('*.test.py')

# Découverte automatique des tests et helpers pour hooks
import glob

def discover_tests():
    return glob.glob('*.test.py')

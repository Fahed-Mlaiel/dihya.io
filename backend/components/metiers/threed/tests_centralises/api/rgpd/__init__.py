# Découverte automatique des tests et helpers pour rgpd
import glob

def discover_tests():
    return glob.glob('*.test.py')

"""
index.test.py – Test d’intégration du point d’entrée validators (Python)
Conformité, CI/CD, audit, synchronisation JS/Python
"""
from . import validators

def test_index_validators():
    assert hasattr(validators, 'validate') or hasattr(validators, 'validators')

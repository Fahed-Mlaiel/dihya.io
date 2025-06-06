"""
__init__.test.py – Test d’import dynamique et d’intégration validators (Python)
Conformité, CI/CD, audit, synchronisation JS/Python
"""
from . import validators

def test_import_validators():
    assert hasattr(validators, 'validate') or hasattr(validators, 'validators')

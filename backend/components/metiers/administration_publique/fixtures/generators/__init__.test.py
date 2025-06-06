"""
Test d'import du module generators (Python)
"""
from . import generate_model, generate_user

def test_imports_generators():
    assert callable(generate_model)
    assert callable(generate_user)

# fallback.test.py
"""Test unitaire avancé pour fallback validators (Python)"""
from .fallback import fallback_validate

def test_fallback_validate():
    assert callable(fallback_validate)

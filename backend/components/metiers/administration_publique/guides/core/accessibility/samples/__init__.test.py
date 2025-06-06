"""
Test d'import du module samples (Python)
"""
from .sample_fixture import *

def test_import_sample_accessibility_guide():
    assert callable(sample_accessibility_guide)

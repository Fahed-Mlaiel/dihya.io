"""
Test d'import du module samples (Python)
"""
from . import sample_helper_fixture

def test_import_sample_helper_fixture():
    assert callable(sample_helper_fixture)

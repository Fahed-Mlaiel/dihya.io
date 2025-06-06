"""
Tests unitaires pour guide_utils.py (Python)
"""
from guides.core.utils import guide_utils

def test_doc_existe():
    assert hasattr(guide_utils, 'doc')

"""
Tests unitaires pour guide_views.py (Python)
"""
from guides.core.views import guide_views

def test_doc_existe():
    assert hasattr(guide_views, 'doc')

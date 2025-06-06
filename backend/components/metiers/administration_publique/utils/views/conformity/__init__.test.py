"""
__init__.test.py – Test d’import dynamique et d’intégration conformity views threed (Python)
"""
from . import conformity_views

def test_import_conformity_views():
    assert hasattr(conformity_views, 'check_rgpd')
    assert hasattr(conformity_views, 'check_accessibility')

"""
__init__.test.py – Test d’import dynamique et d’intégration admin views threed (Python)
"""
from . import admin_views

def test_import_admin_views():
    assert hasattr(admin_views, 'admin_action')

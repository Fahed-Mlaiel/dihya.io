"""
__init__.test.py – Test d’import dynamique et d’intégration threed views (Python)
"""
from . import views

def test_import_threed_views():
    assert hasattr(views, 'render_threed')

"""
__init__.test.py – Test d’import dynamique et d’intégration partials views threed (Python)
"""
from . import partials_views

def test_import_partials_views():
    assert hasattr(partials_views, 'render_widget')

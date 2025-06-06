"""
__init__.test.py – Test d’import dynamique et d’intégration templates views threed (Python)
"""
from . import templates_views

def test_import_templates_views():
    assert hasattr(templates_views, 'render_template')

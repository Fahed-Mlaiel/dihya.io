"""
__init__.test.py – Test d’import dynamique et d’intégration API views threed (Python)
"""
from . import api_views

def test_import_api_views():
    assert hasattr(api_views, 'render_threed_api')

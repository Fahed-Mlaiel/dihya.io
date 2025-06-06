# __init__.test.py – Test d'initialisation Python views (conformité, CI/CD, audit, synchronisation JS/Python)
from . import views

def test_import_views():
    assert hasattr(views, 'render_threed') or hasattr(views, 'renderView')

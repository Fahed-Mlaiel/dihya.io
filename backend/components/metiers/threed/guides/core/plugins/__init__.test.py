# __init__.test.py – Test d’import du point d’entrée Python
def test_import_init():
    from . import get_plugins_guide
    assert callable(get_plugins_guide)

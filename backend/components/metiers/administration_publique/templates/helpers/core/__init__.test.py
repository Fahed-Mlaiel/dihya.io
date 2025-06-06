# __init__.test.py – Test d’import du point d’entrée Python helpers/core

def test_import_init():
    import importlib
    mod = importlib.import_module('templates.helpers.core.__init__')
    assert mod is not None

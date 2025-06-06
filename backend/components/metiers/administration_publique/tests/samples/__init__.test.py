# __init__.test.py – Test d’import du point d’entrée Python samples

def test_import_init():
    import importlib
    mod = importlib.import_module('tests.samples.__init__')
    assert mod is not None

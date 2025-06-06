# __init__.test.py – Test d’import du point d’entrée Python helpers IA

def test_import_init():
    import importlib
    mod = importlib.import_module('utils.ai.helpers.__init__')
    assert mod is not None

# __init__.test.py – Test d’import du point d’entrée Python utils/ai/core

def test_import_init():
    import importlib
    mod = importlib.import_module('utils.ai.core.__init__')
    assert mod is not None

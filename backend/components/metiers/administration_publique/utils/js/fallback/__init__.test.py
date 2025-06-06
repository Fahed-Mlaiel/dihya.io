# __init__.test.py – Test d'import du point d'entrée fallback JS (clé en main)
def test_import_fallback_js_init():
    import importlib
    module = importlib.import_module('.__init__', package=__package__)
    assert hasattr(module, 'fallback_value')

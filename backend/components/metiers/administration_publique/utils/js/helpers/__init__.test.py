# __init__.test.py – Test d'import du point d'entrée helpers JS (clé en main)
def test_import_helpers_js_init():
    import importlib
    module = importlib.import_module('.__init__', package=__package__)
    assert hasattr(module, 'to_camel_case')

# Test d'import du point d'entrée samples JS (Python, clé en main)
def test_import_samples_js_init():
    import importlib
    module = importlib.import_module('.__init__', package=__package__)
    assert hasattr(module, 'sample_js_helper')

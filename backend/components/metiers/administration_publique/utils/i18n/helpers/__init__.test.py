# Test d'import du point d'entrée helpers i18n (Python)
def test_import_helpers_i18n_init():
    import importlib
    module = importlib.import_module('.__init__', package=__package__)
    assert module is not None

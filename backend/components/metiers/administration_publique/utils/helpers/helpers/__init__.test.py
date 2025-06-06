# Test d'import du point d'entrée helpers/helpers (Python)
def test_import_helpers_helpers_init():
    import importlib
    module = importlib.import_module('.__init__', package=__package__)
    assert module is not None

# Test d'import du point d'entrée fallback logger (Python)
def test_import_fallback_logger_init():
    import importlib
    module = importlib.import_module('.__init__', package=__package__)
    assert module is not None

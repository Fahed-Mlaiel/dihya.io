# Test d'import du point d'entrée fallback audit (Python)
def test_import_fallback_audit_init():
    import importlib
    module = importlib.import_module('.__init__', package=__package__)
    assert module is not None

# Test d'import du point d'entrée samples audit (Python)
def test_import_samples_audit_init():
    import importlib
    module = importlib.import_module('.__init__', package=__package__)
    assert module is not None

# __init__.test.py – Test d'import du point d'entrée Python samples avancés (guides/core/samples/samples)
def test_import_samples_init():
    import importlib
    samples = importlib.import_module('backend.components.metiers.threed.guides.core.samples.samples')
    assert samples.sample_accessibility_case is not None
    assert samples.sample_audit_case is not None

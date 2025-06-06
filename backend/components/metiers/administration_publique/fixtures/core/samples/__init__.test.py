# __init__.test.py – Test d'import du point d'entrée Python samples (fixtures/core/samples)
def test_import_samples_init():
    import importlib
    samples = importlib.import_module('backend.components.metiers.threed.fixtures.core.samples')
    assert samples is not None

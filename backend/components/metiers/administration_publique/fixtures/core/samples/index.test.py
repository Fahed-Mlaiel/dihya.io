# index.test.py – Test d'import du point d'entrée principal Python samples (fixtures/core/samples)
def test_import_samples_index():
    import importlib
    samples_index = importlib.import_module('backend.components.metiers.threed.fixtures.core.samples.index')
    assert samples_index is not None

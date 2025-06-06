# index.test.py – Test d'import du point d'entrée principal Python samples (fixtures/helpers/samples)
def test_import_samples_index():
    import importlib
    samples_index = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.samples.index')
    assert samples_index.sample_helper_fixture is not None

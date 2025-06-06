# __init__.test.py – Test d'import du point d'entrée Python samples (fixtures/helpers/samples)
def test_import_samples_init():
    import importlib
    samples = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.samples')
    assert samples.sample_helper_fixture is not None

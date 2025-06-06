# __init__.test.py – Test d'import du point d'entrée Python samples (guides/fallback/samples)
def test_import_samples_init():
    import importlib
    samples = importlib.import_module('backend.components.metiers.threed.guides.fallback.samples')
    assert samples.sample_fallback_case is not None

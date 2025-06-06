# __init__.test.py – Test d'import du point d'entrée Python samples (guides/core/samples)
def test_import_samples_init():
    import importlib
    samples = importlib.import_module('backend.components.metiers.threed.guides.core.samples')
    assert samples.sample_guide_doc is not None

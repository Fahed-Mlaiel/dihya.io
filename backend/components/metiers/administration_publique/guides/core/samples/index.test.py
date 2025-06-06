# index.test.py – Test d'import du point d'entrée principal Python samples (guides/core/samples)
def test_import_samples_index():
    import importlib
    samples_index = importlib.import_module('backend.components.metiers.threed.guides.core.samples.index')
    assert samples_index.sample_guide_doc is not None

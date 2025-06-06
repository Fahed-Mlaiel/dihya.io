"""
__init__.test.py
Test d'import du point d'entrée Python du sous-module samples
"""
def test_import_samples_init():
    import backend.components.metiers.threed.plugins.core.samples
    from backend.components.metiers.threed.plugins.core.samples import SamplePlugin
    assert SamplePlugin is not None

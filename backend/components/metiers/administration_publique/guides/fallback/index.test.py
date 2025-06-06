# index.test.py – Test d'import du point d'entrée principal Python guides/fallback
def test_import_fallback_index():
    import importlib
    fallback_index = importlib.import_module('backend.components.metiers.threed.guides.fallback.index')
    assert fallback_index is not None

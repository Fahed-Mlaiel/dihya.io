# index.test.py – Test d'import du point d'entrée principal Python guides/helpers
def test_import_helpers_index():
    import importlib
    helpers_index = importlib.import_module('backend.components.metiers.threed.guides.helpers.index')
    assert helpers_index is not None

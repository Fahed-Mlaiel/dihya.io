# __init__.test.py – Test d'import du point d'entrée Python helpers (fixtures/helpers/helpers)
def test_import_helpers_init():
    import importlib
    helpers = importlib.import_module('backend.components.metiers.threed.fixtures.helpers.helpers')
    assert helpers is not None

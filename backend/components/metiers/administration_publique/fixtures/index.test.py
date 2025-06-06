# index.test.py – Test d'import du point d'entrée principal Python fixtures (fixtures/index.py)
def test_import_fixtures_index():
    import importlib
    fixtures_index = importlib.import_module('backend.components.metiers.threed.fixtures.index')
    assert fixtures_index is not None

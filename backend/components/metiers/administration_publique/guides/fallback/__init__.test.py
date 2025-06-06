# __init__.test.py – Test d'import du point d'entrée Python guides/fallback
def test_import_fallback_init():
    import importlib
    fallback = importlib.import_module('backend.components.metiers.threed.guides.fallback')
    assert fallback is not None

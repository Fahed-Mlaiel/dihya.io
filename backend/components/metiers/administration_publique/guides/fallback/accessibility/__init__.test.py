# __init__.test.py – Test d'import du point d'entrée Python accessibility (guides/fallback/accessibility)
def test_import_accessibility_init():
    import importlib
    accessibility = importlib.import_module('backend.components.metiers.threed.guides.fallback.accessibility')
    assert accessibility.fallback_accessibility is not None

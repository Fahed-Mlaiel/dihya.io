# __init__.test.py – Test d'import du point d'entrée Python accessibility (guides/helpers/accessibility)
def test_import_accessibility_init():
    import importlib
    accessibility = importlib.import_module('backend.components.metiers.threed.guides.helpers.accessibility')
    assert accessibility.check_accessibility
    assert accessibility.audit_accessibility

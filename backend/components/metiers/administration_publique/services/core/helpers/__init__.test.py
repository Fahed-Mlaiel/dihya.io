"""
__init__.test.py
Test d'import du point d'entrée Python du sous-module helpers
"""
def test_import_helpers_init():
    import backend.components.metiers.threed.services.core.helpers
    from backend.components.metiers.threed.services.core.helpers import ServicesHelper
    assert ServicesHelper is not None

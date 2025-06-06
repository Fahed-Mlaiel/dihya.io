"""
__init__.test.py
Test d'import du point d'entrée Python du sous-module api
"""
def test_import_api_init():
    import backend.components.metiers.threed.services.core.api
    from backend.components.metiers.threed.services.core.api import ApiService
    assert ApiService is not None

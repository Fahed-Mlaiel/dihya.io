"""
__init__.test.py
Test d'import du point d'entrée Python du sous-module impl
"""
def test_import_impl_init():
    import backend.components.metiers.threed.services.core.impl
    from backend.components.metiers.threed.services.core.impl import ServiceThreed
    assert ServiceThreed is not None

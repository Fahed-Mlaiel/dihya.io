"""
__init__.test.py
Test d'import du point d'entrée Python du sous-module controllers
"""
def test_import_controllers_init():
    import backend.components.metiers.threed.services.core.controllers
    from backend.components.metiers.threed.services.core.controllers import ServicesController
    assert ServicesController is not None

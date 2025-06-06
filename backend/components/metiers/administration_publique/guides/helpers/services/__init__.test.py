# __init__.test.py – Test d'import du point d'entrée Python services (guides/helpers/services)
def test_import_services_init():
    import importlib
    services = importlib.import_module('backend.components.metiers.threed.guides.helpers.services')
    assert services.check_service
    assert services.audit_service

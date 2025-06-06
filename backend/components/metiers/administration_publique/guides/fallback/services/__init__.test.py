# __init__.test.py – Test d'import du point d'entrée Python services (guides/fallback/services)
def test_import_services_init():
    import importlib
    services = importlib.import_module('backend.components.metiers.threed.guides.fallback.services')
    assert services.fallback_services is not None

# __init__.test.py – Test d’import du point d’entrée Python
def test_import_init():
    from . import get_service_guide
    assert callable(get_service_guide)

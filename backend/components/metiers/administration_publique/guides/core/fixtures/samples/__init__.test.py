# __init__.test.py – Test d’import du point d’entrée Python
def test_import_init():
    from . import default_sample
    assert default_sample is not None

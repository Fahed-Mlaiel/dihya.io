from . import metier_legacy_core

def test_import_metier_legacy_core():
    assert metier_legacy_core is not None
    assert metier_legacy_core({'x': 2}) == {'x': 2, 'legacy': True}

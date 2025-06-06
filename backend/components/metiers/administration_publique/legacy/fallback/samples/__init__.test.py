# __init__.test.py – Test d’import du point d’entrée Python samples legacy fallback
from . import sample_fallback_legacy

def test_import_sample_fallback_legacy():
    assert sample_fallback_legacy is not None
    assert sample_fallback_legacy({'x': 2}) == {'x': 2, 'fallback': True}

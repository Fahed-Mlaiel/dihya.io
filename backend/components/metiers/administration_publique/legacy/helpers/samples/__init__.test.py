# __init__.test.py – Test d’import du point d’entrée Python samples legacy helpers
from . import sample_helper_legacy

def test_import_sample_helper_legacy():
    assert sample_helper_legacy is not None
    assert sample_helper_legacy({'x': 2}) == {'x': 2, 'helper': True}

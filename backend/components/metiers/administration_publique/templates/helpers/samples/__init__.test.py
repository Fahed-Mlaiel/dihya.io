# __init__.test.py – Test d’import du point d’entrée Python samples helpers templates
from . import sample_helper_template

def test_import_sample_helper_template():
    assert sample_helper_template is not None
    assert sample_helper_template({'x': 2}) == {'x': 2, 'helper': True}

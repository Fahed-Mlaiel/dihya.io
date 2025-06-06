# generic_helper.test.py
# Tests unitaires Python pour generic_helper
from .generic_helper import capitalize_first

def test_capitalize_first():
    assert capitalize_first('hello') == 'Hello'

def test_capitalize_first_empty():
    assert capitalize_first('') == ''

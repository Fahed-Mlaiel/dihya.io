# js_core.test.py
# Tests unitaires Python pour js_core (équivalent JS, ultra avancé)
from .js_core import is_plain_object

def test_is_plain_object_dict():
    assert is_plain_object({'a': 1}) is True

def test_is_plain_object_list():
    assert is_plain_object([1,2,3]) is False

def test_is_plain_object_none():
    assert is_plain_object(None) is False

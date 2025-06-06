# js_helper.test.py
# Tests unitaires Python pour js_helper (équivalent JS, ultra avancé)
from .js_helper import to_camel_case

def test_to_camel_case_simple():
    assert to_camel_case('hello_world') == 'helloWorld'

def test_to_camel_case_single():
    assert to_camel_case('hello') == 'hello'

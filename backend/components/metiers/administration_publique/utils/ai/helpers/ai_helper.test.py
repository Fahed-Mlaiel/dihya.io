# ai_helper.test.py
# Tests unitaires Python pour ai_helper
from .ai_helper import normalize_text

def test_normalize_text():
    assert normalize_text('  Héllo   Wôrld  ') == 'Hello World'

def test_normalize_text_empty():
    assert normalize_text('') == ''

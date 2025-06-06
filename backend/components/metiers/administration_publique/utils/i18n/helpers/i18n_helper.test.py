# i18n_helper.test.py
# Tests unitaires Python pour i18n_helper
from .i18n_helper import humanize_key

def test_humanize_key():
    assert humanize_key('HELLO_WORLD') == 'hello world'

def test_humanize_key_empty():
    assert humanize_key('') == ''

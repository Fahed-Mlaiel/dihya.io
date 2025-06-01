"""
Tests unitaires pour les utilitaires du core backend Dihya
- Multilingue, logs structurés, validation, CI/CD
"""
import sys
sys.path.insert(0, '.')
from flask import Flask, request
import pytest

from backend.core import utils

class DummyRequest:
    def __init__(self, lang):
        self.headers = {'X-Dihya-Lang': lang}

@pytest.mark.parametrize("lang,expected", [
    ("fr", "fr"), ("en", "en"), ("ar", "ar"), ("tzm", "tzm"), ("de", "de"), ("zh", "zh"),
    ("ja", "ja"), ("ko", "ko"), ("nl", "nl"), ("he", "he"), ("fa", "fa"), ("hi", "hi"), ("es", "es"),
    ("xx", "fr")
])
def test_get_lang(monkeypatch, lang, expected):
    monkeypatch.setattr(utils, 'request', DummyRequest(lang))
    assert utils.get_lang() == expected

def test_log_structured(caplog):
    entry = utils.log_structured('info', 'Test log', foo='bar')
    assert entry['level'] == 'info'
    assert entry['message'] == 'Test log'
    assert entry['foo'] == 'bar'

def test_validate_schema():
    schema = {'a': int, 'b': str}
    data = {'a': 1, 'b': 'x'}
    assert utils.validate_schema(data, schema)
    with pytest.raises(ValueError):
        utils.validate_schema({'a': 1}, schema)

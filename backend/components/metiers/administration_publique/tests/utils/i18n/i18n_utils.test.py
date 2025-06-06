# i18n_utils.test.py – Tests unitaires ultra avancés pour i18n_utils.py
import pytest
from .i18n_utils import translate, is_supported_lang, SUPPORTED_LANGS

def test_translate_supported_langs():
    for lang in SUPPORTED_LANGS:
        assert f'[{lang.upper()}]' in translate('Test', lang)

def test_translate_unsupported_lang():
    assert translate('Test', 'xx') == 'Test'

def test_is_supported_lang():
    assert is_supported_lang('fr')
    assert is_supported_lang('en')
    assert not is_supported_lang('xx')

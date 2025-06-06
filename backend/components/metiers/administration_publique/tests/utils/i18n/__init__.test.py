# __init__.test.py – Test d'import global du module i18n (Python)
from . import *

def test_import_i18n_utils():
    assert callable(translate)
    assert callable(is_supported_lang)
    assert isinstance(SUPPORTED_LANGS, list)

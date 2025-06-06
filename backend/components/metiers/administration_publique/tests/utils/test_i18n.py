from .i18n.i18n_utils import translate, is_supported_lang

def test_translation():
    assert translate("hello", "fr") == "bonjour"
    assert translate("goodbye", "fr") == "au revoir"
    assert translate("hello", "es") == "hola"
    assert translate("goodbye", "es") == "adiós"

def test_supported_lang():
    assert is_supported_lang("fr") is True
    assert is_supported_lang("es") is True
    assert is_supported_lang("de") is False

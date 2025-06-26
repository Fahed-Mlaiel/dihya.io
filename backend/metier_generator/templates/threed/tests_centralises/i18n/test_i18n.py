"""
Test centralisé i18n threed (Python).
"""

from ...i18n import translate, get_available_languages


def test_translate_existing_key():
    assert translate("welcome", "fr") == "Bienvenue"


def test_available_languages():
    langs = get_available_languages()
    assert "fr" in langs
    assert "en" in langs


def test_translate_missing_key():
    assert translate("not_found", "zz") == "not_found"

"""
Tests ultra avancés pour le module validators Dihya.
- Couverture unitaire, intégration, multilingue, sécurité, fallback IA open source.
- Compatible CI/CD, zéro faux positif, prêt pour Codespaces.
"""

import sys
sys.path.insert(0, '.')
from backend.django.app.templates.validators.template import ValidatorsTemplate
import pytest

@pytest.mark.parametrize("lang", ['fr', 'en', 'ar', 'ber'])
def test_supported_languages(lang):
    v = ValidatorsTemplate(lang=lang)
    assert lang in v.get_supported_languages()
    assert v.lang == lang

@pytest.mark.parametrize("email,lang,expected,msg_key", [
    ("test@dihya.eu", "fr", True, "email_valid"),
    ("test@dihya.eu", "en", True, "email_valid"),
    ("test@dihya.eu", "ar", True, "email_valid"),
    ("test@dihya.eu", "ber", True, "email_valid"),
    ("notanemail", "fr", False, "email_invalid"),
    ("notanemail", "en", False, "email_invalid"),
    ("notanemail", "ar", False, "email_invalid"),
    ("notanemail", "ber", False, "email_invalid"),
])
def test_validate_email(email, lang, expected, msg_key):
    v = ValidatorsTemplate(lang=lang)
    is_valid, msg = v.validate_email(email)
    assert is_valid == expected
    assert msg == v.MESSAGES[msg_key][lang]

@pytest.mark.parametrize("password,lang,expected,msg_key", [
    ("S3cur3!", "fr", False, "password_weak"),  # trop court
    ("S3cur3!ok", "fr", True, "password_strong"),
    ("S3cur3!ok", "en", True, "password_strong"),
    ("S3cur3!ok", "ar", True, "password_strong"),
    ("S3cur3!ok", "ber", True, "password_strong"),
    ("weak", "fr", False, "password_weak"),
    ("weak", "en", False, "password_weak"),
    ("weak", "ar", False, "password_weak"),
    ("weak", "ber", False, "password_weak"),
])
def test_validate_password(password, lang, expected, msg_key):
    v = ValidatorsTemplate(lang=lang)
    is_strong, msg = v.validate_password(password)
    assert is_strong == expected
    assert msg == v.MESSAGES[msg_key][lang]

@pytest.mark.parametrize("field,value,lang,expected", [
    ("email", "notanemail", "fr", "Suggestion IA : Corrigez le champ email."),
    ("email", "notanemail", "en", "AI Suggestion: Please correct the email field."),
    ("email", "notanemail", "ar", "اقتراح الذكاء الاصطناعي: يرجى تصحيح الحقل email."),
    ("email", "notanemail", "ber", "ⴰⵎⵙⵙⴰⵍ ⴷ ⵉⴳⴳⴰⵔⴰⵡ: ⴰⴷⴷⴰⵔ email."),
])
def test_fallback_ai(field, value, lang, expected):
    v = ValidatorsTemplate(lang=lang)
    suggestion = v.fallback_ai(field, value)
    assert suggestion == expected

def test_get_supported_languages():
    v = ValidatorsTemplate()
    langs = v.get_supported_languages()
    assert set(['fr', 'en', 'ar', 'ber']).issubset(set(langs))

# Sécurité : pas de fuite de données, pas d'injection
def test_no_injection_email():
    v = ValidatorsTemplate()
    is_valid, msg = v.validate_email("test@dihya.eu<script>")
    assert not is_valid
    assert "invalide" in msg or "Invalid" in msg or "غير صالح" in msg or "ⴰⴷⵔⴰⵙ" in msg

def test_no_injection_password():
    v = ValidatorsTemplate()
    is_strong, msg = v.validate_password("S3cur3!<script>")
    assert not is_strong
    assert "faible" in msg or "Weak" in msg or "ضعيفة" in msg or "ⴰⵎⴰⵣⵉⵖ" in msg

# Accessibilité : les messages sont localisés
def test_accessibility_messages():
    for lang in ['fr', 'en', 'ar', 'ber']:
        v = ValidatorsTemplate(lang=lang)
        _, msg = v.validate_email("notanemail")
        assert isinstance(msg, str)
        _, msg = v.validate_password("weak")
        assert isinstance(msg, str)

# Test d'intégration rapide (smoke test)
def test_smoke():
    v = ValidatorsTemplate()
    assert v.validate_email("test@dihya.eu")[0] is True
    assert v.validate_password("S3cur3!ok")[0] is True
    assert "Suggestion" in v.fallback_ai("email", "notanemail", lang="fr")

"""
Pour lancer les tests :
    pytest test_validators.py

Ce fichier garantit une couverture maximale, multilingue, sécurité, fallback IA, accessibilité, CI/CD.
"""

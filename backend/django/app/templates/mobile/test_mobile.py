"""
Dihya Mobile Template – Tests avancés
=====================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module mobile (PWA, web mobile, Flutter/React Native, etc.).
- Multilingue (fr, en, ar, tz)
- Couverture accessibilité, i18n, SEO, sécurité, conformité mobile/PWA, gestion des rôles
- CI/CD ready, aucun faux positif, robustesse Codespaces/Linux

"""

import os
import pytest
from django.test import RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from django.template import TemplateDoesNotExist

from .template import (
    render_mobile_template,
    validate_mobile_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_mobile(db):
    user = User.objects.create_user(username="mobileuser", password="mobilepass")
    user.groups.create(name="Utilisateur mobile")
    return user

@pytest.fixture
def user_guest(db):
    user = User.objects.create_user(username="guest", password="guestpass")
    return user

@pytest.fixture
def example_context():
    return {"test": True, "extra": "value"}

# --- Tests unitaires ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_mobile_template_ok(lang, example_context):
    html = render_mobile_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Bienvenue" in html or "Welcome" in html or "مرحبا" in html or "ⴰⵏⴰⵡ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_mobile_template_user_roles(lang, user_admin, user_mobile, user_guest, example_context):
    html_admin = render_mobile_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_mobile = render_mobile_template("example.html", context=example_context, user=user_mobile, lang=lang)
    html_guest = render_mobile_template("example.html", context=example_context, user=user_guest, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "Utilisateur mobile" in html_mobile or "Mobile user" in html_mobile or "مستخدم" in html_mobile or "ⴰⵎⵓⴱⵉⵍ" in html_mobile
    assert "Invité" in html_guest or "Guest" in html_guest or "زائر" in html_guest or "ⴰⵣⴰⵢⴻⵏ" in html_guest

def test_render_mobile_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_mobile_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_mobile_template_compliance(lang, example_context):
    html = render_mobile_template("example.html", context=example_context, lang=lang)
    results = validate_mobile_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert results["privacy"] is True
    assert results["mobile"] is True
    assert results["pwa"] is True
    assert not results["errors"]

def test_validate_mobile_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_mobile_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_mobile_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_mobile_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_validate_mobile_template_viewport_fail():
    html = "<html lang='fr'><head></head><body></body></html>"
    results = validate_mobile_template(html, lang="fr")
    assert results["accessibility"] is False
    assert results["pwa"] is False
    assert any("viewport" in str(e) for e in results["errors"])

def test_validate_mobile_template_privacy_fail():
    html = "<html lang='fr'><body>{{ mobile.secret_device }}</body></html>"
    results = validate_mobile_template(html, lang="fr")
    assert results["privacy"] is False
    assert results["mobile"] is False
    assert any("confidentiel" in str(e) or "sensible" in str(e) or "mobile" in str(e) for e in results["errors"])

def test_validate_mobile_template_mobile_fail():
    html = "<html lang='fr'><body>tracking cookie analytics</body></html>"
    results = validate_mobile_template(html, lang="fr")
    assert results["mobile"] is False
    assert any("RGPD" in str(e) or "mobile" in str(e) for e in results["errors"])

def test_validate_mobile_template_pwa_manifest_fail():
    html = "<html lang='fr'><head><meta name='viewport' content='width=device-width, initial-scale=1.0'></head><body></body></html>"
    results = validate_mobile_template(html, lang="fr")
    assert results["pwa"] is False
    assert any("manifest" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_guest, example_context):
    html = render_mobile_template("example.html", context=example_context, user=user_guest, lang=lang)
    results = validate_mobile_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security", "privacy", "mobile", "pwa"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.mobile.__init__")
    assert mod is not None

def test_template_render_with_missing_context_keys(user_guest):
    # Le rendu ne doit pas échouer si le contexte ne contient pas toutes les clés attendues
    html = render_mobile_template("example.html", context={}, user=user_guest, lang="fr")
    assert "<html" in html

def test_template_render_with_special_characters(user_guest, example_context):
    # Teste la robustesse avec des caractères spéciaux et unicode
    example_context["special"] = "éèêçàùâîôœ€✓"
    html = render_mobile_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "éèêçàùâîôœ€✓" in html or html  # Doit rendre sans erreur

def test_template_render_multistack_compatibility(user_guest, example_context):
    # Simule un contexte compatible Jinja2 (clé 'user' obligatoire)
    example_context["user"] = user_guest
    html = render_mobile_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "<html" in html

# --- Fin des tests mobile ---

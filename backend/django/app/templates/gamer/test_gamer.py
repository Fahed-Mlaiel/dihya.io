"""
Dihya Gamer Template – Tests avancés
====================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module gamer.
- Multilingue (fr, en, ar, tz)
- Couverture accessibilité, i18n, SEO, sécurité, gestion des rôles
- CI/CD ready, aucun faux positif, robustesse Codespaces/Linux

"""

import os
import pytest
from django.test import RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from django.template import TemplateDoesNotExist

from .template import (
    render_gamer_template,
    validate_gamer_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_player(db):
    user = User.objects.create_user(username="player", password="playerpass")
    return user

@pytest.fixture
def example_context():
    return {"test": True, "extra": "value"}

# --- Tests unitaires ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_gamer_template_ok(lang, example_context):
    html = render_gamer_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Bienvenue" in html or "Welcome" in html or "مرحبا" in html or "ⴰⵏⴰⵡ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_gamer_template_user_roles(lang, user_admin, user_player, example_context):
    html_admin = render_gamer_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_player = render_gamer_template("example.html", context=example_context, user=user_player, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "Joueur" in html_player or "Player" in html_player or "لاعب" in html_player or "ⴰⵎⴰⵢⵏⵓⵜ" in html_player

def test_render_gamer_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_gamer_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_gamer_template_compliance(lang, example_context):
    html = render_gamer_template("example.html", context=example_context, lang=lang)
    results = validate_gamer_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert not results["errors"]

def test_validate_gamer_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_gamer_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_gamer_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_gamer_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_player, example_context):
    html = render_gamer_template("example.html", context=example_context, user=user_player, lang=lang)
    results = validate_gamer_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.gamer.__init__")
    assert mod is not None

# --- Fin des tests gamer ---

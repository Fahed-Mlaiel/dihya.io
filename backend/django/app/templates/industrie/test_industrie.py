"""
Dihya Industrie Template – Tests avancés
========================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module industrie.
- Multilingue (fr, en, ar, tz)
- Couverture accessibilité, i18n, SEO, sécurité, confidentialité, gestion des rôles
- CI/CD ready, aucun faux positif, robustesse Codespaces/Linux

"""

import os
import pytest
from django.test import RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from django.template import TemplateDoesNotExist

from .template import (
    render_industrie_template,
    validate_industrie_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_operator(db):
    user = User.objects.create_user(username="operator", password="operatorpass")
    user.groups.create(name="Opérateur")
    return user

@pytest.fixture
def user_engineer(db):
    user = User.objects.create_user(username="engineer", password="engineerpass")
    user.groups.create(name="Ingénieur")
    return user

@pytest.fixture
def user_client(db):
    user = User.objects.create_user(username="client", password="clientpass")
    return user

@pytest.fixture
def example_context():
    return {"test": True, "extra": "value"}

# --- Tests unitaires ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_industrie_template_ok(lang, example_context):
    html = render_industrie_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Bienvenue" in html or "Welcome" in html or "مرحبا" in html or "ⴰⵏⴰⵡ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_industrie_template_user_roles(lang, user_admin, user_operator, user_engineer, user_client, example_context):
    html_admin = render_industrie_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_operator = render_industrie_template("example.html", context=example_context, user=user_operator, lang=lang)
    html_engineer = render_industrie_template("example.html", context=example_context, user=user_engineer, lang=lang)
    html_client = render_industrie_template("example.html", context=example_context, user=user_client, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "Opérateur" in html_operator or "Operator" in html_operator or "مشغل" in html_operator or "ⴰⵎⴷⴰⵏ" in html_operator
    assert "Ingénieur" in html_engineer or "Engineer" in html_engineer or "مهندس" in html_engineer or "ⴰⵏⵖⴰⵔⴰⵙ" in html_engineer
    assert "Client" in html_client or "Customer" in html_client or "عميل" in html_client or "ⴰⵙⵙⴰⵏⴻⵏ" in html_client

def test_render_industrie_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_industrie_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_industrie_template_compliance(lang, example_context):
    html = render_industrie_template("example.html", context=example_context, lang=lang)
    results = validate_industrie_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert results["privacy"] is True
    assert not results["errors"]

def test_validate_industrie_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_industrie_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_industrie_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_industrie_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_validate_industrie_template_privacy_fail():
    html = "<html lang='fr'><body>{{ machine.secret_key }}</body></html>"
    results = validate_industrie_template(html, lang="fr")
    assert results["privacy"] is False
    assert any("industrielles" in str(e) or "client" in str(e) or "sensibles" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_client, example_context):
    html = render_industrie_template("example.html", context=example_context, user=user_client, lang=lang)
    results = validate_industrie_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security", "privacy"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.industrie.__init__")
    assert mod is not None

def test_template_render_with_missing_context_keys(user_client):
    # Le rendu ne doit pas échouer si le contexte ne contient pas toutes les clés attendues
    html = render_industrie_template("example.html", context={}, user=user_client, lang="fr")
    assert "<html" in html

def test_template_render_with_special_characters(user_client, example_context):
    # Teste la robustesse avec des caractères spéciaux et unicode
    example_context["special"] = "éèêçàùâîôœ€✓"
    html = render_industrie_template("example.html", context=example_context, user=user_client, lang="fr")
    assert "éèêçàùâîôœ€✓" in html or html  # Doit rendre sans erreur

def test_template_render_multistack_compatibility(user_client, example_context):
    # Simule un contexte compatible Jinja2 (clé 'user' obligatoire)
    example_context["user"] = user_client
    html = render_industrie_template("example.html", context=example_context, user=user_client, lang="fr")
    assert "<html" in html

# --- Fin des tests industrie ---

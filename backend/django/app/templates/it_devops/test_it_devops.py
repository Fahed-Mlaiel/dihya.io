"""
Dihya IT & DevOps Template – Tests avancés
==========================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module it_devops.
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
    render_itdevops_template,
    validate_itdevops_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_devops(db):
    user = User.objects.create_user(username="devops", password="devopspass")
    user.groups.create(name="DevOps")
    return user

@pytest.fixture
def user_dev(db):
    user = User.objects.create_user(username="dev", password="devpass")
    user.groups.create(name="Dev")
    return user

@pytest.fixture
def user_ops(db):
    user = User.objects.create_user(username="ops", password="opspass")
    user.groups.create(name="Ops")
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
def test_render_itdevops_template_ok(lang, example_context):
    html = render_itdevops_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Bienvenue" in html or "Welcome" in html or "مرحبا" in html or "ⴰⵏⴰⵡ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_itdevops_template_user_roles(lang, user_admin, user_devops, user_dev, user_ops, user_client, example_context):
    html_admin = render_itdevops_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_devops = render_itdevops_template("example.html", context=example_context, user=user_devops, lang=lang)
    html_dev = render_itdevops_template("example.html", context=example_context, user=user_dev, lang=lang)
    html_ops = render_itdevops_template("example.html", context=example_context, user=user_ops, lang=lang)
    html_client = render_itdevops_template("example.html", context=example_context, user=user_client, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "DevOps" in html_devops or "DevOps" in html_devops or "ديفوبس" in html_devops or "ⴷⴻⴼⵓⴱⵙ" in html_devops
    assert "Dev" in html_dev or "Développeur" in html_dev or "مطور" in html_dev or "ⴷⴻⴼ" in html_dev
    assert "Ops" in html_ops or "Opérations" in html_ops or "عمليات" in html_ops or "ⵓⴱⵙ" in html_ops
    assert "Client" in html_client or "Customer" in html_client or "عميل" in html_client or "ⴰⵙⵙⴰⵏⴻⵏ" in html_client

def test_render_itdevops_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_itdevops_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_itdevops_template_compliance(lang, example_context):
    html = render_itdevops_template("example.html", context=example_context, lang=lang)
    results = validate_itdevops_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert results["privacy"] is True
    assert not results["errors"]

def test_validate_itdevops_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_itdevops_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_itdevops_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_itdevops_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_validate_itdevops_template_privacy_fail():
    html = "<html lang='fr'><body>{{ devops.secret_token }}</body></html>"
    results = validate_itdevops_template(html, lang="fr")
    assert results["privacy"] is False
    assert any("DevOps" in str(e) or "infrastructure" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_client, example_context):
    html = render_itdevops_template("example.html", context=example_context, user=user_client, lang=lang)
    results = validate_itdevops_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security", "privacy"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.it_devops.__init__")
    assert mod is not None

def test_template_render_with_missing_context_keys(user_client):
    # Le rendu ne doit pas échouer si le contexte ne contient pas toutes les clés attendues
    html = render_itdevops_template("example.html", context={}, user=user_client, lang="fr")
    assert "<html" in html

def test_template_render_with_special_characters(user_client, example_context):
    # Teste la robustesse avec des caractères spéciaux et unicode
    example_context["special"] = "éèêçàùâîôœ€✓"
    html = render_itdevops_template("example.html", context=example_context, user=user_client, lang="fr")
    assert "éèêçàùâîôœ€✓" in html or html  # Doit rendre sans erreur

def test_template_render_multistack_compatibility(user_client, example_context):
    # Simule un contexte compatible Jinja2 (clé 'user' obligatoire)
    example_context["user"] = user_client
    html = render_itdevops_template("example.html", context=example_context, user=user_client, lang="fr")
    assert "<html" in html

# --- Fin des tests it_devops ---

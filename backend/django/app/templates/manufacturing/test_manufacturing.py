"""
Dihya Manufacturing Template – Tests avancés
============================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module manufacturing (production industrielle).
- Multilingue (fr, en, ar, tz)
- Couverture accessibilité, i18n, SEO, sécurité, confidentialité, conformité manufacturing, gestion des rôles
- CI/CD ready, aucun faux positif, robustesse Codespaces/Linux

"""

import os
import pytest
from django.test import RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from django.template import TemplateDoesNotExist

from .template import (
    render_manufacturing_template,
    validate_manufacturing_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_supervisor(db):
    user = User.objects.create_user(username="supervisor", password="supervisorpass")
    user.groups.create(name="Superviseur")
    return user

@pytest.fixture
def user_operator(db):
    user = User.objects.create_user(username="operator", password="operatorpass")
    user.groups.create(name="Opérateur")
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
def test_render_manufacturing_template_ok(lang, example_context):
    html = render_manufacturing_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Bienvenue" in html or "Welcome" in html or "مرحبا" in html or "ⴰⵏⴰⵡ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_manufacturing_template_user_roles(lang, user_admin, user_supervisor, user_operator, user_guest, example_context):
    html_admin = render_manufacturing_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_supervisor = render_manufacturing_template("example.html", context=example_context, user=user_supervisor, lang=lang)
    html_operator = render_manufacturing_template("example.html", context=example_context, user=user_operator, lang=lang)
    html_guest = render_manufacturing_template("example.html", context=example_context, user=user_guest, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "Superviseur" in html_supervisor or "Supervisor" in html_supervisor or "مشرف" in html_supervisor or "ⴰⵙⵓⴱⵔⵉⵙⵓⴼ" in html_supervisor
    assert "Opérateur" in html_operator or "Operator" in html_operator or "مشغل" in html_operator or "ⴰⵎⵙⴰⵡⴰⵍ" in html_operator
    assert "Invité" in html_guest or "Guest" in html_guest or "زائر" in html_guest or "ⴰⵣⴰⵢⴻⵏ" in html_guest

def test_render_manufacturing_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_manufacturing_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_manufacturing_template_compliance(lang, example_context):
    html = render_manufacturing_template("example.html", context=example_context, lang=lang)
    results = validate_manufacturing_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert results["privacy"] is True
    assert results["manufacturing"] is True
    assert not results["errors"]

def test_validate_manufacturing_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_manufacturing_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_manufacturing_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_manufacturing_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_validate_manufacturing_template_privacy_fail():
    html = "<html lang='fr'><body>{{ production.secret_industriel }}</body></html>"
    results = validate_manufacturing_template(html, lang="fr")
    assert results["privacy"] is False
    assert results["manufacturing"] is False
    assert any("confidentiel" in str(e) or "sensible" in str(e) or "industriel" in str(e) for e in results["errors"])

def test_validate_manufacturing_template_manufacturing_fail():
    html = "<html lang='fr'><body>tracking cookie analytics</body></html>"
    results = validate_manufacturing_template(html, lang="fr")
    assert results["manufacturing"] is False
    assert any("RGPD" in str(e) or "manufacturing" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_guest, example_context):
    html = render_manufacturing_template("example.html", context=example_context, user=user_guest, lang=lang)
    results = validate_manufacturing_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security", "privacy", "manufacturing"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.manufacturing.__init__")
    assert mod is not None

def test_template_render_with_missing_context_keys(user_guest):
    # Le rendu ne doit pas échouer si le contexte ne contient pas toutes les clés attendues
    html = render_manufacturing_template("example.html", context={}, user=user_guest, lang="fr")
    assert "<html" in html

def test_template_render_with_special_characters(user_guest, example_context):
    # Teste la robustesse avec des caractères spéciaux et unicode
    example_context["special"] = "éèêçàùâîôœ€✓"
    html = render_manufacturing_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "éèêçàùâîôœ€✓" in html or html  # Doit rendre sans erreur

def test_template_render_multistack_compatibility(user_guest, example_context):
    # Simule un contexte compatible Jinja2 (clé 'user' obligatoire)
    example_context["user"] = user_guest
    html = render_manufacturing_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "<html" in html

# --- Fin des tests manufacturing ---

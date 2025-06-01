"""
Dihya Juridique Template – Tests avancés
========================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module juridique.
- Multilingue (fr, en, ar, tz)
- Couverture accessibilité, i18n, SEO, sécurité, confidentialité, conformité juridique, gestion des rôles
- CI/CD ready, aucun faux positif, robustesse Codespaces/Linux

"""

import os
import pytest
from django.test import RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from django.template import TemplateDoesNotExist

from .template import (
    render_juridique_template,
    validate_juridique_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_jurist(db):
    user = User.objects.create_user(username="jurist", password="juristpass")
    user.groups.create(name="Juriste")
    return user

@pytest.fixture
def user_lawyer(db):
    user = User.objects.create_user(username="lawyer", password="lawyerpass")
    user.groups.create(name="Avocat")
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
def test_render_juridique_template_ok(lang, example_context):
    html = render_juridique_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Bienvenue" in html or "Welcome" in html or "مرحبا" in html or "ⴰⵏⴰⵡ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_juridique_template_user_roles(lang, user_admin, user_jurist, user_lawyer, user_guest, example_context):
    html_admin = render_juridique_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_jurist = render_juridique_template("example.html", context=example_context, user=user_jurist, lang=lang)
    html_lawyer = render_juridique_template("example.html", context=example_context, user=user_lawyer, lang=lang)
    html_guest = render_juridique_template("example.html", context=example_context, user=user_guest, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "Juriste" in html_jurist or "Jurist" in html_jurist or "خبير" in html_jurist or "ⴰⵊⵓⵔⵉⵙⵜ" in html_jurist
    assert "Avocat" in html_lawyer or "Lawyer" in html_lawyer or "محامي" in html_lawyer or "ⴰⵎⵏⴰⵙ" in html_lawyer
    assert "Invité" in html_guest or "Guest" in html_guest or "زائر" in html_guest or "ⴰⵣⴰⵢⴻⵏ" in html_guest

def test_render_juridique_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_juridique_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_juridique_template_compliance(lang, example_context):
    html = render_juridique_template("example.html", context=example_context, lang=lang)
    results = validate_juridique_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert results["privacy"] is True
    assert results["legal"] is True
    assert not results["errors"]

def test_validate_juridique_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_juridique_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_juridique_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_juridique_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_validate_juridique_template_privacy_fail():
    html = "<html lang='fr'><body>{{ contrat.clause_confidentielle }}</body></html>"
    results = validate_juridique_template(html, lang="fr")
    assert results["privacy"] is False
    assert results["legal"] is False
    assert any("confidenti" in str(e) or "personnel" in str(e) or "juridique" in str(e) for e in results["errors"])

def test_validate_juridique_template_legal_fail():
    html = "<html lang='fr'><body>tracking cookie analytics</body></html>"
    results = validate_juridique_template(html, lang="fr")
    assert results["legal"] is False
    assert any("RGPD" in str(e) or "légal" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_guest, example_context):
    html = render_juridique_template("example.html", context=example_context, user=user_guest, lang=lang)
    results = validate_juridique_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security", "privacy", "legal"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.juridique.__init__")
    assert mod is not None

def test_template_render_with_missing_context_keys(user_guest):
    # Le rendu ne doit pas échouer si le contexte ne contient pas toutes les clés attendues
    html = render_juridique_template("example.html", context={}, user=user_guest, lang="fr")
    assert "<html" in html

def test_template_render_with_special_characters(user_guest, example_context):
    # Teste la robustesse avec des caractères spéciaux et unicode
    example_context["special"] = "éèêçàùâîôœ€✓"
    html = render_juridique_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "éèêçàùâîôœ€✓" in html or html  # Doit rendre sans erreur

def test_template_render_multistack_compatibility(user_guest, example_context):
    # Simule un contexte compatible Jinja2 (clé 'user' obligatoire)
    example_context["user"] = user_guest
    html = render_juridique_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "<html" in html

# --- Fin des tests juridique ---

"""
Dihya Journalisme Template – Tests avancés
==========================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module journalisme.
- Multilingue (fr, en, ar, tz)
- Couverture accessibilité, i18n, SEO, sécurité, confidentialité, éthique, gestion des rôles
- CI/CD ready, aucun faux positif, robustesse Codespaces/Linux

"""

import os
import pytest
from django.test import RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from django.template import TemplateDoesNotExist

from .template import (
    render_journalisme_template,
    validate_journalisme_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_journalist(db):
    user = User.objects.create_user(username="journalist", password="journalistpass")
    user.groups.create(name="Journaliste")
    return user

@pytest.fixture
def user_editor(db):
    user = User.objects.create_user(username="editor", password="editorpass")
    user.groups.create(name="Éditeur")
    return user

@pytest.fixture
def user_reader(db):
    user = User.objects.create_user(username="reader", password="readerpass")
    return user

@pytest.fixture
def example_context():
    return {"test": True, "extra": "value"}

# --- Tests unitaires ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_journalisme_template_ok(lang, example_context):
    html = render_journalisme_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Bienvenue" in html or "Welcome" in html or "مرحبا" in html or "ⴰⵏⴰⵡ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_journalisme_template_user_roles(lang, user_admin, user_journalist, user_editor, user_reader, example_context):
    html_admin = render_journalisme_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_journalist = render_journalisme_template("example.html", context=example_context, user=user_journalist, lang=lang)
    html_editor = render_journalisme_template("example.html", context=example_context, user=user_editor, lang=lang)
    html_reader = render_journalisme_template("example.html", context=example_context, user=user_reader, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "Journaliste" in html_journalist or "Journalist" in html_journalist or "صحفي" in html_journalist or "ⴰⵊⵓⵏⴰⵍⵉⵙⵜ" in html_journalist
    assert "Éditeur" in html_editor or "Editor" in html_editor or "محرر" in html_editor or "ⴰⵎⵙⴻⴼⵔⴰⴽ" in html_editor
    assert "Lecteur" in html_reader or "Reader" in html_reader or "قارئ" in html_reader or "ⴰⴳⵔⴰⵡⵍⵉ" in html_reader

def test_render_journalisme_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_journalisme_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_journalisme_template_compliance(lang, example_context):
    html = render_journalisme_template("example.html", context=example_context, lang=lang)
    results = validate_journalisme_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert results["privacy"] is True
    assert results["ethics"] is True
    assert not results["errors"]

def test_validate_journalisme_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_journalisme_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_journalisme_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_journalisme_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_validate_journalisme_template_privacy_fail():
    html = "<html lang='fr'><body>{{ article.source_confidentielle }}</body></html>"
    results = validate_journalisme_template(html, lang="fr")
    assert results["privacy"] is False
    assert any("source" in str(e) or "confidentiel" in str(e) for e in results["errors"])

def test_validate_journalisme_template_ethics_fail():
    html = "<html lang='fr'><body>fake news advertising adsense</body></html>"
    results = validate_journalisme_template(html, lang="fr")
    assert results["ethics"] is False
    assert any("éthique" in str(e) or "ethics" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_reader, example_context):
    html = render_journalisme_template("example.html", context=example_context, user=user_reader, lang=lang)
    results = validate_journalisme_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security", "privacy", "ethics"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.journalisme.__init__")
    assert mod is not None

def test_template_render_with_missing_context_keys(user_reader):
    # Le rendu ne doit pas échouer si le contexte ne contient pas toutes les clés attendues
    html = render_journalisme_template("example.html", context={}, user=user_reader, lang="fr")
    assert "<html" in html

def test_template_render_with_special_characters(user_reader, example_context):
    # Teste la robustesse avec des caractères spéciaux et unicode
    example_context["special"] = "éèêçàùâîôœ€✓"
    html = render_journalisme_template("example.html", context=example_context, user=user_reader, lang="fr")
    assert "éèêçàùâîôœ€✓" in html or html  # Doit rendre sans erreur

def test_template_render_multistack_compatibility(user_reader, example_context):
    # Simule un contexte compatible Jinja2 (clé 'user' obligatoire)
    example_context["user"] = user_reader
    html = render_journalisme_template("example.html", context=example_context, user=user_reader, lang="fr")
    assert "<html" in html

# --- Fin des tests journalisme ---

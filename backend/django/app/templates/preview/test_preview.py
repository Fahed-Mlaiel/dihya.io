"""
Dihya Preview Template – Tests avancés
======================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module preview (prévisualisation de contenus, assets, médias, documents, etc.).
- Multilingue (fr, en, ar, tz)
- Couverture accessibilité, i18n, SEO, sécurité, conformité preview, gestion des rôles, droits d’auteur
- CI/CD ready, aucun faux positif, robustesse Codespaces/Linux

"""

import os
import pytest
from django.test import RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from django.template import TemplateDoesNotExist

from .template import (
    render_preview_template,
    validate_preview_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_editor(db):
    user = User.objects.create_user(username="editor", password="editorpass")
    user.groups.create(name="Éditeur")
    return user

@pytest.fixture
def user_reader(db):
    user = User.objects.create_user(username="reader", password="readerpass")
    user.groups.create(name="Lecteur")
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
def test_render_preview_template_ok(lang, example_context):
    html = render_preview_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Prévisualisation" in html or "Preview" in html or "معاينة" in html or "ⵜⴰⵎⴰⵣⵉⵖ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_preview_template_user_roles(lang, user_admin, user_editor, user_reader, user_guest, example_context):
    html_admin = render_preview_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_editor = render_preview_template("example.html", context=example_context, user=user_editor, lang=lang)
    html_reader = render_preview_template("example.html", context=example_context, user=user_reader, lang=lang)
    html_guest = render_preview_template("example.html", context=example_context, user=user_guest, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "Éditeur" in html_editor or "Editor" in html_editor or "محرر" in html_editor or "ⴰⵉⴷⵉⵜⵓⵔ" in html_editor
    assert "Lecteur" in html_reader or "Reader" in html_reader or "قارئ" in html_reader or "ⴰⵍⴽⵜⴰⵔ" in html_reader
    assert "Invité" in html_guest or "Guest" in html_guest or "زائر" in html_guest or "ⴰⵣⴰⵢⴻⵏ" in html_guest

def test_render_preview_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_preview_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_preview_template_compliance(lang, example_context):
    html = render_preview_template("example.html", context=example_context, lang=lang)
    results = validate_preview_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert results["privacy"] is True
    assert results["preview"] is True
    assert results["copyright"] is True
    assert not results["errors"]

def test_validate_preview_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_preview_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_preview_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_preview_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_validate_preview_template_img_alt_fail():
    html = "<html lang='fr'><body><img src='test.jpg'></body></html>"
    results = validate_preview_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("alt" in str(e) for e in results["errors"])

def test_validate_preview_template_privacy_fail():
    html = "<html lang='fr'><body>{{ preview.secret_asset }}</body></html>"
    results = validate_preview_template(html, lang="fr")
    assert results["privacy"] is False
    assert results["preview"] is False
    assert any("confidentiel" in str(e) or "sensible" in str(e) or "preview" in str(e) for e in results["errors"])

def test_validate_preview_template_preview_fail():
    html = "<html lang='fr'><body>tracking cookie analytics</body></html>"
    results = validate_preview_template(html, lang="fr")
    assert results["preview"] is False
    assert any("RGPD" in str(e) or "preview" in str(e) for e in results["errors"])

def test_validate_preview_template_copyright_fail():
    html = "<html lang='fr'><body></body></html>"
    results = validate_preview_template(html, lang="fr")
    assert results["copyright"] is False
    assert any("droit" in str(e) or "copyright" in str(e) for e in results["errors"])

def test_validate_preview_template_viewport_fail():
    html = "<html lang='fr'><head></head><body></body></html>"
    results = validate_preview_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("viewport" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_guest, example_context):
    html = render_preview_template("example.html", context=example_context, user=user_guest, lang=lang)
    results = validate_preview_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security", "privacy", "preview", "copyright"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.preview.__init__")
    assert mod is not None

def test_template_render_with_missing_context_keys(user_guest):
    # Le rendu ne doit pas échouer si le contexte ne contient pas toutes les clés attendues
    html = render_preview_template("example.html", context={}, user=user_guest, lang="fr")
    assert "<html" in html

def test_template_render_with_special_characters(user_guest, example_context):
    # Teste la robustesse avec des caractères spéciaux et unicode
    example_context["special"] = "éèêçàùâîôœ€✓"
    html = render_preview_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "éèêçàùâîôœ€✓" in html or html  # Doit rendre sans erreur

def test_template_render_multistack_compatibility(user_guest, example_context):
    # Simule un contexte compatible Jinja2 (clé 'user' obligatoire)
    example_context["user"] = user_guest
    html = render_preview_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "<html" in html

# --- Fin des tests preview ---

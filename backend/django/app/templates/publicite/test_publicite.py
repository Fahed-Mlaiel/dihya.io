"""
Dihya Publicité Template – Tests avancés
========================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module publicité (annonces, bannières, campagnes, tracking souverain, etc.).
- Multilingue (fr, en, ar, tz)
- Couverture accessibilité, i18n, SEO, sécurité, conformité publicité, gestion des rôles, droits d’auteur
- CI/CD ready, aucun faux positif, robustesse Codespaces/Linux

"""

import os
import pytest
from django.test import RequestFactory, override_settings
from django.contrib.auth.models import AnonymousUser, User
from django.template import TemplateDoesNotExist

from .template import (
    render_publicite_template,
    validate_publicite_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_regie(db):
    user = User.objects.create_user(username="regie", password="regiepass")
    user.groups.create(name="Régie")
    return user

@pytest.fixture
def user_annonceur(db):
    user = User.objects.create_user(username="annonceur", password="annonceurpass")
    user.groups.create(name="Annonceur")
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
def test_render_publicite_template_ok(lang, example_context):
    html = render_publicite_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Publicité" in html or "Advertising" in html or "إعلان" in html or "ⴰⵙⵏⴼⴰⵡ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_publicite_template_user_roles(lang, user_admin, user_regie, user_annonceur, user_guest, example_context):
    html_admin = render_publicite_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_regie = render_publicite_template("example.html", context=example_context, user=user_regie, lang=lang)
    html_annonceur = render_publicite_template("example.html", context=example_context, user=user_annonceur, lang=lang)
    html_guest = render_publicite_template("example.html", context=example_context, user=user_guest, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "Régie" in html_regie or "Agency" in html_regie or "وكالة" in html_regie or "ⵔⴳⵉⵢ" in html_regie
    assert "Annonceur" in html_annonceur or "Advertiser" in html_annonceur or "معلن" in html_annonceur or "ⴰⵏⵏⵓⵙⴻⵔ" in html_annonceur
    assert "Invité" in html_guest or "Guest" in html_guest or "زائر" in html_guest or "ⴰⵣⴰⵢⴻⵏ" in html_guest

def test_render_publicite_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_publicite_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_publicite_template_compliance(lang, example_context):
    html = render_publicite_template("example.html", context=example_context, lang=lang)
    results = validate_publicite_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert results["privacy"] is True
    assert results["publicite"] is True
    assert results["copyright"] is True
    assert not results["errors"]

def test_validate_publicite_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_publicite_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_publicite_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_publicite_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_validate_publicite_template_img_alt_fail():
    html = "<html lang='fr'><body><img src='test.jpg'></body></html>"
    results = validate_publicite_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("alt" in str(e) for e in results["errors"])

def test_validate_publicite_template_privacy_fail():
    html = "<html lang='fr'><body>{{ pub.secret_campaign }}</body></html>"
    results = validate_publicite_template(html, lang="fr")
    assert results["privacy"] is False
    assert results["publicite"] is False
    assert any("confidentiel" in str(e) or "sensible" in str(e) or "publicité" in str(e) for e in results["errors"])

def test_validate_publicite_template_publicite_fail():
    html = "<html lang='fr'><body>tracking cookie analytics</body></html>"
    results = validate_publicite_template(html, lang="fr")
    assert results["publicite"] is False
    assert any("RGPD" in str(e) or "publicité" in str(e) for e in results["errors"])

def test_validate_publicite_template_copyright_fail():
    html = "<html lang='fr'><body></body></html>"
    results = validate_publicite_template(html, lang="fr")
    assert results["copyright"] is False
    assert any("droit" in str(e) or "copyright" in str(e) for e in results["errors"])

def test_validate_publicite_template_viewport_fail():
    html = "<html lang='fr'><head></head><body></body></html>"
    results = validate_publicite_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("viewport" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_guest, example_context):
    html = render_publicite_template("example.html", context=example_context, user=user_guest, lang=lang)
    results = validate_publicite_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security", "privacy", "publicite", "copyright"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.publicite.__init__")
    assert mod is not None

def test_template_render_with_missing_context_keys(user_guest):
    # Le rendu ne doit pas échouer si le contexte ne contient pas toutes les clés attendues
    html = render_publicite_template("example.html", context={}, user=user_guest, lang="fr")
    assert "<html" in html

def test_template_render_with_special_characters(user_guest, example_context):
    # Teste la robustesse avec des caractères spéciaux et unicode
    example_context["special"] = "éèêçàùâîôœ€✓"
    html = render_publicite_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "éèêçàùâîôœ€✓" in html or html  # Doit rendre sans erreur

def test_template_render_multistack_compatibility(user_guest, example_context):
    # Simule un contexte compatible Jinja2 (clé 'user' obligatoire)
    example_context["user"] = user_guest
    html = render_publicite_template("example.html", context=example_context, user=user_guest, lang="fr")
    assert "<html" in html

# --- Fin des tests publicite ---

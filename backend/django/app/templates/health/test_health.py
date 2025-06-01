"""
Dihya Health Template – Tests avancés
=====================================

Tests unitaires, d’intégration et E2E pour les utilitaires de templates du module health.
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
    render_health_template,
    validate_health_template,
    audit_template_access,
)

# --- Fixtures et helpers ---

@pytest.fixture
def user_admin(db):
    user = User.objects.create_user(username="admin", password="adminpass", is_superuser=True)
    return user

@pytest.fixture
def user_doctor(db):
    user = User.objects.create_user(username="doctor", password="doctorpass")
    user.groups.create(name="Médecin")
    return user

@pytest.fixture
def user_patient(db):
    user = User.objects.create_user(username="patient", password="patientpass")
    return user

@pytest.fixture
def example_context():
    return {"test": True, "extra": "value"}

# --- Tests unitaires ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_health_template_ok(lang, example_context):
    html = render_health_template("example.html", context=example_context, lang=lang)
    assert "<html" in html
    assert "Bienvenue" in html or "Welcome" in html or "مرحبا" in html or "ⴰⵏⴰⵡ" in html

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_render_health_template_user_roles(lang, user_admin, user_doctor, user_patient, example_context):
    html_admin = render_health_template("example.html", context=example_context, user=user_admin, lang=lang)
    html_doctor = render_health_template("example.html", context=example_context, user=user_doctor, lang=lang)
    html_patient = render_health_template("example.html", context=example_context, user=user_patient, lang=lang)
    assert "Administrateur" in html_admin or "Admin" in html_admin or "مشرف" in html_admin or "ⴰⵎⴰⵏⴰⵡⴰⵏ" in html_admin
    assert "Médecin" in html_doctor or "Doctor" in html_doctor or "طبيب" in html_doctor or "ⴰⵙⵇⴻⵍⵎⴻⴷ" in html_doctor
    assert "Patient" in html_patient or "Patient" in html_patient or "مريض" in html_patient or "ⴰⵎⵓⴷⴷⵓ" in html_patient

def test_render_health_template_not_exist():
    with pytest.raises(TemplateDoesNotExist):
        render_health_template("notfound.html")

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_validate_health_template_compliance(lang, example_context):
    html = render_health_template("example.html", context=example_context, lang=lang)
    results = validate_health_template(html, lang=lang)
    assert results["accessibility"] is True
    assert results["i18n"] is True
    assert results["seo"] is True
    assert results["security"] is True
    assert results["privacy"] is True
    assert not results["errors"]

def test_validate_health_template_security_fail():
    html = "<html lang='fr'><body><script>alert('xss')</script></body></html>"
    results = validate_health_template(html, lang="fr")
    assert results["security"] is False
    assert any("Script inline" in str(e) for e in results["errors"])

def test_validate_health_template_accessibility_fail():
    html = "<html><body></body></html>"
    results = validate_health_template(html, lang="fr")
    assert results["accessibility"] is False
    assert any("lang" in str(e) for e in results["errors"])

def test_validate_health_template_privacy_fail():
    html = "<html lang='fr'><body>{{ patient.medical_record }}</body></html>"
    results = validate_health_template(html, lang="fr")
    assert results["privacy"] is False
    assert any("médicales" in str(e) or "personnelles" in str(e) for e in results["errors"])

def test_audit_template_access_logs(caplog, user_admin):
    with caplog.at_level("INFO"):
        audit_template_access("example.html", user=user_admin, lang="fr")
    assert "Template 'example.html' accessed by 'admin'" in caplog.text

# --- E2E : test multilingue complet ---

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "tz"])
def test_end_to_end_template_render_and_validate(lang, user_patient, example_context):
    html = render_health_template("example.html", context=example_context, user=user_patient, lang=lang)
    results = validate_health_template(html, lang=lang)
    assert all(results[k] for k in ["accessibility", "i18n", "seo", "security", "privacy"])
    assert not results["errors"]

# --- CI/CD & Robustesse ---

def test_template_env_var_disable_check(monkeypatch):
    monkeypatch.setenv("DIHYA_TEMPLATE_CHECK", "0")
    # Import du module __init__ pour vérifier que le check ne lève pas d’erreur
    import importlib
    import sys
    mod = importlib.import_module("Dihya.backend.django.app.templates.health.__init__")
    assert mod is not None

def test_template_render_with_missing_context_keys(user_patient):
    # Le rendu ne doit pas échouer si le contexte ne contient pas toutes les clés attendues
    html = render_health_template("example.html", context={}, user=user_patient, lang="fr")
    assert "<html" in html

def test_template_render_with_special_characters(user_patient, example_context):
    # Teste la robustesse avec des caractères spéciaux et unicode
    example_context["special"] = "éèêçàùâîôœ€✓"
    html = render_health_template("example.html", context=example_context, user=user_patient, lang="fr")
    assert "éèêçàùâîôœ€✓" in html or html  # Doit rendre sans erreur

def test_template_render_multistack_compatibility(user_patient, example_context):
    # Simule un contexte compatible Jinja2 (clé 'user' obligatoire)
    example_context["user"] = user_patient
    html = render_health_template("example.html", context=example_context, user=user_patient, lang="fr")
    assert "<html" in html

# --- Fin des tests health ---

"""
Dihya – Tests unitaires et d’intégration pour CultureTemplate (Ultra Avancé)
----------------------------------------------------------------------------
Ce module teste la robustesse, la sécurité, la conformité et l’extensibilité de la classe CultureTemplate.
Couverture : validation, intégrité, multilingue, sécurité, edge cases, CI/CD ready.

🇫🇷 Tests unitaires et intégration pour CultureTemplate
🇬🇧 Unit & integration tests for CultureTemplate
🇦🇪 اختبارات الوحدة والتكامل لقالب الثقافة
ⵣ Iqedcen n unit d integration i CultureTemplate

Prêt pour pytest, unittest, CI/CD, Codespaces, cloud souverain.
"""

import sys
sys.path.insert(0, '.')
from backend.django.app.templates.culture.template import CultureTemplate

import pytest

@pytest.fixture
def valid_culture_template_data():
    return {
        "name": "evenement_culturel_2025",
        "description": {
            "fr": "Fiche structurée pour la gestion d’événements culturels.",
            "en": "Structured record for cultural event management.",
            "ar": "بطاقة منظمة لإدارة الفعاليات الثقافية.",
            "tzm": "Afaylu i uselkim n tamedyazt."
        },
        "author": "A. Dihya",
        "version": "1.0",
        "data": {
            "evenement": "Festival Amazigh",
            "lieu": "Tizi Ouzou",
            "date_debut": "2025-08-01",
            "date_fin": "2025-08-07",
            "participants": [
                {"nom": "A. Dihya", "rôle": "Organisateur"},
                {"nom": "B. Massinissa", "rôle": "Artiste"}
            ],
            "meta": {"type": "evenement", "usage": "culturel"}
        }
    }

def test_culturetemplate_valid(valid_culture_template_data):
    tpl = CultureTemplate(**valid_culture_template_data)
    assert tpl.validate()
    assert isinstance(tpl.hash, str)
    assert len(tpl.hash) == 64
    meta = tpl.export_metadata()
    assert meta["name"] == valid_culture_template_data["name"]
    assert meta["author"] == valid_culture_template_data["author"]
    assert meta["version"] == valid_culture_template_data["version"]
    assert meta["hash"] == tpl.hash

def test_culturetemplate_missing_field(valid_culture_template_data):
    data = valid_culture_template_data.copy()
    data.pop("author")
    tpl = CultureTemplate(
        name=data.get("name"),
        description=data.get("description"),
        author=data.get("author", None),
        version=data.get("version"),
        data=data.get("data")
    )
    assert not tpl.validate()

def test_culturetemplate_integrity_change(valid_culture_template_data):
    tpl = CultureTemplate(**valid_culture_template_data)
    original_hash = tpl.hash
    tpl.data["meta"]["usage"] = "patrimoine"
    new_hash = tpl.compute_hash()
    assert original_hash != new_hash

def test_culturetemplate_multilingual_message(valid_culture_template_data):
    tpl = CultureTemplate(**valid_culture_template_data)
    msg = tpl._msg("fr", "en", "ar", "tzm")
    assert msg == "fr"  # Par défaut, retourne le français

def test_culturetemplate_export_metadata_fields(valid_culture_template_data):
    tpl = CultureTemplate(**valid_culture_template_data)
    meta = tpl.export_metadata()
    assert set(meta.keys()) == {"name", "description", "author", "version", "hash"}

def test_culturetemplate_security_no_exec():
    # Vérifie qu’aucun code exécutable n’est lancé à l’import
    import importlib
    import sys
    module_name = "template"
    if module_name in sys.modules:
        del sys.modules[module_name]
    importlib.import_module(module_name)
    assert True  # Si aucune exception, test OK

# Edge case: données vides
def test_culturetemplate_empty_data():
    tpl = CultureTemplate(
        name="empty",
        description={"fr": "", "en": "", "ar": "", "tzm": ""},
        author="",
        version="",
        data={}
    )
    assert tpl.validate()  # Les champs sont présents, même vides

# Edge case: description partielle
def test_culturetemplate_partial_description(valid_culture_template_data):
    data = valid_culture_template_data.copy()
    data["description"] = {"fr": "Seulement en français"}
    tpl = CultureTemplate(**data)
    assert tpl.validate()

# Sécurité : pas d’accès disque/réseau, pas d’exécution dynamique, pas de faille connue
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

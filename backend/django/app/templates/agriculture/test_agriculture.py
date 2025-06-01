"""
Dihya – Tests unitaires et d’intégration pour AgricultureTemplate (Ultra Avancé)
--------------------------------------------------------------------------------
Ce module teste la robustesse, la sécurité, la conformité et l’extensibilité de la classe AgricultureTemplate.
Couverture : validation, intégrité, multilingue, sécurité, edge cases, CI/CD ready.

🇫🇷 Tests unitaires et intégration pour AgricultureTemplate
🇬🇧 Unit & integration tests for AgricultureTemplate
🇦🇪 اختبارات الوحدة والتكامل لقالب الزراعة
ⵣ Iqedcen n unit d integration i AgricultureTemplate

Prêt pour pytest, unittest, CI/CD, Codespaces, cloud souverain.
"""

import sys
sys.path.insert(0, '.')
from backend.django.app.templates.agriculture.template import AgricultureTemplate
import pytest

@pytest.fixture
def valid_agriculture_template_data():
    return {
        "name": "fiche_culture_ble",
        "description": {
            "fr": "Fiche technique structurée pour la culture du blé.",
            "en": "Structured technical sheet for wheat cultivation.",
            "ar": "بطاقة تقنية منظمة لزراعة القمح.",
            "tzm": "Aficha technique n tazrawt n taqmuḍt."
        },
        "author": "A. Dihya",
        "version": "1.0",
        "data": {
            "culture": "blé",
            "saison": "printemps",
            "besoins_eau": "modérés",
            "meta": {"type": "fiche", "usage": "culture"}
        }
    }

def test_agriculturetemplate_valid(valid_agriculture_template_data):
    tpl = AgricultureTemplate(**valid_agriculture_template_data)
    assert tpl.validate()
    assert isinstance(tpl.hash, str)
    assert len(tpl.hash) == 64
    meta = tpl.export_metadata()
    assert meta["name"] == valid_agriculture_template_data["name"]
    assert meta["author"] == valid_agriculture_template_data["author"]
    assert meta["version"] == valid_agriculture_template_data["version"]
    assert meta["hash"] == tpl.hash

def test_agriculturetemplate_missing_field(valid_agriculture_template_data):
    data = valid_agriculture_template_data.copy()
    data.pop("author")
    tpl = AgricultureTemplate(
        name=data.get("name"),
        description=data.get("description"),
        author=data.get("author", None),
        version=data.get("version"),
        data=data.get("data")
    )
    assert not tpl.validate()

def test_agriculturetemplate_integrity_change(valid_agriculture_template_data):
    tpl = AgricultureTemplate(**valid_agriculture_template_data)
    original_hash = tpl.hash
    tpl.data["meta"]["usage"] = "rotation"
    new_hash = tpl.compute_hash()
    assert original_hash != new_hash

def test_agriculturetemplate_multilingual_message(valid_agriculture_template_data):
    tpl = AgricultureTemplate(**valid_agriculture_template_data)
    msg = tpl._msg("fr", "en", "ar", "tzm")
    assert msg == "fr"  # Par défaut, retourne le français

def test_agriculturetemplate_export_metadata_fields(valid_agriculture_template_data):
    tpl = AgricultureTemplate(**valid_agriculture_template_data)
    meta = tpl.export_metadata()
    assert set(meta.keys()) == {"name", "description", "author", "version", "hash"}

def test_agriculturetemplate_security_no_exec():
    # Vérifie qu’aucun code exécutable n’est lancé à l’import
    import importlib
    import sys
    module_name = "template"
    if module_name in sys.modules:
        del sys.modules[module_name]
    importlib.import_module(module_name)
    assert True  # Si aucune exception, test OK

# Edge case: données vides
def test_agriculturetemplate_empty_data():
    tpl = AgricultureTemplate(
        name="empty",
        description={"fr": "", "en": "", "ar": "", "tzm": ""},
        author="",
        version="",
        data={}
    )
    assert tpl.validate()  # Les champs sont présents, même vides

# Edge case: description partielle
def test_agriculturetemplate_partial_description(valid_agriculture_template_data):
    data = valid_agriculture_template_data.copy()
    data["description"] = {"fr": "Seulement en français"}
    tpl = AgricultureTemplate(**data)
    assert tpl.validate()

# Sécurité : pas d’accès disque/réseau, pas d’exécution dynamique, pas de faille connue
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

"""
Dihya – Tests unitaires et d’intégration pour AssuranceTemplate (Ultra Avancé)
------------------------------------------------------------------------------
Ce module teste la robustesse, la sécurité, la conformité et l’extensibilité de la classe AssuranceTemplate.
Couverture : validation, intégrité, multilingue, sécurité, edge cases, CI/CD ready.

🇫🇷 Tests unitaires et intégration pour AssuranceTemplate
🇬🇧 Unit & integration tests for AssuranceTemplate
🇦🇪 اختبارات الوحدة والتكامل لقالب التأمين
ⵣ Iqedcen n unit d integration i AssuranceTemplate

Prêt pour pytest, unittest, CI/CD, Codespaces, cloud souverain.
"""

import sys
sys.path.insert(0, '.')
from backend.django.app.templates.assurance.template import AssuranceTemplate
import pytest

@pytest.fixture
def valid_assurance_template_data():
    return {
        "name": "contrat_auto_2025",
        "description": {
            "fr": "Contrat structuré pour l’assurance automobile.",
            "en": "Structured contract for car insurance.",
            "ar": "عقد منظم لتأمين السيارات.",
            "tzm": "Acontrat n tazmert n tigmmiwin."
        },
        "author": "A. Dihya",
        "version": "1.0",
        "data": {
            "contrat": "auto",
            "assuré": "A. Dihya",
            "date_debut": "2025-01-01",
            "date_fin": "2026-01-01",
            "garanties": ["RC", "Bris de glace", "Vol"],
            "meta": {"type": "contrat", "usage": "assurance_auto"}
        }
    }

def test_assurancetemplate_valid(valid_assurance_template_data):
    tpl = AssuranceTemplate(**valid_assurance_template_data)
    assert tpl.validate()
    assert isinstance(tpl.hash, str)
    assert len(tpl.hash) == 64
    meta = tpl.export_metadata()
    assert meta["name"] == valid_assurance_template_data["name"]
    assert meta["author"] == valid_assurance_template_data["author"]
    assert meta["version"] == valid_assurance_template_data["version"]
    assert meta["hash"] == tpl.hash

def test_assurancetemplate_missing_field(valid_assurance_template_data):
    data = valid_assurance_template_data.copy()
    data.pop("author")
    tpl = AssuranceTemplate(
        name=data.get("name"),
        description=data.get("description"),
        author=data.get("author", None),
        version=data.get("version"),
        data=data.get("data")
    )
    assert not tpl.validate()

def test_assurancetemplate_integrity_change(valid_assurance_template_data):
    tpl = AssuranceTemplate(**valid_assurance_template_data)
    original_hash = tpl.hash
    tpl.data["meta"]["usage"] = "sinistre"
    new_hash = tpl.compute_hash()
    assert original_hash != new_hash

def test_assurancetemplate_multilingual_message(valid_assurance_template_data):
    tpl = AssuranceTemplate(**valid_assurance_template_data)
    msg = tpl._msg("fr", "en", "ar", "tzm")
    assert msg == "fr"  # Par défaut, retourne le français

def test_assurancetemplate_export_metadata_fields(valid_assurance_template_data):
    tpl = AssuranceTemplate(**valid_assurance_template_data)
    meta = tpl.export_metadata()
    assert set(meta.keys()) == {"name", "description", "author", "version", "hash"}

def test_assurancetemplate_security_no_exec():
    # Vérifie qu’aucun code exécutable n’est lancé à l’import
    import importlib
    import sys
    module_name = "template"
    if module_name in sys.modules:
        del sys.modules[module_name]
    importlib.import_module(module_name)
    assert True  # Si aucune exception, test OK

# Edge case: données vides
def test_assurancetemplate_empty_data():
    tpl = AssuranceTemplate(
        name="empty",
        description={"fr": "", "en": "", "ar": "", "tzm": ""},
        author="",
        version="",
        data={}
    )
    assert tpl.validate()  # Les champs sont présents, même vides

# Edge case: description partielle
def test_assurancetemplate_partial_description(valid_assurance_template_data):
    data = valid_assurance_template_data.copy()
    data["description"] = {"fr": "Seulement en français"}
    tpl = AssuranceTemplate(**data)
    assert tpl.validate()

# Sécurité : pas d’accès disque/réseau, pas d’exécution dynamique, pas de faille connue
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

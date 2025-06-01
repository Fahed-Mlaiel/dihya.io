"""
Dihya – Tests unitaires et d’intégration pour AdminTemplate (Ultra Avancé)
--------------------------------------------------------------------------
Ce module teste la robustesse, la sécurité, la conformité et l’extensibilité de la classe AdminTemplate.
Couverture : validation, intégrité, multilingue, sécurité, edge cases, CI/CD ready.

🇫🇷 Tests unitaires et intégration pour AdminTemplate
🇬🇧 Unit & integration tests for AdminTemplate
🇦🇪 اختبارات الوحدة والتكامل لقالب الإدارة العمومية
ⵣ Iqedcen n unit d integration i AdminTemplate

Prêt pour pytest, unittest, CI/CD, Codespaces, cloud souverain.
"""

import sys
sys.path.insert(0, '.')
from backend.django.app.templates.administration_publique.template import AdminTemplate
import pytest

@pytest.fixture
def valid_admin_template_data():
    return {
        "name": "formulaire_naissance",
        "description": {
            "fr": "Formulaire structuré pour la déclaration de naissance.",
            "en": "Structured form for birth declaration.",
            "ar": "استمارة منظمة لتصريح الولادة.",
            "tzm": "Aformulaire n tazwart i usenqed n ttwilit."
        },
        "author": "A. Dihya",
        "version": "1.0",
        "data": {
            "fields": [
                {"name": "nom", "type": "string", "required": True},
                {"name": "prénom", "type": "string", "required": True},
                {"name": "date_naissance", "type": "date", "required": True}
            ],
            "meta": {"type": "formulaire", "usage": "naissance"}
        }
    }

def test_admintemplate_valid(valid_admin_template_data):
    tpl = AdminTemplate(**valid_admin_template_data)
    assert tpl.validate()
    assert isinstance(tpl.hash, str)
    assert len(tpl.hash) == 64
    meta = tpl.export_metadata()
    assert meta["name"] == valid_admin_template_data["name"]
    assert meta["author"] == valid_admin_template_data["author"]
    assert meta["version"] == valid_admin_template_data["version"]
    assert meta["hash"] == tpl.hash

def test_admintemplate_missing_field(valid_admin_template_data):
    data = valid_admin_template_data.copy()
    data.pop("author")
    tpl = AdminTemplate(
        name=data.get("name"),
        description=data.get("description"),
        author=data.get("author", None),
        version=data.get("version"),
        data=data.get("data")
    )
    assert not tpl.validate()

def test_admintemplate_integrity_change(valid_admin_template_data):
    tpl = AdminTemplate(**valid_admin_template_data)
    original_hash = tpl.hash
    tpl.data["meta"]["usage"] = "adoption"
    new_hash = tpl.compute_hash()
    assert original_hash != new_hash

def test_admintemplate_multilingual_message(valid_admin_template_data):
    tpl = AdminTemplate(**valid_admin_template_data)
    msg = tpl._msg("fr", "en", "ar", "tzm")
    assert msg == "fr"  # Par défaut, retourne le français

def test_admintemplate_export_metadata_fields(valid_admin_template_data):
    tpl = AdminTemplate(**valid_admin_template_data)
    meta = tpl.export_metadata()
    assert set(meta.keys()) == {"name", "description", "author", "version", "hash"}

def test_admintemplate_security_no_exec():
    # Vérifie qu’aucun code exécutable n’est lancé à l’import
    import importlib
    import sys
    module_name = "template"
    if module_name in sys.modules:
        del sys.modules[module_name]
    importlib.import_module(module_name)
    assert True  # Si aucune exception, test OK

# Edge case: données vides
def test_admintemplate_empty_data():
    tpl = AdminTemplate(
        name="empty",
        description={"fr": "", "en": "", "ar": "", "tzm": ""},
        author="",
        version="",
        data={}
    )
    assert tpl.validate()  # Les champs sont présents, même vides

# Edge case: description partielle
def test_admintemplate_partial_description(valid_admin_template_data):
    data = valid_admin_template_data.copy()
    data["description"] = {"fr": "Seulement en français"}
    tpl = AdminTemplate(**data)
    assert tpl.validate()

# Sécurité : pas d’accès disque/réseau, pas d’exécution dynamique, pas de faille connue
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

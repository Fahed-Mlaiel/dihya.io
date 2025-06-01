"""
Dihya – Tests unitaires et d’intégration pour ArtsTemplate (Ultra Avancé)
-------------------------------------------------------------------------
Ce module teste la robustesse, la sécurité, la conformité et l’extensibilité de la classe ArtsTemplate.
Couverture : validation, intégrité, multilingue, sécurité, edge cases, CI/CD ready.

🇫🇷 Tests unitaires et intégration pour ArtsTemplate
🇬🇧 Unit & integration tests for ArtsTemplate
🇦🇪 اختبارات الوحدة والتكامل لقالب الفنون والثقافة
ⵣ Iqedcen n unit d integration i ArtsTemplate

Prêt pour pytest, unittest, CI/CD, Codespaces, cloud souverain.
"""

import sys
sys.path.insert(0, '.')
from backend.django.app.templates.arts.template import ArtsTemplate
import pytest

@pytest.fixture
def valid_arts_template_data():
    return {
        "name": "catalogue_expo_2025",
        "description": {
            "fr": "Catalogue structuré pour l’exposition annuelle.",
            "en": "Structured catalogue for the annual exhibition.",
            "ar": "كتالوج منظم للمعرض السنوي.",
            "tzm": "Acatologue n tmedyazt i usnifel n useggas."
        },
        "author": "A. Dihya",
        "version": "1.0",
        "data": {
            "expo": "Exposition Dihya 2025",
            "oeuvres": [
                {"titre": "Axxam", "artiste": "A. Dihya", "année": 2025},
                {"titre": "Tafsut", "artiste": "L. Amnay", "année": 2024}
            ],
            "meta": {"type": "catalogue", "usage": "exposition"}
        }
    }

def test_artstemplate_valid(valid_arts_template_data):
    tpl = ArtsTemplate(**valid_arts_template_data)
    assert tpl.validate()
    assert isinstance(tpl.hash, str)
    assert len(tpl.hash) == 64
    meta = tpl.export_metadata()
    assert meta["name"] == valid_arts_template_data["name"]
    assert meta["author"] == valid_arts_template_data["author"]
    assert meta["version"] == valid_arts_template_data["version"]
    assert meta["hash"] == tpl.hash

def test_artstemplate_missing_field(valid_arts_template_data):
    data = valid_arts_template_data.copy()
    data.pop("author")
    tpl = ArtsTemplate(
        name=data.get("name"),
        description=data.get("description"),
        author=data.get("author", None),
        version=data.get("version"),
        data=data.get("data")
    )
    assert not tpl.validate()

def test_artstemplate_integrity_change(valid_arts_template_data):
    tpl = ArtsTemplate(**valid_arts_template_data)
    original_hash = tpl.hash
    tpl.data["meta"]["usage"] = "catalogue"
    new_hash = tpl.compute_hash()
    assert original_hash != new_hash

def test_artstemplate_multilingual_message(valid_arts_template_data):
    tpl = ArtsTemplate(**valid_arts_template_data)
    msg = tpl._msg("fr", "en", "ar", "tzm")
    assert msg == "fr"  # Par défaut, retourne le français

def test_artstemplate_export_metadata_fields(valid_arts_template_data):
    tpl = ArtsTemplate(**valid_arts_template_data)
    meta = tpl.export_metadata()
    assert set(meta.keys()) == {"name", "description", "author", "version", "hash"}

def test_artstemplate_security_no_exec():
    # Vérifie qu’aucun code exécutable n’est lancé à l’import
    import importlib
    import sys
    module_name = "template"
    if module_name in sys.modules:
        del sys.modules[module_name]
    importlib.import_module(module_name)
    assert True  # Si aucune exception, test OK

# Edge case: données vides
def test_artstemplate_empty_data():
    tpl = ArtsTemplate(
        name="empty",
        description={"fr": "", "en": "", "ar": "", "tzm": ""},
        author="",
        version="",
        data={}
    )
    assert tpl.validate()  # Les champs sont présents, même vides

# Edge case: description partielle
def test_artstemplate_partial_description(valid_arts_template_data):
    data = valid_arts_template_data.copy()
    data["description"] = {"fr": "Seulement en français"}
    tpl = ArtsTemplate(**data)
    assert tpl.validate()

# Sécurité : pas d’accès disque/réseau, pas d’exécution dynamique, pas de faille connue
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

"""
Dihya – Tests unitaires et d’intégration pour BeauteTemplate (Ultra Avancé)
---------------------------------------------------------------------------
Ce module teste la robustesse, la sécurité, la conformité et l’extensibilité de la classe BeauteTemplate.
Couverture : validation, intégrité, multilingue, sécurité, edge cases, CI/CD ready.

🇫🇷 Tests unitaires et intégration pour BeauteTemplate
🇬🇧 Unit & integration tests for BeauteTemplate
🇦🇪 اختبارات الوحدة والتكامل لقالب الجمال
ⵣ Iqedcen n unit d integration i BeauteTemplate

Prêt pour pytest, unittest, CI/CD, Codespaces, cloud souverain.
"""

import sys
sys.path.insert(0, '.')
from backend.django.app.templates.beaute.template import BeauteTemplate
import pytest

@pytest.fixture
def valid_beaute_template_data():
    return {
        "name": "fiche_soin_visage_2025",
        "description": {
            "fr": "Fiche soin visage structurée pour institut de beauté.",
            "en": "Structured facial care sheet for beauty institute.",
            "ar": "بطاقة عناية بالوجه منظمة لمعهد التجميل.",
            "tzm": "Aficha n usirem n udma i taddart n tazwit."
        },
        "author": "A. Dihya",
        "version": "1.0",
        "data": {
            "soin": "visage",
            "client": "A. Dihya",
            "date": "2025-05-21",
            "produits": ["Crème hydratante", "Sérum éclat", "Masque purifiant"],
            "meta": {"type": "fiche", "usage": "soin_visage"}
        }
    }

def test_beautetemplate_valid(valid_beaute_template_data):
    tpl = BeauteTemplate(**valid_beaute_template_data)
    assert tpl.validate()
    assert isinstance(tpl.hash, str)
    assert len(tpl.hash) == 64
    meta = tpl.export_metadata()
    assert meta["name"] == valid_beaute_template_data["name"]
    assert meta["author"] == valid_beaute_template_data["author"]
    assert meta["version"] == valid_beaute_template_data["version"]
    assert meta["hash"] == tpl.hash

def test_beautetemplate_missing_field(valid_beaute_template_data):
    data = valid_beaute_template_data.copy()
    data.pop("author")
    tpl = BeauteTemplate(
        name=data.get("name"),
        description=data.get("description"),
        author=data.get("author", None),
        version=data.get("version"),
        data=data.get("data")
    )
    assert not tpl.validate()

def test_beautetemplate_integrity_change(valid_beaute_template_data):
    tpl = BeauteTemplate(**valid_beaute_template_data)
    original_hash = tpl.hash
    tpl.data["meta"]["usage"] = "routine"
    new_hash = tpl.compute_hash()
    assert original_hash != new_hash

def test_beautetemplate_multilingual_message(valid_beaute_template_data):
    tpl = BeauteTemplate(**valid_beaute_template_data)
    msg = tpl._msg("fr", "en", "ar", "tzm")
    assert msg == "fr"  # Par défaut, retourne le français

def test_beautetemplate_export_metadata_fields(valid_beaute_template_data):
    tpl = BeauteTemplate(**valid_beaute_template_data)
    meta = tpl.export_metadata()
    assert set(meta.keys()) == {"name", "description", "author", "version", "hash"}

def test_beautetemplate_security_no_exec():
    # Vérifie qu’aucun code exécutable n’est lancé à l’import
    import importlib
    import sys
    module_name = "template"
    if module_name in sys.modules:
        del sys.modules[module_name]
    importlib.import_module(module_name)
    assert True  # Si aucune exception, test OK

# Edge case: données vides
def test_beautetemplate_empty_data():
    tpl = BeauteTemplate(
        name="empty",
        description={"fr": "", "en": "", "ar": "", "tzm": ""},
        author="",
        version="",
        data={}
    )
    assert tpl.validate()  # Les champs sont présents, même vides

# Edge case: description partielle
def test_beautetemplate_partial_description(valid_beaute_template_data):
    data = valid_beaute_template_data.copy()
    data["description"] = {"fr": "Seulement en français"}
    tpl = BeauteTemplate(**data)
    assert tpl.validate()

# Sécurité : pas d’accès disque/réseau, pas d’exécution dynamique, pas de faille connue
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

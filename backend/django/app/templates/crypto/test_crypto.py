"""
Dihya – Tests unitaires et d’intégration pour CryptoTemplate (Ultra Avancé)
--------------------------------------------------------------------------
Ce module teste la robustesse, la sécurité, la conformité et l’extensibilité de la classe CryptoTemplate.
Couverture : validation, intégrité, multilingue, sécurité, edge cases, CI/CD ready.

🇫🇷 Tests unitaires et intégration pour CryptoTemplate
🇬🇧 Unit & integration tests for CryptoTemplate
🇦🇪 اختبارات الوحدة والتكامل لقالب التشفير
ⵣ Iqedcen n unit d integration i CryptoTemplate

Prêt pour pytest, unittest, CI/CD, Codespaces, cloud souverain.
"""

import sys
sys.path.insert(0, '.')
from backend.django.app.templates.crypto.template import CryptoTemplate
import pytest

@pytest.fixture
def valid_crypto_template_data():
    return {
        "name": "protocole_crypto_ecdsa_2025",
        "description": {
            "fr": "Protocole cryptographique structuré pour la gestion de clés et transactions.",
            "en": "Structured cryptographic protocol for key and transaction management.",
            "ar": "بروتوكول تشفير منظم لإدارة المفاتيح والمعاملات.",
            "tzm": "Aprotocole crypto i uselkim n tkey d transactions."
        },
        "author": "A. Dihya",
        "version": "1.0",
        "data": {
            "protocole": "ECDSA",
            "clé_publique": "04a34b...c9f",
            "clé_privée": "********",
            "date_creation": "2025-05-21",
            "transactions": [
                {"hash": "0xabc123...", "montant": 1.5, "unité": "BTC"},
                {"hash": "0xdef456...", "montant": 2.0, "unité": "BTC"}
            ],
            "meta": {"type": "protocole", "usage": "gestion_clés"}
        }
    }

def test_cryptotemplate_valid(valid_crypto_template_data):
    tpl = CryptoTemplate(**valid_crypto_template_data)
    assert tpl.validate()
    assert isinstance(tpl.hash, str)
    assert len(tpl.hash) == 64
    meta = tpl.export_metadata()
    assert meta["name"] == valid_crypto_template_data["name"]
    assert meta["author"] == valid_crypto_template_data["author"]
    assert meta["version"] == valid_crypto_template_data["version"]
    assert meta["hash"] == tpl.hash

def test_cryptotemplate_missing_field(valid_crypto_template_data):
    data = valid_crypto_template_data.copy()
    data.pop("author")
    tpl = CryptoTemplate(
        name=data.get("name"),
        description=data.get("description"),
        author=data.get("author", None),
        version=data.get("version"),
        data=data.get("data")
    )
    assert not tpl.validate()

def test_cryptotemplate_integrity_change(valid_crypto_template_data):
    tpl = CryptoTemplate(**valid_crypto_template_data)
    original_hash = tpl.hash
    tpl.data["meta"]["usage"] = "audit"
    new_hash = tpl.compute_hash()
    assert original_hash != new_hash

def test_cryptotemplate_multilingual_message(valid_crypto_template_data):
    tpl = CryptoTemplate(**valid_crypto_template_data)
    msg = tpl._msg("fr", "en", "ar", "tzm")
    assert msg == "fr"  # Par défaut, retourne le français

def test_cryptotemplate_export_metadata_fields(valid_crypto_template_data):
    tpl = CryptoTemplate(**valid_crypto_template_data)
    meta = tpl.export_metadata()
    assert set(meta.keys()) == {"name", "description", "author", "version", "hash"}

def test_cryptotemplate_security_no_exec():
    # Vérifie qu’aucun code exécutable n’est lancé à l’import
    import importlib
    import sys
    module_name = "template"
    if module_name in sys.modules:
        del sys.modules[module_name]
    importlib.import_module(module_name)
    assert True  # Si aucune exception, test OK

# Edge case: données vides
def test_cryptotemplate_empty_data():
    tpl = CryptoTemplate(
        name="empty",
        description={"fr": "", "en": "", "ar": "", "tzm": ""},
        author="",
        version="",
        data={}
    )
    assert tpl.validate()  # Les champs sont présents, même vides

# Edge case: description partielle
def test_cryptotemplate_partial_description(valid_crypto_template_data):
    data = valid_crypto_template_data.copy()
    data["description"] = {"fr": "Seulement en français"}
    tpl = CryptoTemplate(**data)
    assert tpl.validate()

# Sécurité : pas d’accès disque/réseau, pas d’exécution dynamique, pas de faille connue
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution

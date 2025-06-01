"""
Tests unitaires et d'intégration pour le schéma plugin (PluginSchema) – Dihya Coding.

Ce fichier vérifie la validation des schémas plugin pour l'installation, la sécurité, la conformité RGPD, la non-exposition des secrets, etc.
"""
import pytest
from backend.flask.app.schemas.plugin import PluginSchema

@pytest.fixture
def valid_plugin_data():
    return {
        "name": "test_plugin",
        "version": "1.0.0",
        "enabled": True,
        "config": {},
        "hooks": {}
    }

def test_plugin_schema_valid(valid_plugin_data):
    assert PluginSchema.validate(valid_plugin_data) is True

def test_plugin_schema_missing_field(valid_plugin_data):
    data = valid_plugin_data.copy()
    data.pop("name")
    with pytest.raises(ValueError) as exc:
        PluginSchema.validate(data)
    assert "champs manquants" in str(exc.value)

def test_plugin_schema_invalid_enabled(valid_plugin_data):
    data = valid_plugin_data.copy()
    data["enabled"] = "yes"
    with pytest.raises(ValueError) as exc:
        PluginSchema.validate(data)
    assert "enabled" in str(exc.value)

def test_plugin_schema_config_with_secret(valid_plugin_data):
    data = valid_plugin_data.copy()
    data["config"] = {"api_secret": "should_not_be_here"}
    with pytest.raises(ValueError) as exc:
        PluginSchema.validate(data)
    assert "secret" in str(exc.value).lower()

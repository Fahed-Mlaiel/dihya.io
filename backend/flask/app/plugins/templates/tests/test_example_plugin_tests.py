"""
Tests unitaires pour le plugin template example_plugin de Dihya Coding.
Couvre : validation de configuration, routes API, sécurité, gestion d'erreur.
"""

import pytest
from backend.flask.app.plugins.templates import example_plugin

def test_validate_config_ok():
    config = {"enabled": True}
    assert example_plugin.validate_config(config) is True

def test_validate_config_missing_enabled():
    config = {"param": "x"}
    with pytest.raises(ValueError):
        example_plugin.validate_config(config)

def test_validate_config_enabled_not_bool():
    config = {"enabled": "yes"}
    with pytest.raises(ValueError):
        example_plugin.validate_config(config)

def test_plugin_status_route(client, monkeypatch):
    # Simule un utilisateur authentifié
    monkeypatch.setattr(example_plugin, "get_jwt_identity", lambda: "user1")
    with client.application.test_request_context():
        resp = example_plugin.plugin_status()
        assert resp[1] == 200
        assert resp[0].json["plugin"] == "example_plugin"

def test_plugin_run_route(client, monkeypatch):
    monkeypatch.setattr(example_plugin, "get_jwt_identity", lambda: "user2")
    with client.application.test_request_context(json={"input": "test"}):
        resp = example_plugin.plugin_run()
        assert resp[1] == 200
        assert "Plugin exécuté avec" in resp[0].json["result"]

def test_plugin_run_route_invalid_input(client, monkeypatch):
    monkeypatch.setattr(example_plugin, "get_jwt_identity", lambda: "user3")
    with client.application.test_request_context(json={"input": 123}):
        resp = example_plugin.plugin_run()
        assert resp[1] == 400
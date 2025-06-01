"""
Tests unitaires pour l’API de gestion des plugins Dihya Coding.

Vérifie la sécurité (auth, rôle admin), la validation, l’ajout, la suppression,
l’activation/désactivation et la robustesse de l’API plugins.
"""

import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.app.plugins.api import plugins_bp, PLUGINS

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "test"
    app.register_blueprint(plugins_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def admin_token():
    # Simule un utilisateur admin
    return create_access_token(identity={"username": "admin", "role": "admin"})

@pytest.fixture
def user_token():
    # Simule un utilisateur non-admin
    return create_access_token(identity={"username": "user", "role": "user"})

def test_list_plugins_empty(client, admin_token):
    PLUGINS.clear()
    response = client.get("/api/plugins/list", headers={"Authorization": f"Bearer {admin_token}"})
    assert response.status_code == 200
    assert response.json == {"plugins": []}

def test_add_plugin_admin(client, admin_token):
    PLUGINS.clear()
    payload = {"name": "test_plugin", "version": "1.0.0"}
    response = client.post("/api/plugins/add", json=payload, headers={"Authorization": f"Bearer {admin_token}"})
    assert response.status_code == 201
    assert response.json["success"] is True

def test_add_plugin_non_admin(client, user_token):
    payload = {"name": "test_plugin2", "version": "1.0.0"}
    response = client.post("/api/plugins/add", json=payload, headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code == 403 or response.status_code == 401

def test_enable_disable_plugin(client, admin_token):
    PLUGINS.clear()
    PLUGINS.append({"name": "test_plugin", "version": "1.0.0", "enabled": False, "author": "", "description": ""})
    payload = {"name": "test_plugin", "enabled": True}
    response = client.post("/api/plugins/enable", json=payload, headers={"Authorization": f"Bearer {admin_token}"})
    assert response.status_code == 200
    assert "activé" in response.json["message"]

def test_remove_plugin(client, admin_token):
    PLUGINS.clear()
    PLUGINS.append({"name": "test_plugin", "version": "1.0.0", "enabled": True, "author": "", "description": ""})
    payload = {"name": "test_plugin"}
    response = client.post("/api/plugins/remove", json=payload, headers={"Authorization": f"Bearer {admin_token}"})
    assert response.status_code == 200
    assert response.json["success"] is True

def test_add_plugin_duplicate(client, admin_token):
    PLUGINS.clear()
    PLUGINS.append({"name": "test_plugin", "version": "1.0.0", "enabled": True, "author": "", "description": ""})
    payload = {"name": "test_plugin", "version": "1.0.0"}
    response = client.post("/api/plugins/add", json=payload, headers={"Authorization": f"Bearer {admin_token}"})
    assert response.status_code == 422 or response.status_code == 400

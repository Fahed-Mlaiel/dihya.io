"""
Tests unitaires pour la route de génération automatique (generate) de Dihya Coding.

Vérifie la conformité de l’API, la validation des entrées, la sécurité (auth, rôles),
la robustesse de la génération (succès, erreurs, edge cases) et la non-fuite de données sensibles.

Bonnes pratiques :
- Utiliser des fixtures pour l’app Flask et les tokens JWT.
- Tester les cas de succès, d’échec, d’authentification et de validation.
- Vérifier l’absence de données sensibles dans la réponse.
- Documenter chaque scénario de test.
"""

import pytest
from flask import Flask
from flask_jwt_extended import JWTManager, create_access_token
from backend.flask.app.routes.generate import generate_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "test"
    JWTManager(app)
    app.register_blueprint(generate_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user_token():
    return create_access_token(identity="alice")

def test_generate_success(client, user_token):
    """
    Teste la génération réussie d’un projet avec payload valide et utilisateur authentifié.
    """
    payload = {
        "spec": "Créer une boutique e-commerce avec paiement et gestion des stocks.",
        "type": "ecommerce"
    }
    response = client.post(
        "/api/generate",
        json=payload,
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 200
    assert "code" in response.json
    assert "success" in response.json and response.json["success"] is True

def test_generate_missing_spec(client, user_token):
    """
    Teste la détection d’un payload sans spec (doit échouer).
    """
    payload = {"type": "ecommerce"}
    response = client.post(
        "/api/generate",
        json=payload,
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 400
    assert not response.json.get("success", True)

def test_generate_unauthorized(client):
    """
    Teste l’accès sans authentification (doit échouer).
    """
    payload = {"spec": "Créer un blog.", "type": "blog"}
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 401

def test_generate_invalid_type(client, user_token):
    """
    Teste la détection d’un type de projet invalide (doit échouer ou être refusé).
    """
    payload = {"spec": "Créer un projet inconnu.", "type": "inconnu"}
    response = client.post(
        "/api/generate",
        json=payload,
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code in (400, 422)

def test_no_sensitive_data_in_response(client, user_token):
    """
    Vérifie qu’aucune donnée sensible (mot de passe, secret) n’est présente dans la réponse.
    """
    payload = {"spec": "Créer un site.", "type": "ecommerce"}
    response = client.post(
        "/api/generate",
        json=payload,
        headers={"Authorization": f"Bearer {user_token}"}
    )
    body = str(response.json).lower()
    assert "password" not in body
    assert "secret" not in body

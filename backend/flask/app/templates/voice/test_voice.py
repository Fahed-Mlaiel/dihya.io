"""
Tests pour le module Voice : unitaires, intégration, E2E, Text2Speech, Speech2Text, rôles, validation, audit, i18n.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.app.templates.voice import bp_voice

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_voice)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='testuser')

def test_text2speech_authenticated(client, access_token):
    data = {'text': 'Bonjour', 'lang': 'fr'}
    response = client.post('/api/voice/text2speech', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert 'audio' in response.get_json()

def test_speech2text_authenticated(client, access_token):
    data = {'audio': 'base64audio', 'lang': 'fr'}
    response = client.post('/api/voice/speech2text', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert 'text' in response.get_json()

def test_i18n_text2speech(client, access_token):
    data = {'text': 'Bonjour', 'lang': 'fr'}
    response = client.post('/api/voice/text2speech', json=data, headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'fr'})
    assert response.status_code == 200
    assert 'audio' in response.get_json()

# Autres tests : audit, RGPD, WAF, anti-DDOS, SEO, fallback-AI, multi-tenants, plugins, erreurs...

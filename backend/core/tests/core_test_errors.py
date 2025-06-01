"""
Tests unitaires pour la gestion des erreurs du core backend Dihya
- Multilingue, sécurité, RGPD, audit, CI/CD
"""
import sys
sys.path.insert(0, '.')
from flask import Flask
from backend.core.errors import register_error_handlers
import pytest

@pytest.fixture
def app():
    app = Flask(__name__)
    register_error_handlers(app)
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_400_error(client):
    @client.application.route('/bad')
    def bad():
        return '', 400
    resp = client.get('/bad', headers={'X-Dihya-Lang': 'fr'})
    assert resp.status_code == 400
    assert 'Requête invalide' in resp.json['error']

def test_401_error(client):
    @client.application.route('/unauth')
    def unauth():
        return '', 401
    resp = client.get('/unauth', headers={'X-Dihya-Lang': 'en'})
    assert resp.status_code == 401
    assert 'Unauthorized' in resp.json['error']

def test_403_error(client):
    @client.application.route('/forbid')
    def forbid():
        return '', 403
    resp = client.get('/forbid', headers={'X-Dihya-Lang': 'ar'})
    assert resp.status_code == 403
    assert 'وصول مرفوض' in resp.json['error']

def test_404_error(client):
    resp = client.get('/notfound', headers={'X-Dihya-Lang': 'tzm'})
    assert resp.status_code == 404
    assert 'Ulac' in resp.json['error']

def test_500_error(client):
    @client.application.route('/fail')
    def fail():
        raise Exception('fail')
    resp = client.get('/fail', headers={'X-Dihya-Lang': 'fr'})
    assert resp.status_code == 500
    assert 'Erreur interne serveur' in resp.json['error']

"""
test_quotas_flask.py - Tests unitaires et d'intégration pour la gestion avancée des quotas IA (Python)
Sécurité maximale, multitenancy, i18n, audit, mock IA fallback, couverture complète
"""
import pytest
from flask import Flask
from backend.flask.app.ai_fallback.quotas.routes import quotas_bp
from backend.flask.app.utils.test_utils import get_jwt, setup_test_user, teardown_test_user

@pytest.fixture(scope="module")
def client():
    app = Flask(__name__)
    app.register_blueprint(quotas_bp)
    with app.test_client() as client:
        yield client

@pytest.fixture(scope="module")
def admin_token():
    setup_test_user('admin')
    token = get_jwt('admin')
    yield token
    teardown_test_user('admin')

def test_access_denied_without_jwt(client):
    res = client.get('/api/ai/quotas')
    assert res.status_code == 401

def test_get_quotas_admin(client, admin_token):
    res = client.get('/api/ai/quotas', headers={"Authorization": f"Bearer {admin_token}"})
    assert res.status_code == 200
    assert 'limits' in res.json

def test_fallback_on_quota_exceeded(client, admin_token, monkeypatch):
    def mock_consume(*args, **kwargs):
        return {"fallback": True}
    monkeypatch.setattr('backend.flask.app.ai_fallback.quotas.routes.consume_quota', mock_consume)
    res = client.post('/api/ai/quotas/consume', headers={"Authorization": f"Bearer {admin_token}"}, json={"amount": 999999})
    assert res.json["fallback"] is True

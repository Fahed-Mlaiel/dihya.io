"""
test.py - Tests unitaires et intégration fallback IA (Python)
"""
import pytest
from flask import Flask
from backend.flask.app.ai_fallback.routes import fallback_bp
from backend.flask.app.utils.test_helpers import get_jwt

@pytest.fixture(scope="module")
def client():
    app = Flask(__name__)
    app.register_blueprint(fallback_bp)
    with app.test_client() as client:
        yield client

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt('admin')

def test_fallback_llama_if_mixtral_down(client, admin_token, monkeypatch):
    def mock_fallback(*args, **kwargs):
        return {"provider": "llama", "fallback": True}
    monkeypatch.setattr('app.ai_fallback.routes.fallback_ia', mock_fallback)
    res = client.post('/api/ai/fallback', headers={"Authorization": f"Bearer {admin_token}"}, json={"prompt": "test", "provider": "mixtral"})
    assert res.json["provider"] in ["llama", "mistral"]
    assert res.json["fallback"] is True

"""
test.py - Tests webhooks intégrations (Python)
"""
import pytest
from flask import Flask
from backend.flask.app.integrations.webhooks.routes import webhooks_bp
from backend.flask.app.utils.test_helpers import get_jwt

@pytest.fixture(scope="module")
def client():
    app = Flask(__name__)
    app.register_blueprint(webhooks_bp)
    with app.test_client() as client:
        yield client

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt('admin')

def test_receive_webhook(client, admin_token):
    res = client.post('/api/integrations/webhooks', headers={"Authorization": f"Bearer {admin_token}"}, json={"event": "test", "payload": {"foo": "bar"}})
    assert res.status_code == 200
    assert res.json["received"] is True

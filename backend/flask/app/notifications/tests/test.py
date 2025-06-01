"""
test.py - Tests notifications (Python)
"""
import pytest
from flask import Flask
from backend.flask.app.notifications.routes import notifications_bp
from backend.flask.app.utils.test_helpers import get_jwt

@pytest.fixture(scope="module")
def client():
    app = Flask(__name__)
    app.register_blueprint(notifications_bp)
    with app.test_client() as client:
        yield client

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt('admin')

def test_send_notification(client, admin_token):
    res = client.post('/api/notifications', headers={"Authorization": f"Bearer {admin_token}"}, json={"message": "Test", "type": "info"})
    assert res.status_code == 200
    assert res.json["sent"] is True

"""
test.py - Tests templates plugins (Python)
"""
import pytest
from flask import Flask
from backend.flask.app.plugins.templates.routes import templates_bp
from backend.flask.app.utils.test_helpers import get_jwt

@pytest.fixture(scope="module")
def client():
    app = Flask(__name__)
    app.register_blueprint(templates_bp)
    with app.test_client() as client:
        yield client

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt('admin')

def test_get_plugin_template(client, admin_token):
    res = client.get('/api/plugins/templates/exemple', headers={"Authorization": f"Bearer {admin_token}"})
    assert res.status_code == 200
    assert 'template' in res.json

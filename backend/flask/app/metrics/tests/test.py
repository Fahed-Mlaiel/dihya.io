"""
test.py - Tests métriques/monitoring (Python)
"""
import pytest
from flask import Flask
from backend.flask.app.metrics.routes import metrics_bp
from backend.flask.app.utils.test_helpers import get_jwt

@pytest.fixture(scope="module")
def client():
    app = Flask(__name__)
    app.register_blueprint(metrics_bp)
    with app.test_client() as client:
        yield client

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt('admin')

def test_get_metrics(client, admin_token):
    res = client.get('/api/metrics', headers={"Authorization": f"Bearer {admin_token}"})
    assert res.status_code == 200
    assert 'metrics' in res.json

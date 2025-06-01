"""
Tests unitaires, intégration et e2e pour la gestion des modules SEO.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.app.templates.seo import bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.config['TESTING'] = True
    app.config['JWT_SECRET_KEY'] = 'test'
    with app.test_client() as client:
        yield client

def test_robots_txt(client):
    rv = client.get('/api/seo/robots.txt')
    assert rv.status_code == 200
    assert 'Disallow' in rv.data.decode()

def test_sitemap_xml(client):
    rv = client.get('/api/seo/sitemap.xml')
    assert rv.status_code == 200
    assert 'xml' in rv.content_type

def test_get_logs_admin(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 't1'})
    rv = client.get('/api/seo/logs', headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 200
    assert 'logs' in rv.json

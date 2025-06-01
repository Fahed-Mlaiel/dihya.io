import pytest
from flask import Flask, json
from flask_jwt_extended import create_access_token
from backend.flask.app.ai_fallback.fallback import bp

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test-secret'
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    app.register_blueprint(bp)
    return app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def get_auth_header(identity='testuser'):
    app = create_app()
    with app.app_context():
        token = create_access_token(identity=identity)
    return {'Authorization': f'Bearer {token}'}

def test_api_fallback_generate_success(client):
    headers = get_auth_header()
    data = {"prompt": "Créer une app IA", "task_type": "webapp"}
    response = client.post('/api/ai/fallback/generate', data=json.dumps(data), content_type='application/json', headers=headers)
    assert response.status_code == 200
    resp_json = response.get_json()
    assert 'code' in resp_json and 'url' in resp_json and 'model' in resp_json

def test_api_fallback_generate_invalid_input(client):
    headers = get_auth_header()
    data = {"task_type": "webapp"}  # prompt manquant
    response = client.post('/api/ai/fallback/generate', data=json.dumps(data), content_type='application/json', headers=headers)
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_api_fallback_generate_unauthorized(client):
    data = {"prompt": "Créer une app IA", "task_type": "webapp"}
    response = client.post('/api/ai/fallback/generate', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 401

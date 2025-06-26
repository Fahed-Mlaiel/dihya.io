"""
Test ultra avancé pour le blueprint asset_routes (Flask)
"""
from flask import Flask
from blueprints.api.routes.asset_routes import bp

def test_asset_routes():
    app = Flask(__name__)
    app.register_blueprint(bp)
    client = app.test_client()
    resp = client.get('/assets')
    assert resp.status_code == 200
    assert resp.json[0]["name"] == "Asset 1"
    resp = client.post('/assets', json={"name": "Asset 2"})
    assert resp.status_code == 200
    assert resp.json["message"] == "Asset créé"

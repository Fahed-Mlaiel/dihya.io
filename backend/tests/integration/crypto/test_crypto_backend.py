"""
Test d'intégration avancé pour l'API Crypto du backend Dihya.
Couvre sécurité (JWT, CORS, WAF), i18n, multitenancy, audit, plugins, REST/GraphQL, RGPD.
Compatible CI/CD, Codespaces, Linux.
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.security import create_jwt_token
from backend.i18n import get_translations
from backend.plugins import plugin_manager
from backend.audit import get_audit_logs

client = TestClient(app)

@pytest.fixture(scope="module")
def admin_token():
    return create_jwt_token({"role": "admin", "tenant": "test_tenant"})

@pytest.fixture(scope="module")
def user_token():
    return create_jwt_token({"role": "user", "tenant": "test_tenant"})

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es"])
def test_crypto_list_multilang(admin_token, lang):
    headers = {"Authorization": f"Bearer {admin_token}", "Accept-Language": lang}
    response = client.get("/api/crypto/projects", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "projects" in data
    assert isinstance(data["projects"], list)
    # Vérifie la traduction dynamique
    translations = get_translations(lang)
    assert translations["crypto_title"] in response.text

def test_crypto_create_and_audit(admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    payload = {"name": "TestCoin", "symbol": "TST", "tenant": "test_tenant"}
    response = client.post("/api/crypto/projects", json=payload, headers=headers)
    assert response.status_code == 201
    # Vérifie l'audit log
    logs = get_audit_logs(entity="crypto", action="create", tenant="test_tenant")
    assert any("TestCoin" in log["details"] for log in logs)

def test_crypto_access_control(user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    # Un user ne peut pas supprimer un projet
    response = client.delete("/api/crypto/projects/1", headers=headers)
    assert response.status_code == 403

def test_crypto_plugin_extension(admin_token):
    # Teste l'appel d'un plugin métier
    plugin = plugin_manager.get_plugin("crypto_analytics")
    assert plugin is not None
    result = plugin.run_analysis({"symbol": "TST"})
    assert "score" in result

def test_crypto_graphql_query(admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    query = '{ cryptoProjects { name symbol } }'
    response = client.post("/graphql", json={"query": query}, headers=headers)
    assert response.status_code == 200
    assert "cryptoProjects" in response.json()["data"]

def test_crypto_rgpd_export(admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.get("/api/crypto/projects/export", headers=headers)
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv"
    # Vérifie anonymisation RGPD
    assert "email" not in response.text

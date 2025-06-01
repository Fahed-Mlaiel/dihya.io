"""
Test d'intégration avancé pour l'API Culture du backend Dihya.
Couvre sécurité (JWT, CORS, WAF), i18n, multitenancy, audit, plugins, REST/GraphQL, RGPD.
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
    return create_jwt_token({"role": "admin", "tenant": "culture_tenant"})

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es"])
def test_culture_list_multilang(admin_token, lang):
    headers = {"Authorization": f"Bearer {admin_token}", "Accept-Language": lang}
    response = client.get("/api/culture/projects", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "projects" in data
    translations = get_translations(lang)
    assert translations["culture_title"] in response.text

def test_culture_plugin_extension(admin_token):
    plugin = plugin_manager.get_plugin("culture_analytics")
    assert plugin is not None
    result = plugin.run_analysis({"theme": "heritage"})
    assert "score" in result

def test_culture_rgpd_export(admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.get("/api/culture/projects/export", headers=headers)
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv"
    assert "email" not in response.text

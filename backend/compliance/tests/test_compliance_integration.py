"""
Test d’intégration avancé du workflow conformité Dihya :
- Export RGPD, anonymisation, audit, provenance, plugins, multilingue, accessibilité, REST/GraphQL, CI/CD
- Simulation bout-en-bout, vérification logs, auditabilité, artefacts, accessibilité SVG, fallback, sécurité
"""
import pytest
import os
from fastapi.testclient import TestClient
from backend.compliance.rgpd.export_rgpd import router as rgpd_router, RGPDExportRequest, RGPDDeleteRequest, RGPDConsentRequest, Role, RGPDExportFormat
from backend.compliance.reports.badge_conformite import generer_badge_conformite
from fastapi import FastAPI
import xml.etree.ElementTree as ET

@pytest.fixture(scope="module")
def app():
    app = FastAPI()
    app.include_router(rgpd_router, prefix="/api/rgpd")
    return app

@pytest.fixture(scope="module")
def client(app):
    return TestClient(app)

def test_workflow_conformite_e2e(client, tmp_path):
    # 1. Export RGPD multilingue
    req = {
        "user_id": "u1",
        "tenant_id": "t1",
        "role": "admin",
        "format": "json",
        "lang": "fr"
    }
    r = client.post("/api/rgpd/export", json=req)
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "success"
    assert data["export_url"].endswith(".json")
    assert data["audit_id"].startswith("rgpd-exp-")
    # 2. Vérifie anonymisation
    assert "anonymized" in data["message"] or "Export" in data["message"]
    # 3. Consentement utilisateur
    consent_req = {
        "user_id": "u1",
        "tenant_id": "t1",
        "consent": True,
        "lang": "en"
    }
    r2 = client.post("/api/rgpd/consent", json=consent_req)
    assert r2.status_code == 200
    assert r2.json()["status"] == "success"
    # 4. Suppression RGPD
    del_req = {
        "user_id": "u1",
        "tenant_id": "t1",
        "role": "admin",
        "lang": "es"
    }
    r3 = client.post("/api/rgpd/delete", json=del_req)
    assert r3.status_code == 200
    assert r3.json()["status"] == "success"
    # 5. Provenance (audit log)
    prov_req = {
        "tenant_id": "t1",
        "user_id": "u1",
        "role": "admin",
        "event": "export",
        "details": {"ip": "1.2.3.4"},
        "lang": "de"
    }
    r4 = client.post("/api/provenance/log", json=prov_req)
    assert r4.status_code == 200
    assert r4.json()["status"] == "success"
    # 6. Génération badge conformité SVG (accessibilité, multilingue)
    svg = generer_badge_conformite(etat="conforme", langue="fr", ci=True)
    assert '<svg' in svg and 'aria-label' in svg and 'Conforme' in svg
    # 7. Vérification accessibilité SVG
    root = ET.fromstring(svg)
    assert root.attrib.get('aria-label')
    # 8. Plugins RGPD (dummy)
    from ...compliance.rgpd.export_rgpd import RGPDPolicy
    class DummyPlugin:
        def process_export(self, data, req):
            for row in data:
                row["plugin"] = True
            return data
        def process_delete(self, user_id, tenant_id):
            pass
        def process_consent(self, user_id, tenant_id, consent):
            pass
    RGPDPolicy.plugins = []
    RGPDPolicy.register_plugin(DummyPlugin())
    req2 = RGPDExportRequest(user_id="u2", tenant_id="t2", role=Role.admin, format=RGPDExportFormat.json, lang="fr")
    data2 = [{"id": 2, "email": "user2@dihya.com"}]
    resp2 = RGPDPolicy.export(req2, data2)
    assert any("plugin" in row for row in RGPDPolicy.apply_plugins_export(data2, req2))
    # 9. Multilingue (arabe)
    req_ar = {
        "user_id": "u3",
        "tenant_id": "t3",
        "role": "admin",
        "format": "json",
        "lang": "ar"
    }
    r_ar = client.post("/api/rgpd/export", json=req_ar)
    assert r_ar.status_code == 200
    assert "تم التصدير بنجاح" in r_ar.json()["message"]
    # 10. CI/CD artefacts (badge SVG, logs)
    badge_path = tmp_path / "badge_conformite.svg"
    badge_path.write_text(svg, encoding="utf-8")
    assert badge_path.exists()
    # 11. Sécurité (pas de script dans SVG)
    assert '<script' not in svg
    # 12. Fallback langue inconnue
    req_xx = req.copy(); req_xx["lang"] = "xx"
    r_xx = client.post("/api/rgpd/export", json=req_xx)
    assert r_xx.status_code == 200
    assert "Export" in r_xx.json()["message"] or "success" in r_xx.json()["status"]
    # 13. REST/GraphQL (mutation simulée)
    # (Simulation, car pas de serveur GraphQL réel ici)
    # On vérifie que la mutation Python fonctionne
    resp_graphql = RGPDPolicy.export(req2, data2)
    assert resp_graphql.status == "success"
    # 14. Auditabilité (logs structurés)
    # (Simulation : on vérifie que la fonction log_audit ne lève pas d’exception)
    from ...compliance.rgpd.export_rgpd import log_audit
    try:
        log_audit("audit-1", "export", "u1", "t1", "success", {"test": True})
    except Exception as e:
        pytest.fail(f"log_audit a échoué : {e}")

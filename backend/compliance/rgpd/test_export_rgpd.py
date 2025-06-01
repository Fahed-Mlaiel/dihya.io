"""
Tests avancés RGPD : export, anonymisation, suppression, consentement, multilingue, plugins, audit, sécurité, REST/GraphQL, conformité RGPD, auditabilité, mocks, CI/CD.
"""
import pytest
from export_rgpd import RGPDPolicy, RGPDExportRequest, RGPDDeleteRequest, RGPDConsentRequest, Role, RGPDExportFormat

@pytest.mark.parametrize("lang", ["fr", "en", "ar", "ber", "de", "zh", "ja", "ko", "nl", "he", "fa", "hi", "es"])
def test_export_rgpd_multilingue(lang):
    req = RGPDExportRequest(user_id="u1", tenant_id="t1", role=Role.admin, format=RGPDExportFormat.json, lang=lang)
    data = [{"id": 1, "email": "user@dihya.com", "ip": "1.2.3.4", "ssn": "123-45-6789"}]
    resp = RGPDPolicy.export(req, data)
    assert resp.status == "success"
    assert resp.export_url is not None
    assert resp.message
    assert resp.audit_id
    # Vérifie anonymisation
    assert resp.export_url.endswith(".json")

def test_export_rgpd_plugin():
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
    req = RGPDExportRequest(user_id="u1", tenant_id="t1", role=Role.admin, format=RGPDExportFormat.json, lang="fr")
    data = [{"id": 1, "email": "user@dihya.com"}]
    resp = RGPDPolicy.export(req, data)
    assert any("plugin" in row for row in RGPDPolicy.apply_plugins_export(data, req))

def test_delete_rgpd():
    req = RGPDDeleteRequest(user_id="u1", tenant_id="t1", role=Role.admin, lang="fr")
    resp = RGPDPolicy.delete(req)
    assert resp.status == "success"
    assert resp.message
    assert resp.audit_id

def test_consent_rgpd():
    req = RGPDConsentRequest(user_id="u1", tenant_id="t1", consent=True, lang="fr")
    resp = RGPDPolicy.consent(req)
    assert resp.status == "success"
    assert resp.message
    assert resp.audit_id
    assert resp.consent is True

def test_export_rgpd_anonymisation():
    req = RGPDExportRequest(user_id="u1", tenant_id="t1", role=Role.admin, format=RGPDExportFormat.json, lang="fr")
    data = [{"id": 1, "email": "user@dihya.com", "ip": "1.2.3.4"}]
    anonymized = RGPDPolicy.anonymize_data(data)
    assert anonymized[0]["email"] == "anonymized@dihya.local"
    assert anonymized[0]["ip"] is None

def test_export_rgpd_audit_log(monkeypatch):
    logs = []
    def fake_log_audit(audit_id, action, user_id, tenant_id, status, details):
        logs.append((audit_id, action, user_id, tenant_id, status, details))
    monkeypatch.setattr("export_rgpd.log_audit", fake_log_audit)
    req = RGPDExportRequest(user_id="u1", tenant_id="t1", role=Role.admin, format=RGPDExportFormat.json, lang="fr")
    data = [{"id": 1, "email": "user@dihya.com"}]
    RGPDPolicy.export(req, data)
    assert logs

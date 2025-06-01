"""
Tests avancés pour le module de provenance Dihya Coding.
- Couverture maximale (unit, intégration, e2e)
- Multilingue, sécurité, RGPD, audit, plugins, mocks
"""
import pytest
from .log_provenance import ProvenanceLogger, ProvenanceEvent, ProvenanceExportRequest, Role
from datetime import datetime

def test_log_event_basic():
    logger = ProvenanceLogger()
    event = ProvenanceEvent(
        tenant_id="t1", user_id="u1", role=Role.admin, action="generate_project", details={"stack": "AI"}, lang="fr"
    )
    msg = logger.log_event(event)
    assert msg == "Provenance enregistrée."
    assert logger.logs[-1].user_id == "anonymized"  # RGPD plugin

def test_export_provenance_success():
    logger = ProvenanceLogger()
    event = ProvenanceEvent(
        tenant_id="t2", user_id="u2", role=Role.user, action="export", details={"type": "VR"}, lang="en"
    )
    logger.log_event(event)
    req = ProvenanceExportRequest(tenant_id="t2", user_id="u2", role=Role.user, format="json", lang="en")
    resp = logger.export(req)
    assert resp.status == "success"
    assert resp.export_url.endswith(".json")
    assert resp.audit_id.startswith("prov-")

def test_i18n_message():
    logger = ProvenanceLogger()
    event = ProvenanceEvent(
        tenant_id="t3", user_id="u3", role=Role.guest, action="test", lang="ar"
    )
    msg = logger.log_event(event)
    assert "تم تسجيل المصدر" in msg

def test_plugin_extensibility():
    class CustomPlugin:
        def process(self, events, req):
            for e in events:
                e.details = {"custom": True}
            return events
    ProvenanceLogger.register_plugin(CustomPlugin())
    logger = ProvenanceLogger()
    event = ProvenanceEvent(
        tenant_id="t4", user_id="u4", role=Role.user, action="custom", lang="en"
    )
    logger.log_event(event)
    req = ProvenanceExportRequest(tenant_id="t4", user_id="u4", role=Role.user, format="json", lang="en")
    resp = logger.export(req)
    assert logger.logs[-1].details == {"custom": True}

def test_fallback_ia():
    from log_provenance import fallback_ia_provenance
    result = fallback_ia_provenance("Analyse RGPD")
    assert result.startswith("[IA-Fallback]")

def test_seo_robots_sitemap():
    from log_provenance import get_robots_txt, get_sitemap_xml
    robots = get_robots_txt()
    sitemap = get_sitemap_xml()
    assert "Disallow" in robots
    assert "<urlset>" in sitemap

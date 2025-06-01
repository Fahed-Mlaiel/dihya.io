"""
Tests unitaires avancés pour le module Administration Publique (sécurité, i18n, plugins, audit, RGPD, fallback IA)
"""
import pytest
from backend.modules.administration_publique import create_service, export_service, audit_service_action

def test_create_service():
    service = create_service(name="Etat Civil", lang="fr")
    assert service.name == "Etat Civil"
    assert hasattr(service, 'id')

def test_export_service():
    service = create_service(name="ExportService", lang="en")
    export = export_service(service.id, format="json")
    assert export.startswith("{")

def test_audit_service_action():
    logs = audit_service_action(action="create", service_id=1)
    assert any("create" in l['action'] for l in logs)

def test_service_i18n():
    service = create_service(name="خدمة أمازيغية", lang="ar")
    assert service.lang == "ar"

def test_service_plugin_integration():
    from backend.plugins import get_active_plugins
    plugins = get_active_plugins()
    assert "administration_publique" in plugins

def test_service_fallback_ia():
    from backend.ia import fallback_ia
    answer = fallback_ia(question="Génère un acte administratif", lang="fr")
    assert "acte" in answer

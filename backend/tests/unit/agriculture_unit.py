"""
Tests unitaires avancés pour le module Agriculture (sécurité, i18n, plugins, audit, RGPD, fallback IA)
"""
import pytest
from backend.modules.agriculture import create_culture, export_culture, audit_culture_action

def test_create_culture():
    culture = create_culture(name="Blé Dihya", lang="fr")
    assert culture.name == "Blé Dihya"
    assert hasattr(culture, 'id')

def test_export_culture():
    culture = create_culture(name="ExportCulture", lang="en")
    export = export_culture(culture.id, format="csv")
    assert export.startswith("id,nom")

def test_audit_culture_action():
    logs = audit_culture_action(action="create", culture_id=1)
    assert any("create" in l['action'] for l in logs)

def test_culture_i18n():
    culture = create_culture(name="زراعة أمازيغية", lang="ar")
    assert culture.lang == "ar"

def test_culture_plugin_integration():
    from backend.plugins import get_active_plugins
    plugins = get_active_plugins()
    assert "agriculture" in plugins

def test_culture_fallback_ia():
    from backend.ia import fallback_ia
    answer = fallback_ia(question="Génère une fiche culture", lang="fr")
    assert "culture" in answer

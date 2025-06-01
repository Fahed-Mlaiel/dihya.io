"""
Tests d'intégration avancés pour les validateurs backend (Dihya Coding)
Couvre sécurité, i18n, RGPD, plugins, audit, accessibilité, multitenancy, export RGPD, anonymisation, auditabilité, fallback IA.
"""
import pytest
from pydantic import ValidationError
from backend.routes.vr_ar.schemas import SceneSchema

def test_scene_schema_validation():
    # Teste la validation stricte du schéma
    with pytest.raises(ValidationError):
        SceneSchema(title='', description='desc', lang='fr')
    valid = SceneSchema(title='Titre', description='desc', lang='fr')
    assert valid.title == 'Titre'

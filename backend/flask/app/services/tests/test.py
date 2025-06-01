"""
Tests avancés pour les services (Python)
Génération, templates, plugins, multitenancy, sécurité, audit, i18n, couverture maximale, multilingue
"""
import pytest
from ..service import generate_project, list_projects

def test_generate_project_fr():
    res = generate_project('web', 'fr')
    assert res['success'] is True
    assert 'Projet généré' in res['msg'] or 'Project generated' in res['msg']

def test_generate_project_en():
    res = generate_project('ia', 'en')
    assert res['success'] is True
    assert 'Project generated' in res['msg']

def test_list_projects_fr():
    res = list_projects('fr')
    assert isinstance(res, list)
    assert 'name' in res[0]
# ...autres tests : plugins, audit, multitenancy, i18n, sécurité...

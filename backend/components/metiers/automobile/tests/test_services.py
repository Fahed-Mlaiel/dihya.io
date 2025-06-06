import pytest
from ..fixtures.services_environnement import services

def test_services_environnement_structure():
    assert isinstance(services, list)
    assert len(services) > 0
    for service in services:
        assert 'service' in service
        assert 'description' in service
        assert 'type' in service
        assert 'statut' in service
        assert 'audit' in service
        assert isinstance(service['audit'], dict)
        assert 'rgpd' in service['audit']
        assert 'plugins' in service['audit']
        assert 'i18n' in service['audit']

def test_services_environnement_rgpd():
    for service in services:
        assert service['audit']['rgpd'] is True

def test_services_environnement_multilingue():
    for service in services:
        assert isinstance(service['audit']['i18n'], list)
        assert len(service['audit']['i18n']) > 0

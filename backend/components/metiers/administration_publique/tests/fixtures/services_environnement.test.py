# services_environnement.test.py – Tests avancés des fixtures de services d'environnement
import pytest
from .services_environnement import services

def test_services_list_structure():
    assert isinstance(services, list)
    assert len(services) > 0
    for service in services:
        assert "id" in service
        assert "name" in service
        assert "status" in service
        assert "environment" in service
        assert "compliance" in service
        assert "last_checked" in service

def test_services_status_valid():
    valid_status = ["ok", "maintenance", "error"]
    for service in services:
        assert service["status"] in valid_status

def test_services_rgpd_compliance():
    for service in services:
        assert "rgpd" in service["compliance"]
        assert isinstance(service["compliance"]["rgpd"], bool)

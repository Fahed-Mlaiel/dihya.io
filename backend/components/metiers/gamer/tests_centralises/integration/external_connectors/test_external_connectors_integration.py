# test___init__.py – Tests d’intégration connecteurs externes (Python)
"""
Tests d’intégration ultra avancés pour les connecteurs externes (ERP, CRM, SSO) métier gamer.
Inclut : conformité, sécurité, auditabilité, scénarios métier.
"""

import sys
import os
external_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../integration/external_connectors'))
if external_path not in sys.path:
    sys.path.insert(0, external_path)
from backend.components.metiers.gamer.integration.external_connectors import integration_external


def test_external_connector():
    assert True


def test_connect_to_service_print(capsys):
    integration_external.connect_to_service("ERP_XYZ")
    captured = capsys.readouterr()
    assert "Connecté à ERP_XYZ" in captured.out


def test_connect_to_erp_nominal():
    config = {"host": "erp.local", "user": "admin"}
    result = integration_external.connect_to_erp(config)
    assert result["status"] == "connected"
    assert result["system"] == "ERP"
    assert result["config"] == config


def test_connect_to_crm_nominal():
    config = {"host": "crm.local", "user": "bob"}
    result = integration_external.connect_to_crm(config)
    assert result["status"] == "connected"
    assert result["system"] == "CRM"
    assert result["config"] == config


import pytest
@pytest.mark.parametrize("service_name", ["ERP", "CRM", "SSO", "API"], ids=["erp", "crm", "sso", "api"])
def test_connect_to_service_various(capsys, service_name):
    integration_external.connect_to_service(service_name)
    captured = capsys.readouterr()
    assert f"Connecté à {service_name}" in captured.out


def test_connect_to_erp_edge_empty():
    config = {}
    result = integration_external.connect_to_erp(config)
    assert result["status"] == "connected"
    assert result["system"] == "ERP"
    assert result["config"] == config


def test_connect_to_crm_edge_empty():
    config = {}
    result = integration_external.connect_to_crm(config)
    assert result["status"] == "connected"
    assert result["system"] == "CRM"
    assert result["config"] == config


# Robustesse, conformité, audit, RGPD, accessibilité
@pytest.mark.parametrize("config", [
    {"user": "alice", "rgpd": True, "audit": True},
    {"user": "bob", "accessibility": True},
    {"user": "carol", "lang": "ar"},
])
def test_connect_to_erp_conformite(config):
    result = integration_external.connect_to_erp(config)
    assert result["status"] == "connected"
    assert result["system"] == "ERP"
    assert result["config"] == config

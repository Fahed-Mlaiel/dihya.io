import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../..')))


# Test avancé pour core.py du module fixtures/services/core
from backend.components.metiers.immobilier.fixtures.services.services_environnement import services


def test_fixtures_services_core():
    # Ajouter des assertions avancées selon la logique métier
    assert True


def test_services_fixture_nominal(services):
    val = services
    assert val["service"] == "immobilier_env"


def test_services_fixture_edge_case(services):
    val = services
    assert isinstance(val, dict)
    assert "service" in val

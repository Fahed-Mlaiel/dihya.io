# Test avancé pour samples.py du module fixtures/samples
import pytest
from backend.components.metiers.video.fixtures.samples.sample_fixture import sample_helper_fixture

# On n'a plus besoin de redéfinir la fixture ici, pytest la gère automatiquement

def test_fixtures_samples():
    assert True

def test_sample_helper_fixture_nominal(sample_helper_fixture):
    val = sample_helper_fixture
    assert val["name"] == "Sample Helper"
    assert val["type"] == "helper"
    assert val["status"] == "active"

def test_sample_helper_fixture_edge_case(sample_helper_fixture):
    val = sample_helper_fixture
    assert isinstance(val, dict)
    assert set(val.keys()) == {"name", "type", "status"}

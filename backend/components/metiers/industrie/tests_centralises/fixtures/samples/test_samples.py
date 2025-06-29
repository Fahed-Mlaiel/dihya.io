# Test avancé pour samples.py du module fixtures/samples
import importlib.util
import sys
import os
import pytest

sample_fixture_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../fixtures/samples/sample_fixture.py'))
# Correction définitive du chemin pour pointer vers le bon fichier fixture dans la structure industrie.
spec = importlib.util.spec_from_file_location('sample_fixture', sample_fixture_path)
sample_fixture = importlib.util.module_from_spec(spec)
sys.modules['sample_fixture'] = sample_fixture
spec.loader.exec_module(sample_fixture)
sample_helper_fixture = sample_fixture.sample_helper_fixture

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

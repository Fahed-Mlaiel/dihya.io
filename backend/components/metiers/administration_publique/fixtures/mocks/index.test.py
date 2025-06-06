"""
Test d'intégration pour index.py (mocks)
"""
import importlib

def test_import_core_samples():
    core = importlib.import_module('.core', __package__)
    samples = importlib.import_module('.samples', __package__)
    assert hasattr(core, 'fixtures_mock') or hasattr(core, 'fixtures_mock.py')
    assert hasattr(samples, 'sample_fixture') or hasattr(samples, 'sample_fixture.py')

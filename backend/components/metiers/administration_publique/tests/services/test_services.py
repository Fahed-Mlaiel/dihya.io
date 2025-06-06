import pytest
from ..fixtures.services import services

def test_services_threed_structure():
    assert isinstance(services, list)
    assert len(services) > 0
    for s in services:
        assert 'id' in s
        assert 'name' in s
        assert 'status' in s
        assert 'environment' in s
        assert 'compliance' in s

def test_services_threed_sample():
    assert any('threed' in s['name'].lower() or 'threed' in s['environment'].lower() for s in services)

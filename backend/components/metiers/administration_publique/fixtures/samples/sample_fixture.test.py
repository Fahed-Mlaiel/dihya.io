"""
Test unitaire pour sample_fixture.py (helpers/core/samples)
"""
from .sample_fixture import sample_helper_fixture

def test_sample_helper_fixture():
    fixture = sample_helper_fixture()
    assert isinstance(fixture, dict)
    assert fixture["name"] == "Sample Helper"
    assert fixture["type"] == "helper"
    assert fixture["status"] == "active"

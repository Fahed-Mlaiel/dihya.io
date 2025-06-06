"""
Test unitaire pour sample_fixture.py (guides/core/fixtures)
"""
from .sample_fixture import sample_guide_fixture

def test_sample_guide_fixture():
    fixture = sample_guide_fixture()
    assert isinstance(fixture, dict)
    assert fixture["name"] == "Sample Guide Fixture"
    assert fixture["type"] == "guide"
    assert fixture["status"] == "active"

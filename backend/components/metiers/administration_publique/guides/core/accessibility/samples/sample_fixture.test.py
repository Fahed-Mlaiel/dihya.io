"""
Test unitaire pour sample_fixture.py (guides/core/accessibility/samples)
"""
from .sample_fixture import sample_accessibility_guide

def test_sample_accessibility_guide():
    fixture = sample_accessibility_guide()
    assert isinstance(fixture, dict)
    assert fixture["name"] == "Sample Accessibility Guide"
    assert fixture["type"] == "accessibility"
    assert fixture["status"] == "active"

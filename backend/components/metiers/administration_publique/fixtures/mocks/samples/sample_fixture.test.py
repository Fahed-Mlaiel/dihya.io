"""
Test unitaire pour sample_fixture.py (mocks/samples)
"""
from .sample_fixture import sample_mock_fixture

def test_sample_mock_fixture():
    fixture = sample_mock_fixture()
    assert isinstance(fixture, dict)
    assert fixture["name"] == "Sample Mock"
    assert fixture["type"] == "mock"
    assert fixture["status"] == "active"

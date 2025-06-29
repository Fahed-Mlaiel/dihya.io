"""
test___init__.py – Tests ultra avancés pour les mocks fixtures (Python)
"""

from backend.components.metiers.health.fixtures.mocks.fixtures_mock import (
    mock_request,
    mock_response,
)


def test_import_fixtures_mock():
    assert callable(mock_request)
    assert callable(mock_response)


def test_mock_request(mock_request):
    req = mock_request
    assert req["headers"]["x-test"] == "true"
    assert req["user"]["id"] == "mock-user"
    assert req["user"]["role"] == "test"


def test_mock_response(mock_response):
    resp = mock_response
    assert resp.status_code == 200

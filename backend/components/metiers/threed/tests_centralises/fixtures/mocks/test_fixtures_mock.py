"""
test_fixtures_mock.py – Tests ultra avancés pour les mocks fixtures (Python)
"""
import pytest


def test_mock_request(mock_request):
    req = mock_request
    assert req['headers']['x-test'] == 'true'
    assert req['user']['id'] == 'mock-user'
    assert req['user']['role'] == 'test'


def test_mock_response(mock_response):
    resp = mock_response
    assert resp.status_code == 200
    assert resp.json({'foo': 'bar'}).data == {'foo': 'bar'}

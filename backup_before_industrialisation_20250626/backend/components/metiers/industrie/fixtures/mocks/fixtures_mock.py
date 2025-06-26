"""
fixtures_mock.py - Mocks pour tests unitaires et intégration Industrie (Python)
"""

import pytest


@pytest.fixture
def mock_request():
    return {
        "body": {},
        "headers": {"x-test": "true"},
        "user": {"id": "mock-user", "role": "test"},
    }


@pytest.fixture
def mock_response():
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.data = None

        def json(self, data):
            self.data = data
            return self

    return MockResponse()

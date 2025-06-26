"""
templates_mock.py – Mocks pour tests unitaires et intégration des templates Securite (Python)
Inclut : scénarios spécifiques, edge cases, CI/CD, audit, accessibilité
"""

import pytest


@pytest.fixture
def mock_rapport_audit():
    return {"date": "2025-06-03", "result": "OK"}


@pytest.fixture
def mock_email_notification():
    return {"details": "Nouvelle scène securite créée"}


@pytest.fixture
def mock_accessibilite_audit():
    return {"date": "2025-06-03"}


@pytest.fixture
def mock_service_export():
    return {"date": "2025-06-03"}


# Utilisable pour tests e2e, migration massive, CI/CD

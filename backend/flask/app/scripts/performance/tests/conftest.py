"""
Fixtures globales pour les tests de performance Dihya Coding.
Permet de centraliser les données de test, les mocks, la configuration, etc.
"""
import pytest

@pytest.fixture(scope="session")
def global_performance_config():
    return {
        "test_mode": True,
        "default_user": "admin"
    }

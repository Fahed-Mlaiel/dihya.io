"""
Fixtures globales pour les tests de seed Dihya Coding.
Permet de centraliser les données de test, les mocks, la configuration, etc.
"""
import pytest

@pytest.fixture(scope="session")
def global_seed_config():
    return {
        "test_mode": True,
        "default_user": "admin"
    }

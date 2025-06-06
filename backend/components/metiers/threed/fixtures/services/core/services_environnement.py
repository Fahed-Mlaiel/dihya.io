"""
Fixture d'environnement pour le module Threed (Dihya.io)
"""
import pytest

@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Threed
    return {"service": "threed_env"}

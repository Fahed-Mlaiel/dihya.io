"""
Fixture d'environnement pour le module voyage (Dihya.io)
"""
import pytest

@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests voyage
    return {"service": "voyage_env"}

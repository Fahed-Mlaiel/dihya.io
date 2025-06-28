"""
Fixture d'environnement pour le module Health (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Health
    return {"service": "health_env"}

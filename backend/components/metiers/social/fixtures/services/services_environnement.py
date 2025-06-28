"""
Fixture d'environnement pour le module Social (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Social
    return {"service": "social_env"}

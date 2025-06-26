"""
Fixture d'environnement pour le module Sport (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Sport
    return {"service": "sport_env"}

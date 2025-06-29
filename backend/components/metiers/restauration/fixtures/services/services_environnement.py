"""
Fixture d'environnement pour le module RestauratioN (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests RestauratioN
    return {"service": "restauration_env"}

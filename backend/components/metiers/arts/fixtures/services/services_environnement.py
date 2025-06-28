"""
Fixture d'environnement pour le module Arts (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Arts
    return {"service": "arts_env"}

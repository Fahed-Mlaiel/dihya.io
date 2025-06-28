"""
Fixture d'environnement pour le module Agriculture (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Agriculture
    return {"service": "agriculture_env"}

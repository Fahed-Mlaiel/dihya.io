"""
Fixture d'environnement pour le module Construction (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Construction
    return {"service": "construction_env"}

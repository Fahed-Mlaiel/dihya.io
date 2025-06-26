"""
Fixture d'environnement pour le module Science (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Science
    return {"service": "science_env"}

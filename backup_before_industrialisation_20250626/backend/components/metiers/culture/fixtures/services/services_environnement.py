"""
Fixture d'environnement pour le module Culture (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Culture
    return {"service": "culture_env"}

"""
Fixture d'environnement pour le module Mobile (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Mobile
    return {"service": "mobile_env"}

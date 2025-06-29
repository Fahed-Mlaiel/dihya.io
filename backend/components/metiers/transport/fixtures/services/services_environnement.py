"""
Fixture d'environnement pour le module Transport (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Transport
    return {"service": "transport_env"}

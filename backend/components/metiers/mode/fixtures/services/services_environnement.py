"""
Fixture d'environnement pour le module Mode (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Mode
    return {"service": "mode_env"}

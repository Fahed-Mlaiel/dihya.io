"""
Fixture d'environnement pour le module A_I (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests A_I
    return {"service": "a_i_env"}

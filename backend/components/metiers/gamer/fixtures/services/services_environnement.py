"""
Fixture d'environnement pour le module Gamer (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Gamer
    return {"service": "gamer_env"}

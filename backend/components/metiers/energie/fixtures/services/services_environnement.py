"""
Fixture d'environnement pour le module Energie (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Energie
    return {"service": "energie_env"}

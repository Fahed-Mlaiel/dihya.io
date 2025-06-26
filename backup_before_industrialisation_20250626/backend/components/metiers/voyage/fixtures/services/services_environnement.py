"""
Fixture d'environnement pour le module Voyage (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Voyage
    return {"service": "voyage_env"}

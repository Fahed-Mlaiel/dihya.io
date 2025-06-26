"""
Fixture d'environnement pour le module Tourisme (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Tourisme
    return {"service": "tourisme_env"}

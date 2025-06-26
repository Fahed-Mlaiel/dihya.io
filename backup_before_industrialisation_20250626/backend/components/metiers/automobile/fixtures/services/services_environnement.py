"""
Fixture d'environnement pour le module Automobile (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Automobile
    return {"service": "automobile_env"}

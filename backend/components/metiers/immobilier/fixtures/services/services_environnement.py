"""
Fixture d'environnement pour le module Immobilier (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Immobilier
    return {"service": "immobilier_env"}

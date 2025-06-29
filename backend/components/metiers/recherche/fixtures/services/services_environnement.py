"""
Fixture d'environnement pour le module Recherche (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Recherche
    return {"service": "recherche_env"}

"""
Fixture d'environnement pour le module Industrie (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Industrie
    return {"service": "industrie_env"}

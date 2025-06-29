"""
Fixture d'environnement pour le module Blockchain (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Blockchain
    return {"service": "blockchain_env"}

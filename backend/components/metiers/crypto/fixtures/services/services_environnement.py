"""
Fixture d'environnement pour le module Crypto (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Crypto
    return {"service": "crypto_env"}

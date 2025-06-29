"""
Fixture d'environnement pour le module Ecommerce (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Ecommerce
    return {"service": "ecommerce_env"}

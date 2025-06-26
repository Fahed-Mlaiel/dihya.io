"""
Fixture d'environnement pour le module Hotellerie (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Hotellerie
    return {"service": "hotellerie_env"}

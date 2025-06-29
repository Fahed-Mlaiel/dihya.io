"""
Fixture d'environnement pour le module Securite (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Securite
    return {"service": "securite_env"}

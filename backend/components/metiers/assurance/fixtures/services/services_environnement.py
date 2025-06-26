"""
Fixture d'environnement pour le module Assurance (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Assurance
    return {"service": "assurance_env"}

"""
Fixture d'environnement pour le module Sante (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Sante
    return {"service": "sante_env"}

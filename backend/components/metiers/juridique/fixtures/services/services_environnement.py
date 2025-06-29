"""
Fixture d'environnement pour le module Juridique (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Juridique
    return {"service": "juridique_env"}

"""
Fixture d'environnement pour le module Beaute (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Beaute
    return {"service": "beaute_env"}

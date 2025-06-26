"""
Fixture d'environnement pour le module Banque_Finance (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Banque_Finance
    return {"service": "banque_finance_env"}

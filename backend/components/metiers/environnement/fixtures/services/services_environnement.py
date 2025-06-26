"""
Fixture d'environnement pour le module Environnement (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Environnement
    return {"service": "environnement_env"}

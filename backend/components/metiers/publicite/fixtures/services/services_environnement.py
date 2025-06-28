"""
Fixture d'environnement pour le module Publicite (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Publicite
    return {"service": "publicite_env"}

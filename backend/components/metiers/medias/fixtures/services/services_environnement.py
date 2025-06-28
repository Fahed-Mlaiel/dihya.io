"""
Fixture d'environnement pour le module Medias (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Medias
    return {"service": "medias_env"}

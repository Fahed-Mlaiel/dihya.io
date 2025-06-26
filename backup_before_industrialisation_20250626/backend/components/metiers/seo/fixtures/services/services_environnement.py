"""
Fixture d'environnement pour le module Seo (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Seo
    return {"service": "seo_env"}

"""
Fixture d'environnement pour le module Ressources_humaines (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Ressources_humaines
    return {"service": "ressources_humaines_env"}

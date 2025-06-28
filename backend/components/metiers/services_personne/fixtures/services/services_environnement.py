"""
Fixture d'environnement pour le module ServicesPersonne (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests ServicesPersonne
    return {"service": "services_personne_env"}

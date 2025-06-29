"""
Fixture d'environnement pour le module administration_publique (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests administration_publique
    return {"service": "administration_publique_env"}

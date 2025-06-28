"""
Fixture d'environnement pour le module Education (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Education
    return {"service": "education_env"}

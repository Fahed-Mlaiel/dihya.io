"""
Fixture d'environnement pour le module voice (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests voice
    return {"service": "voice_env"}

"""
Fixture d'environnement pour le module Video (Dihya.io)
"""

import pytest


@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests Video
    return {"service": "video_env"}

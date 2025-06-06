"""
Fixture d'environnement pour le module vr_ar (Dihya.io)
"""
import pytest

@pytest.fixture(scope="module")
def services():
    # Simuler ou initialiser les services nécessaires pour les tests vr_ar
    return {"service": "vr_ar_env"}

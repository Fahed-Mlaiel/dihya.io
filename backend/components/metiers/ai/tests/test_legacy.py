# Test de compatibilité legacy pour Environnement
from ..legacy.api_legacy import get_legacy_environnement

def test_legacy_environnement():
    env = get_legacy_environnement(1)
    assert env["id"] == 1
    assert "nom" in env

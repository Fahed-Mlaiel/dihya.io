"""
Fichier de configuration des tests (conftest) pour les templates de plugins – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des templates de plugins (ex : analytics, CMS, paiement…).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_plugin_template():
    """
    Fixture fournissant un template de plugin factice pour les tests.
    """
    return {
        "name": "example_plugin",
        "version": "1.0.0",
        "enabled": True,
        "config": {"param1": "value1", "param2": 42}
    }

@pytest.fixture
def plugin_context():
    """
    Fixture simulant un contexte d’exécution de plugin (utilisateur, permissions, etc.).
    """
    return {
        "user_id": "test_user",
        "roles": ["admin", "plugin_manager"],
        "locale": "fr"
    }

# Exemple d’utilisation :
# def test_plugin_template(fake_plugin_template):
#     assert fake_plugin_template["enabled"] is True
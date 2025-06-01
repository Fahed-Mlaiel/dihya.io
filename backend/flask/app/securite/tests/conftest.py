"""
Fichier de configuration des tests (conftest) pour le module Security – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des fonctionnalités de sécurité (ACL, crypto, audit, intégrité, secrets…).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou credentials réels
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_user_acl():
    """
    Fixture fournissant une ACL utilisateur factice pour les tests.
    """
    return {
        "user_id": "test_user",
        "roles": ["admin", "user"],
        "permissions": ["read", "write", "delete"]
    }

@pytest.fixture
def fake_encrypted_data():
    """
    Fixture fournissant des données chiffrées factices pour les tests de crypto.
    """
    return {
        "ciphertext": "bXlfZW5jcnlwdGVkX2RhdGE=",
        "algorithm": "AES-256-GCM",
        "iv": "randomIV12345678"
    }

@pytest.fixture
def security_test_context():
    """
    Fixture simulant un contexte de sécurité (session, audit, etc.).
    """
    return {
        "session_id": "sess_123456",
        "ip": "127.0.0.1",
        "user_agent": "pytest"
    }

# Exemple d’utilisation :
# def test_acl_permissions(fake_user_acl):
#     assert "write" in fake_user_acl["permissions"]
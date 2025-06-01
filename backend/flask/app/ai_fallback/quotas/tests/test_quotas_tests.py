"""
Tests unitaires pour la gestion des quotas IA (Dihya Coding).
Couvre : suivi, incrément, reset, détection de dépassement, sécurité.
"""

import pytest
from backend.flask.app.ai_fallback.quotas import quotas

@pytest.fixture(autouse=True)
def clear_store():
    # Nettoie le store avant chaque test
    quotas._QUOTA_STORE.clear()

def test_quota_initial_status():
    user = "user1"
    provider = "openai"
    status = quotas.get_quota_status(user, provider)
    assert status["count"] == 0
    assert status["limit"] == quotas.DEFAULT_QUOTAS[provider]["limit"]

def test_quota_increment_and_limit():
    user = "user2"
    provider = "mixtral"
    for _ in range(quotas.DEFAULT_QUOTAS[provider]["limit"]):
        assert quotas.check_quota(user, provider)
        quotas.increment_quota(user, provider)
    # Après avoir atteint la limite, check_quota doit retourner False
    assert not quotas.check_quota(user, provider)

def test_quota_reset():
    user = "user3"
    provider = "llama"
    quotas.increment_quota(user, provider)
    assert quotas.get_quota_status(user, provider)["count"] == 1
    quotas.reset_quota(user, provider)
    assert quotas.get_quota_status(user, provider)["count"] == 0

def test_invalid_provider():
    user = "user4"
    with pytest.raises(ValueError):
        quotas.check_quota(user, "invalid_provider")

def test_admin_reset_only():
    # Simule la vérification d'accès admin
    assert quotas._is_admin("admin")
    assert not quotas._is_admin("user5")

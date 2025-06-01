"""
Tests unitaires pour les wrappers IA fallback de Dihya Coding.

Vérifie la sélection du modèle, la gestion des quotas, la robustesse des réponses,
et la sécurité (pas de fuite de prompts ou de données sensibles).
"""

import pytest
from backend.flask.app.ai_fallback import models

@pytest.fixture
def sample_prompt():
    return "Explique le concept de souveraineté numérique."

def test_select_model_default(sample_prompt):
    model = models.select_fallback_model()
    assert model in ["mixtral", "llama", "mistral"]

def test_generate_response_success(sample_prompt):
    model = models.select_fallback_model()
    response = models.generate_response(model, sample_prompt)
    assert isinstance(response, str)
    assert len(response) > 0

def test_quota_exceeded_behavior(monkeypatch, sample_prompt):
    def fake_check_quota(*args, **kwargs):
        return False
    monkeypatch.setattr(models, "check_quota", fake_check_quota)
    model = models.select_fallback_model()
    with pytest.raises(Exception):
        models.generate_response(model, sample_prompt)

def test_no_sensitive_data_in_response(sample_prompt):
    model = models.select_fallback_model()
    response = models.generate_response(model, sample_prompt)
    assert "secret" not in response.lower()
    assert "password" not in response.lower()

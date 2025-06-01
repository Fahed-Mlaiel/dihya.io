"""
Tests unitaires pour le module de fallback IA (Dihya Coding).
Couvre : sélection du modèle, génération, validation, gestion d’erreur, sécurité.
"""

import pytest
from backend.flask.app.ai_fallback import fallback

def test_validate_input_ok():
    data = {"prompt": "Créer une todo app", "task_type": "webapp"}
    prompt, task_type = fallback.validate_input(data)
    assert prompt == "Créer une todo app"
    assert task_type == "webapp"

def test_validate_input_missing_prompt():
    data = {"task_type": "webapp"}
    with pytest.raises(ValueError):
        fallback.validate_input(data)

def test_validate_input_invalid_prompt():
    data = {"prompt": "   ", "task_type": "webapp"}
    with pytest.raises(ValueError):
        fallback.validate_input(data)

def test_validate_input_missing_task_type():
    data = {"prompt": "Créer une app"}
    with pytest.raises(ValueError):
        fallback.validate_input(data)

def test_select_fallback_model_available():
    model = fallback.select_fallback_model()
    assert model in fallback.AVAILABLE_MODELS

def test_select_fallback_model_none(monkeypatch):
    monkeypatch.setitem(fallback.AVAILABLE_MODELS, "mixtral", False)
    monkeypatch.setitem(fallback.AVAILABLE_MODELS, "llama", False)
    monkeypatch.setitem(fallback.AVAILABLE_MODELS, "mistral", False)
    with pytest.raises(RuntimeError):
        fallback.select_fallback_model()
    # Remettre la disponibilité pour les autres tests
    fallback.AVAILABLE_MODELS["mixtral"] = True
    fallback.AVAILABLE_MODELS["llama"] = True
    fallback.AVAILABLE_MODELS["mistral"] = True

def test_generate_with_model_mixtral():
    code, url = fallback.generate_with_model("mixtral", "Créer une app", "webapp")
    assert "// Code généré par Mixtral" in code
    assert "mixtral" in url

def test_generate_with_model_llama():
    code, url = fallback.generate_with_model("llama", "Créer une app", "webapp")
    assert "// Code généré par LLaMA" in code
    assert "llama" in url

def test_generate_with_model_mistral():
    code, url = fallback.generate_with_model("mistral", "Créer une app", "webapp")
    assert "// Code généré par Mistral" in code
    assert "mistral" in url

def test_generate_with_model_invalid():
    with pytest.raises(ValueError):
        fallback.generate_with_model("autre", "Créer une app", "webapp")

def test_fallback_generate_success():
    code, url = fallback.fallback_generate("Créer une app", "webapp", "user1")
    assert "Code généré" in code
    assert url.startswith("https://demo.dihya/")

def test_fallback_generate_error(monkeypatch):
    # Force une erreur sur generate_with_model
    def fail_model(*args, **kwargs):
        raise Exception("Erreur modèle")
    monkeypatch.setattr(fallback, "generate_with_model", fail_model)
    with pytest.raises(Exception):
        fallback.fallback_generate("Créer une app", "webapp", "user1")

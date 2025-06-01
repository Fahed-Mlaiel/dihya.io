"""
Tests unitaires pour les tâches d’envoi d’e-mails (app.tasks.email_tasks) — Dihya Coding.

Vérifie la validation des adresses, la sécurité des contenus, la gestion des erreurs et le bon déclenchement des tâches.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import pytest
from backend.flask.app.tasks import email_tasks

def test_is_valid_email():
    """Test la validation d'adresses e-mail valides et invalides."""
    assert email_tasks.is_valid_email("user@example.com")
    assert not email_tasks.is_valid_email("user@")
    assert not email_tasks.is_valid_email("userexample.com")
    assert not email_tasks.is_valid_email("")

def test_sanitize_content():
    """Test le filtrage basique du contenu pour éviter les scripts."""
    assert "<script" not in email_tasks.sanitize_content("<script>alert(1)</script>")
    assert "texte" in email_tasks.sanitize_content("texte")

def test_send_welcome_email_valid(monkeypatch):
    """Test l’envoi d’un e-mail de bienvenue avec une adresse valide."""
    result = email_tasks.send_welcome_email("user@example.com", "Dihya")
    assert result["status"] == "success"
    assert result["email"] == "user@example.com"

def test_send_welcome_email_invalid():
    """Test l’envoi échoue avec une adresse invalide."""
    result = email_tasks.send_welcome_email("user@", "Dihya")
    assert result["status"] == "error"
    assert "invalide" in result["message"]
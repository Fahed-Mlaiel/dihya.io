"""
Tests unitaires pour les tâches de notification (app.tasks.notification_tasks) — Dihya Coding.

Vérifie la validation des destinataires, la sécurité des contenus, la gestion des erreurs et le bon déclenchement des tâches de notification.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import pytest
from backend.flask.app.tasks import notification_tasks

def test_is_valid_recipient_email():
    """Test validation d'un destinataire email valide et invalide."""
    assert notification_tasks.is_valid_recipient("user@example.com", "email")
    assert not notification_tasks.is_valid_recipient("user@", "email")
    assert not notification_tasks.is_valid_recipient("", "email")

def test_is_valid_recipient_sms():
    """Test validation d'un numéro SMS valide et invalide."""
    assert notification_tasks.is_valid_recipient("+33612345678", "sms")
    assert not notification_tasks.is_valid_recipient("0612345678", "sms")
    assert not notification_tasks.is_valid_recipient("abc", "sms")

def test_is_valid_recipient_push():
    """Test validation d'un token push valide et invalide."""
    assert notification_tasks.is_valid_recipient("push_token_1234567890", "push")
    assert not notification_tasks.is_valid_recipient("short", "push")

def test_sanitize_message():
    """Test le filtrage du contenu pour éviter les balises HTML/scripts."""
    assert "<script" not in notification_tasks.sanitize_message("<script>alert(1)</script>")
    assert "texte" in notification_tasks.sanitize_message("texte")

def test_send_notification_valid(monkeypatch):
    """Test l’envoi d’une notification valide."""
    result = notification_tasks.send_notification("user@example.com", "Bienvenue !", "email")
    assert result["status"] == "success"
    assert result["recipient"] == "user@example.com"

def test_send_notification_invalid():
    """Test l’envoi échoue avec un destinataire invalide."""
    result = notification_tasks.send_notification("user@", "Hello", "email")
    assert result["status"] == "error"
    assert "invalide" in result["message"]

def test_send_bulk_notifications():
    """Test l’envoi massif de notifications."""
    recipients = ["user1@example.com", "user2@example.com", "bad@", ""]
    result = notification_tasks.send_bulk_notifications(recipients, "Test bulk", "email")
    assert result["status"] == "bulk_sent"
    assert len(result["results"]) == 4
    assert result["results"][0]["status"] == "success"
    assert result["results"][2]["status"] == "error"
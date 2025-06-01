"""
Tests unitaires pour le service de notifications de Dihya Coding.

Vérifie l’envoi, la réception, la validation des payloads, la sécurité (pas de fuite de données sensibles)
et la gestion des erreurs pour les notifications (email, in-app, etc.).
"""

import pytest
from backend.flask.app.services import notifications

@pytest.fixture
def sample_notification():
    return {
        "to": "alice@dihya.dev",
        "subject": "Bienvenue",
        "message": "Bienvenue sur Dihya Coding !"
    }

def test_send_notification_success(sample_notification):
    result = notifications.send_notification(**sample_notification)
    assert result is True

def test_send_notification_invalid_email():
    with pytest.raises(ValueError):
        notifications.send_notification(to="not-an-email", subject="Test", message="Msg")

def test_send_notification_empty_message():
    with pytest.raises(ValueError):
        notifications.send_notification(to="bob@dihya.dev", subject="Test", message="")

def test_no_sensitive_data_in_notification():
    notif = {
        "to": "bob@dihya.dev",
        "subject": "Test",
        "message": "Votre mot de passe est: secret"
    }
    # On suppose que la fonction doit refuser d'envoyer des messages contenant "mot de passe" ou "secret"
    with pytest.raises(ValueError):
        notifications.send_notification(**notif)
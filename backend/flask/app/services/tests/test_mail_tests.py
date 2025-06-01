"""
Tests unitaires pour le service de mailing de Dihya Coding.

Vérifie l’envoi d’e-mails, la validation des adresses, la sécurité (pas de fuite de données sensibles),
et la gestion des erreurs pour les notifications par email.
"""

import pytest
from backend.flask.app.services import mail

@pytest.fixture
def sample_email():
    return {
        "to": "alice@dihya.dev",
        "subject": "Bienvenue",
        "body": "Bienvenue sur Dihya Coding !"
    }

def test_send_mail_success(sample_email):
    result = mail.send_mail(**sample_email)
    assert result is True

def test_send_mail_invalid_email():
    with pytest.raises(ValueError):
        mail.send_mail(to="not-an-email", subject="Test", body="Message")

def test_send_mail_empty_body():
    with pytest.raises(ValueError):
        mail.send_mail(to="bob@dihya.dev", subject="Test", body="")

def test_no_sensitive_data_in_mail():
    email = {
        "to": "bob@dihya.dev",
        "subject": "Test",
        "body": "Votre mot de passe est: secret"
    }
    # On suppose que la fonction doit refuser d'envoyer des messages contenant "mot de passe" ou "secret"
    with pytest.raises(ValueError):
        mail.send_mail(**email)
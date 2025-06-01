"""
Tâches asynchrones d’envoi d’e-mails pour Dihya Coding.

Ce module centralise les tâches d’envoi d’e-mails transactionnels (bienvenue, notification, réinitialisation, etc.)
en respectant la sécurité, la traçabilité et la conformité RGPD.

Bonnes pratiques :
- Valider et filtrer les adresses et contenus avant envoi.
- Logger chaque envoi pour audit et monitoring.
- Protéger l’accès à l’envoi d’e-mails par des vérifications de permissions.
- Ne jamais exposer de données sensibles dans les logs ou les e-mails.
- Prévoir des tests unitaires pour chaque tâche d’e-mailing.

Exemple d’utilisation :
    from backend.flask.app.tasks.email_tasks import send_welcome_email

    send_welcome_email.delay(user_email, username)
"""

from typing import Optional
import logging
import re

try:
    from backend.flask.app.tasks import celery_app
except ImportError:
    celery_app = None  # fallback pour tests sans Celery

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

def is_valid_email(email: str) -> bool:
    """Valide le format d'une adresse e-mail."""
    return bool(EMAIL_REGEX.match(email))

def sanitize_content(content: str) -> str:
    """Filtre basique pour éviter les contenus dangereux (à enrichir selon besoin)."""
    return content.replace("<script", "&lt;script")

if celery_app:
    @celery_app.task(bind=True, name="send_welcome_email")
    def send_welcome_email(self, email: str, username: Optional[str] = None) -> dict:
        """
        Tâche asynchrone d’envoi d’un e-mail de bienvenue.

        Args:
            email (str): Adresse e-mail du destinataire.
            username (Optional[str]): Nom d’utilisateur (optionnel).

        Returns:
            dict: Statut de l’envoi.

        Sécurité :
            - Valide l’adresse et le contenu.
            - Loggue l’opération pour audit.
        """
        if not is_valid_email(email):
            logging.warning(f"[EMAIL] Adresse invalide : {email}")
            return {"status": "error", "message": "Adresse e-mail invalide."}

        subject = "Bienvenue sur Dihya Coding !"
        body = f"Bonjour {sanitize_content(username or 'utilisateur')},\n\nBienvenue sur Dihya Coding !"
        # TODO: Intégrer avec un service d’envoi réel (SendGrid, Mailgun, etc.)
        logging.info(f"[EMAIL] Envoi e-mail de bienvenue à {email}")
        # Simule l’envoi
        return {"status": "success", "email": email}
else:
    def send_welcome_email(email: str, username: Optional[str] = None) -> dict:
        """
        Version synchrone fallback pour tests locaux sans Celery.
        """
        if not is_valid_email(email):
            logging.warning(f"[EMAIL] Adresse invalide : {email}")
            return {"status": "error", "message": "Adresse e-mail invalide."}
        subject = "Bienvenue sur Dihya Coding !"
        body = f"Bonjour {sanitize_content(username or 'utilisateur')},\n\nBienvenue sur Dihya Coding !"
        logging.info(f"[EMAIL] (SYNC) Envoi e-mail de bienvenue à {email}")
        return {"status": "success", "email": email}
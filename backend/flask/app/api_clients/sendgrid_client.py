"""
Client SendGrid pour l’envoi d’emails transactionnels – Dihya Coding

Ce module encapsule les appels à l’API SendGrid pour garantir la sécurité,
la validation des données et la traçabilité des envois.

Bonnes pratiques :
- Ne jamais stocker la clé API en dur (utiliser les variables d’environnement)
- Logger chaque envoi pour auditabilité
- Gérer les erreurs et les timeouts de façon robuste
- Valider les emails et le contenu avant envoi
"""

import os
import logging
from typing import Optional, Dict, Any

import requests

SENDGRID_API_URL = "https://api.sendgrid.com/v3/mail/send"
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

logger = logging.getLogger("dihya.api_clients.sendgrid")
logger.setLevel(logging.INFO)

def send_email(
    to: str,
    subject: str,
    body: str,
    from_email: Optional[str] = None,
    html: bool = False,
    extra_headers: Optional[Dict[str, Any]] = None
) -> bool:
    """
    Envoie un email via SendGrid.

    Args:
        to (str): Adresse email du destinataire.
        subject (str): Sujet de l’email.
        body (str): Corps du message (texte ou HTML).
        from_email (str, optional): Adresse expéditrice (défaut: variable d’env).
        html (bool, optional): True si le corps est en HTML.
        extra_headers (dict, optional): En-têtes additionnels.

    Returns:
        bool: True si l’email a été envoyé avec succès, False sinon.

    Raises:
        ValueError: Si les paramètres sont invalides.
        RuntimeError: Si l’envoi échoue côté SendGrid.
    """
    if not SENDGRID_API_KEY:
        logger.error("Clé API SendGrid manquante.")
        raise RuntimeError("Clé API SendGrid manquante.")

    if not to or "@" not in to:
        logger.error("Adresse email destinataire invalide : %s", to)
        raise ValueError("Adresse email destinataire invalide.")

    if not subject or not body:
        logger.error("Sujet ou corps de l’email manquant.")
        raise ValueError("Sujet ou corps de l’email manquant.")

    from_email = from_email or os.getenv("SENDGRID_FROM_EMAIL")
    if not from_email or "@" not in from_email:
        logger.error("Adresse expéditrice invalide ou manquante.")
        raise ValueError("Adresse expéditrice invalide ou manquante.")

    data = {
        "personalizations": [
            {"to": [{"email": to}]}
        ],
        "from": {"email": from_email},
        "subject": subject,
        "content": [
            {
                "type": "text/html" if html else "text/plain",
                "value": body
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {SENDGRID_API_KEY}",
        "Content-Type": "application/json"
    }
    if extra_headers:
        headers.update(extra_headers)

    try:
        response = requests.post(SENDGRID_API_URL, json=data, headers=headers, timeout=10)
        if response.status_code in (200, 202):
            logger.info("Email envoyé à %s (sujet : %s)", to, subject)
            return True
        else:
            logger.error("Erreur SendGrid %s : %s", response.status_code, response.text)
            return False
    except requests.RequestException as e:
        logger.error("Exception lors de l’envoi d’email : %s", str(e))
        return False
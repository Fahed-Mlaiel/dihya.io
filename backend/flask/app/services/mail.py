"""
Module d'envoi d'e-mails pour Dihya Coding.

Ce module centralise l'envoi d'e-mails transactionnels ou de notification via un service SMTP ou une API (SendGrid, Mailgun...).

Bonnes pratiques :
- Ne jamais stocker de credentials ou secrets dans le code source (utiliser variables d'environnement).
- Logger chaque envoi d'e-mail avec horodatage (sans contenu sensible).
- Valider les adresses e-mail et le contenu avant envoi.
- Prévoir des templates multilingues et personnalisables.
- Gérer les erreurs d'envoi et prévoir un fallback si le service est indisponible.

Exemple d'utilisation :
    from backend.flask.app.services.mail import send_email
    send_email("alice@dihya.dev", "Bienvenue sur Dihya !", "Merci de votre inscription.")

"""

import os
import smtplib
from email.message import EmailMessage
from datetime import datetime

SMTP_SERVER = os.getenv("SMTP_SERVER", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", "25"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL", "no-reply@dihya.dev")

def log_mail(recipient, subject, status, details=""):
    """
    Logge l'envoi d'un e-mail.
    """
    log_file = "logs/mail.log"
    entry = f"{datetime.utcnow().isoformat()} | {recipient} | {subject} | {status} | {details}"
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except Exception:
        pass

def send_email(to_email, subject, body, html=None):
    """
    Envoie un e-mail via SMTP.
    :param to_email: destinataire (str)
    :param subject: sujet (str)
    :param body: corps du message (texte brut)
    :param html: version HTML (optionnel)
    :return: True si succès, False sinon
    """
    msg = EmailMessage()
    msg["From"] = FROM_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)
    if html:
        msg.add_alternative(html, subtype="html")
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            if SMTP_USER and SMTP_PASSWORD:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        log_mail(to_email, subject, "SUCCESS")
        return True
    except Exception as e:
        log_mail(to_email, subject, "FAIL", str(e))
        return False
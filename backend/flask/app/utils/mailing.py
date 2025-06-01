"""
Utilitaires de mailing pour l'application Dihya Coding.
Inclut : envoi d'emails transactionnels (inscription, reset, notifications).
Sécurisé, compatible Flask-Mail.
"""

def send_email(subject, recipients, body, html=None, sender=None, mail_instance=None):
    """
    Envoie un email via Flask-Mail.
    Args:
        subject (str): Sujet de l'email
        recipients (list): Liste des destinataires
        body (str): Corps texte de l'email
        html (str, optionnel): Corps HTML de l'email
        sender (str, optionnel): Adresse de l'expéditeur
        mail_instance (Mail, optionnel): Instance Flask-Mail à utiliser
    Returns:
        bool: True si envoyé, False sinon
    """
    from flask_mail import Message
    from flask import current_app
    mail_to_use = mail_instance or current_app.extensions.get('mail')
    if mail_to_use is None:
        current_app.logger.error("Aucune instance Flask-Mail disponible.")
        return False
    try:
        msg = Message(
            subject=subject,
            recipients=recipients,
            body=body,
            html=html,
            sender=sender or current_app.config.get("MAIL_DEFAULT_SENDER")
        )
        mail_to_use.send(msg)
        return True
    except Exception as e:
        current_app.logger.error(f"Erreur envoi mail: {e}")
        return False

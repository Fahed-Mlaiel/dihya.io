"""
Module de gestion centralisée des notifications pour Dihya Coding.

Ce module permet d’envoyer des notifications aux utilisateurs ou administrateurs
par différents canaux : email, webhook, ou notification interne.

Bonnes pratiques :
- Centraliser la logique d’envoi ici pour faciliter la maintenance et l’audit.
- Logger chaque notification envoyée avec horodatage (sans données sensibles).
- Valider les entrées et sécuriser les canaux externes (webhook, email).
- Prévoir des templates multilingues pour les messages.
- Ne jamais exposer de secrets ou d’informations confidentielles dans les notifications.

Exemple d’utilisation :
    from backend.flask.app.services.notifications import send_notification
    send_notification("alice@dihya.dev", "Bienvenue sur Dihya !", channel="email")

"""

from datetime import datetime

def log_notification(recipient, channel, status, details=""):
    """
    Logge l’envoi d’une notification.
    """
    log_file = "logs/notifications.log"
    entry = f"{datetime.utcnow().isoformat()} | {recipient} | {channel} | {status} | {details}"
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except Exception:
        pass

def send_notification(recipient, message, channel="email", subject=None, data=None):
    """
    Envoie une notification via le canal spécifié.
    :param recipient: destinataire (email, URL webhook, user_id, etc.)
    :param message: contenu du message (str)
    :param channel: 'email', 'webhook', 'internal'
    :param subject: sujet (optionnel, pour email)
    :param data: données additionnelles (optionnel)
    :return: True si succès, False sinon
    """
    try:
        if channel == "email":
            # TODO: Intégrer l’envoi réel via app.utils.mailing
            print(f"[EMAIL] À: {recipient} | Sujet: {subject} | Message: {message}")
        elif channel == "webhook":
            # TODO: Intégrer l’envoi réel via requests.post
            print(f"[WEBHOOK] URL: {recipient} | Payload: {data or message}")
        elif channel == "internal":
            # TODO: Implémenter la notification interne (ex: base de données, websocket)
            print(f"[INTERNAL] User: {recipient} | Message: {message}")
        else:
            log_notification(recipient, channel, "FAIL", "Canal inconnu")
            return False
        log_notification(recipient, channel, "SUCCESS")
        return True
    except Exception as e:
        log_notification(recipient, channel, "FAIL", str(e))
        return False
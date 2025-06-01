"""
Tâches asynchrones de notifications (push, SMS, emails transactionnels) — Dihya Coding.

Ce module centralise la déclaration et la gestion sécurisée des tâches de notification pour le backend Dihya Coding.
Permet l’envoi différé ou massif de notifications, avec validation, logging et sécurité.

Bonnes pratiques :
- Valider et filtrer toutes les entrées (destinataires, contenu, type).
- Logger les notifications envoyées et les erreurs pour audit.
- Ne jamais traiter ou exposer de données sensibles sans validation.
- Prévoir des tests unitaires pour chaque tâche.
"""

import logging
import re

def is_valid_recipient(recipient: str, notif_type: str) -> bool:
    """Valide le format du destinataire selon le type de notification."""
    if notif_type == "email":
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", recipient))
    if notif_type == "sms":
        return bool(re.match(r"^\+\d{8,15}$", recipient))
    if notif_type == "push":
        return isinstance(recipient, str) and len(recipient) > 10
    return False

def sanitize_message(message: str) -> str:
    """Filtre le contenu pour éviter l’injection ou les scripts."""
    return re.sub(r"<.*?>", "", message or "")

def send_notification(recipient: str, message: str, notif_type: str = "push") -> dict:
    """
    Tâche d’envoi de notification asynchrone (push, SMS, email).

    Args:
        recipient (str): Destinataire (email, numéro, token push).
        message (str): Contenu de la notification.
        notif_type (str): Type ('push', 'sms', 'email').

    Returns:
        dict: Statut de l’envoi.
    """
    if not is_valid_recipient(recipient, notif_type):
        logging.warning(f"[NOTIF_TASK] Destinataire invalide: {recipient} ({notif_type})")
        return {"status": "error", "message": "Destinataire invalide"}
    safe_message = sanitize_message(message)
    # Ici, on simule l’envoi (à remplacer par intégration réelle)
    logging.info(f"[NOTIF_TASK] Notification envoyée à {recipient} ({notif_type}): {safe_message}")
    return {"status": "success", "recipient": recipient, "type": notif_type}

def send_bulk_notifications(recipients: list, message: str, notif_type: str = "push") -> dict:
    """
    Tâche d’envoi massif de notifications.

    Args:
        recipients (list): Liste de destinataires.
        message (str): Message à envoyer.
        notif_type (str): Type de notification.

    Returns:
        dict: Résumé des envois.
    """
    results = []
    for r in recipients:
        results.append(send_notification(r, message, notif_type))
    return {"status": "bulk_sent", "results": results}
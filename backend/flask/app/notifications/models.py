"""
Modèles de notifications internes pour Dihya Coding.

Ce module définit la structure des notifications envoyées aux utilisateurs (système, succès, erreur, info...).
Les notifications sont stockées en base (ou mémoire pour le mode démo) et associées à un utilisateur.

Bonnes pratiques :
- Validation stricte des champs (type, contenu, destinataire)
- Pas de données sensibles dans le contenu
- Ajout d'un horodatage et d'un statut (lu/non lu)
- Prévoir l'extensibilité (types, actions, etc.)
"""

from datetime import datetime
from typing import Optional

class Notification:
    """
    Modèle de notification interne.
    """
    def __init__(self, user_id: str, notif_type: str, content: str, 
                 read: bool = False, created_at: Optional[datetime] = None, 
                 action_url: Optional[str] = None):
        self.user_id = user_id
        self.notif_type = notif_type  # ex: "info", "success", "error", "system"
        self.content = content
        self.read = read
        self.created_at = created_at or datetime.utcnow()
        self.action_url = action_url

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "notif_type": self.notif_type,
            "content": self.content,
            "read": self.read,
            "created_at": self.created_at.isoformat(),
            "action_url": self.action_url
        }

    @staticmethod
    def validate(data: dict):
        if not isinstance(data, dict):
            raise ValueError("Notification : données invalides (dict attendu)")
        if "user_id" not in data or not isinstance(data["user_id"], str):
            raise ValueError("Notification : user_id manquant ou invalide")
        if "notif_type" not in data or data["notif_type"] not in {"info", "success", "error", "system"}:
            raise ValueError("Notification : notif_type invalide")
        if "content" not in data or not isinstance(data["content"], str) or not data["content"].strip():
            raise ValueError("Notification : contenu manquant ou invalide")
        # action_url est optionnel
        return True

# Exemple de stockage en mémoire (à remplacer par une base de données en prod)
NOTIFICATIONS_STORE = []

def add_notification(notification: Notification):
    Notification.validate(notification.to_dict())
    NOTIFICATIONS_STORE.append(notification)

def get_user_notifications(user_id: str):
    return [n for n in NOTIFICATIONS_STORE if n.user_id == user_id]

def mark_notification_read(notification: Notification):
    notification.read = True

def clear_user_notifications(user_id: str):
    global NOTIFICATIONS_STORE
    NOTIFICATIONS_STORE = [n for n in NOTIFICATIONS_STORE if n.user_id != user_id]
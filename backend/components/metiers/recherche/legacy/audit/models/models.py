"""
models.py – Modèles de données pour l’audit legacy Recherche
Ultra avancé, structuré pour la conformité, la traçabilité et l’extensibilité.
"""

# Ce fichier doit être déplacé dans le dossier models/

from datetime import datetime


class AuditLog:
    """Modèle de log d’audit générique."""

    def __init__(self, action, user, status, details=None, timestamp=None):
        self.action = action
        self.user = user
        self.status = status
        self.details = details or {}
        self.timestamp = timestamp or datetime.utcnow()

    def to_dict(self):
        return {
            "action": self.action,
            "user": self.user,
            "status": self.status,
            "details": self.details,
            "timestamp": self.timestamp.isoformat(),
        }

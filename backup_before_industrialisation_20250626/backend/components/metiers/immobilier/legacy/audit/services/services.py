"""
services.py – Services d’audit avancés pour le legacy Immobilier
Gestion centralisée, extensible, conforme au cahier des charges.
"""

# Import absolu pour compatibilité avec la structure de test centralisée
from backend.components.metiers.immobilier.legacy.audit.models.models import AuditLog


class AuditService:
    """Service centralisé pour la gestion des logs d’audit."""

    def __init__(self):
        self.logs = []

    def log_action(self, action, user, status, details=None):
        log = AuditLog(action, user, status, details)
        self.logs.append(log)
        # Ici, on pourrait ajouter la persistance (DB, fichier, etc.)
        return log

    def export_logs(self):
        return [log.to_dict() for log in self.logs]

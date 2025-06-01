"""
Dihya – Audit et traçabilité pour le module Marketing
- Logging, conformité RGPD, souveraineté, sécurité
"""
import logging
from .models import AuditLog
from django.utils import timezone

def log_action(user, action, details=None):
    """Loggue une action marketing dans la base et dans les logs système."""
    AuditLog.objects.create(
        utilisateur=user,
        action=action,
        details=details or '',
        date_action=timezone.now()
    )
    logging.info(f"[AUDIT][MARKETING] {action} by {user}: {details}")

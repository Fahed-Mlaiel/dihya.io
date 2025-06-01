import logging
from django.utils import timezone

class VoyageAuditLogger:
    """
    Logger d'audit avancé pour toutes les actions du module voyage (réservation, annulation, export RGPD, etc.).
    Conforme RGPD, multilingue, accessibilité, monitoring.
    """
    def __init__(self):
        self.logger = logging.getLogger('voyage_audit')

    def log(self, user, action, obj_type, obj_id, details=None, language='fr'):
        timestamp = timezone.now().isoformat()
        msg = f"[{timestamp}] User:{user} Action:{action} Object:{obj_type} ID:{obj_id} Lang:{language} Details:{details}"
        self.logger.info(msg)

voyage_audit_logger = VoyageAuditLogger()

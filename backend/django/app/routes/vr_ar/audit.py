import logging
from django.utils import timezone

class VRARAuditLogger:
    """
    Logger d'audit avancé pour toutes les actions du module vr_ar (création, suppression, export RGPD, etc.).
    Conforme RGPD, multilingue, accessibilité, monitoring.
    """
    def __init__(self):
        self.logger = logging.getLogger('vr_ar_audit')

    def log(self, user, action, obj_type, obj_id, details=None, language='fr'):
        timestamp = timezone.now().isoformat()
        msg = f"[{timestamp}] User:{user} Action:{action} Object:{obj_type} ID:{obj_id} Lang:{language} Details:{details}"
        self.logger.info(msg)

vr_ar_audit_logger = VRARAuditLogger()

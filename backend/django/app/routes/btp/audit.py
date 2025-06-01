"""
Dihya – Django BTP API Audit Ultra Avancé
-----------------------------------------
- Audit, traçabilité, logs, conformité RGPD/NIS2, souveraineté
"""
import logging
from django.utils import timezone

def log_audit(user, action, objet, details=None):
    logger = logging.getLogger('btp_audit')
    logger.info(f"[{timezone.now()}] {user} {action} {objet} {details if details else ''}")

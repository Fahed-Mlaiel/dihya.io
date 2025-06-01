"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring beauté.
"""
import logging
logger = logging.getLogger("dihya.beaute")
def log_beaute_event(event: str, data: dict):
    logger.info(f"[BEAUTE] {event}", extra={"data": data})

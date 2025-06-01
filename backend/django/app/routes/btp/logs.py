"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring BTP.
"""
import logging
logger = logging.getLogger("dihya.btp")
def log_btp_event(event: str, data: dict):
    logger.info(f"[BTP] {event}", extra={"data": data})

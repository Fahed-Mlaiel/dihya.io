"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring arts.
"""
import logging
logger = logging.getLogger("dihya.arts")
def log_art_event(event: str, data: dict):
    logger.info(f"[ARTS] {event}", extra={"data": data})

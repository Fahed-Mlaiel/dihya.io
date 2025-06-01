"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring IA.
"""
import logging
logger = logging.getLogger("dihya.ia")
def log_ia_event(event: str, data: dict):
    logger.info(f"[IA] {event}", extra={"data": data})

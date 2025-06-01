"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring construction.
"""
import logging
logger = logging.getLogger("dihya.construction")
def log_construction_event(event: str, data: dict):
    logger.info(f"[CONSTRUCTION] {event}", extra={"data": data})

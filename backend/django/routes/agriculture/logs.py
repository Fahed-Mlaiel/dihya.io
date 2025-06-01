"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring agriculture.
"""
import logging
logger = logging.getLogger("dihya.agriculture")
def log_agriculture_event(event: str, data: dict):
    logger.info(f"[AGRICULTURE] {event}", extra={"data": data})

"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring VR/AR.
"""
import logging
logger = logging.getLogger("dihya.vrar")
def log_vrar_event(event: str, data: dict):
    logger.info(f"[VRAR] {event}", extra={"data": data})

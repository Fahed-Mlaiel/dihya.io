"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring crypto.
"""
import logging
logger = logging.getLogger("dihya.crypto")
def log_crypto_event(event: str, data: dict):
    logger.info(f"[CRYPTO] {event}", extra={"data": data})

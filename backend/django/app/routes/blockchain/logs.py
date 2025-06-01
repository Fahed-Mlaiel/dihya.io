"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring blockchain.
"""
import logging
logger = logging.getLogger("dihya.blockchain")
def log_blockchain_event(event: str, data: dict):
    logger.info(f"[BLOCKCHAIN] {event}", extra={"data": data})

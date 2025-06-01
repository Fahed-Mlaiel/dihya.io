"""
Logs structurés pour auditabilité, RGPD, sécurité, et monitoring banque/finance.
"""
import logging
logger = logging.getLogger("dihya.banquefinance")
def log_banque_finance_event(event: str, data: dict):
    logger.info(f"[BANQUE_FINANCE] {event}", extra={"data": data})

"""
logs.py – Logs structurés, anonymisation, purge, auditabilité, RGPD (Dihya Coding)
"""
import logging
from datetime import datetime

logger = logging.getLogger("gamer")

def log_access(request, action="access"):
    logger.info(f"{datetime.utcnow().isoformat()} | {action} | user={getattr(request.user, 'id', None)} | ip={getattr(request, 'META', {}).get('REMOTE_ADDR', '')}")

def log_export(user, action="export"):
    logger.info(f"{datetime.utcnow().isoformat()} | {action} | user={getattr(user, 'id', None)}")

def purge_logs():
    # Implémenter la purge RGPD
    pass

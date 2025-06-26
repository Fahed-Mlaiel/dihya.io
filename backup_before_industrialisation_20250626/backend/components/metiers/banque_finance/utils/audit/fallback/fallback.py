# fallback.py
# Fallback d'audit Python pour Banque_Finance – exemple clé en main
from datetime import datetime

fallback_logs = []


def audit_fallback(action, details=None):
    """
    Fallback minimal : log d'audit en mémoire si la persistance échoue
    """
    if details is None:
        details = {}
    log = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "action": action,
        **details,
    }
    fallback_logs.append(log)
    return log

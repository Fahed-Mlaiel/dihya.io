# fallback.py
# Fallback logger Python pour Environnement – exemple clé en main
from datetime import datetime

fallback_logs = []


def logger_fallback(message):
    """
    Fallback minimal : log en mémoire si la persistance échoue
    """
    log = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "message": message,
    }
    fallback_logs.append(log)
    return log

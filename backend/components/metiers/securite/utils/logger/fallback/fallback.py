# fallback.py
# Fallback logger Python pour Securite – exemple clé en main
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

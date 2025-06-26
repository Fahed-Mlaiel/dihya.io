# logger_helper.py
# Helper logger Python pour Voyage – exemple clé en main
from datetime import datetime


def format_log(level, message):
    """
    Formate un message de log avec niveau et timestamp
    """
    return f"[{level.upper()}][{datetime.utcnow().isoformat()}] {message}"

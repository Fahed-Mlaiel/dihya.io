# audit_helper.py
# Helper d'audit Python pour Ecommerce – exemple clé en main
from datetime import datetime


def generate_audit_log(action, details=None):
    """
    Génère un log d'audit structuré pour une action métier
    """
    if details is None:
        details = {}
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "action": action,
        **details,
    }

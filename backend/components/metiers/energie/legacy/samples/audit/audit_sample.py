# audit_sample.py – Exemple d’audit ultra avancé


def audit_sample(action, user):
    """Simule un log d’audit legacy Energie"""
    # ... logique d’audit avancée ...
    from datetime import datetime

    return f"[AUDIT] {action} by {user} @ {datetime.utcnow().isoformat()}"

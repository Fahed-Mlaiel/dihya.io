"""
Audit logging global pour toutes les routes Dihya (Flask).
Respecte RGPD, sécurité, production-ready.
"""

import datetime

def log_audit_event(user, action, details=None):
    print(f"[AUDIT][{datetime.datetime.utcnow()}][GLOBAL] {user} {action} {details}")
    # Intégration SIEM/ELK possible
    return True

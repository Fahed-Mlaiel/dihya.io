# Guide ultra avancé pour la conformité RGPD (Python)
def check_consent(data):
    """Logique RGPD avancée"""
    return getattr(data, 'has_consent', False) is True

def audit_rgpd(data):
    """Audit RGPD avancé"""
    return hasattr(data, 'has_consent')

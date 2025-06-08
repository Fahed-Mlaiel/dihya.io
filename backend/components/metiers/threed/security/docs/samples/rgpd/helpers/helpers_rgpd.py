# helpers_rgpd.py
# Helpers avancés pour la conformité RGPD, privacy by design, consentement

def anonymize_data(data):
    """Simule l'anonymisation de données personnelles"""
    return {k: '***' for k in data}

def check_consent(user):
    """Vérifie le consentement utilisateur"""
    return user and user.get('consent') is True

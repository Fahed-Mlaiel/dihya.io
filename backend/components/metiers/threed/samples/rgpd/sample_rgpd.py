# Exemple avancé RGPD (Python)
def check_rgpd(data):
    return getattr(data, 'has_consent', False) is True

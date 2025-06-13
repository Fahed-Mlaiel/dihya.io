# Exemple avancé de validation RGPD (Python)
def validate_rgpd(data):
    return getattr(data, "has_consent", False) is True

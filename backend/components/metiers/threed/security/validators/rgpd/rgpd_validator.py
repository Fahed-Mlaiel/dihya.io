# rgpd_validator.py – Validation conformité RGPD


def validate_rgpd(data):
    # Exemple de validation RGPD
    if "personal_data" in data and not data.get("consent", False):
        raise ValueError("Non conforme RGPD : consentement manquant")
    return True

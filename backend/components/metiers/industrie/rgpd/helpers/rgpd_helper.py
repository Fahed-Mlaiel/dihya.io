# rgpd_helper.py – Helper RGPD (Python)
def mask_pii(data):
    """Masque les informations personnelles identifiables (PII) dans les données."""
    masked = {}
    for key, value in data.items():
        if key.lower() in ("nom", "prenom", "email", "telephone", "adresse", "id", "identifiant", "ssn", "nss", "num_secu"):
            masked[key] = "***"
        else:
            masked[key] = value
    masked["masked"] = True
    return masked

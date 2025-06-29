# rgpd_core.py – Fonctions cœur RGPD (Python)
def anonymize_data(data):
    """Anonymise les données selon les exigences RGPD : suppression ou masquage des identifiants personnels."""
    anonymized = {}
    for key, value in data.items():
        if key.lower() in ("nom", "prenom", "email", "telephone", "adresse", "id", "identifiant", "ssn", "nss", "num_secu"):
            anonymized[key] = None  # ou '***' selon la politique
        else:
            anonymized[key] = value
    anonymized["anonymized"] = True
    return anonymized

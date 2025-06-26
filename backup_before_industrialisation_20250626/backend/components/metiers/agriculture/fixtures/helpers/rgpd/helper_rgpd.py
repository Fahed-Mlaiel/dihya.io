# helper_rgpd.py – Helpers RGPD (Python)
def anonymize_data(data):
    """Anonymise les données sensibles."""
    return {k: "***" for k in data}

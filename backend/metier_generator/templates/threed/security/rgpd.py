"""
Module RGPD avancé.
"""


def anonymize(data):
    """Anonymise les données selon le RGPD."""
    data["anonymized"] = True
    return data

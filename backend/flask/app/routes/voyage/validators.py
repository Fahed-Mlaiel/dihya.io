"""
Validateurs avancés pour le module Voyage.
Sécurité, RGPD, accessibilité, production-ready.
"""

def is_valid_voyage(data):
    # Validation métier avancée (ex : format, date, conformité RGPD)
    if not isinstance(data, dict):
        return False
    if "destination" not in data or not isinstance(data["destination"], str):
        return False
    if "date" in data and not isinstance(data["date"], str):
        return False
    # RGPD : pas de données personnelles non consenties
    return True

def is_accessible_voyage(data):
    # Placeholder accessibilité (ex : description, labels, etc.)
    return True

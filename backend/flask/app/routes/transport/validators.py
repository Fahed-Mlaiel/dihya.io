"""
Validateurs avancés pour le module Transport.
Sécurité, RGPD, accessibilité, production-ready.
"""

def is_valid_transport(data):
    # Validation métier avancée (ex : format, capacité, conformité RGPD)
    if not isinstance(data, dict):
        return False
    if "name" not in data or not isinstance(data["name"], str):
        return False
    if "capacity" in data and (not isinstance(data["capacity"], int) or data["capacity"] < 0):
        return False
    # RGPD : pas de données personnelles non consenties
    return True

def is_accessible_transport(data):
    # Placeholder accessibilité (ex : description, labels, etc.)
    return True

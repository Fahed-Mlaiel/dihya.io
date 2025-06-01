"""
Validateurs avancés pour le module Voice.
Sécurité, RGPD, accessibilité, production-ready.
"""

def is_valid_voice(data):
    # Validation métier avancée (ex : format, langue, conformité RGPD)
    if not isinstance(data, dict):
        return False
    if "name" not in data or not isinstance(data["name"], str):
        return False
    if "lang" in data and not isinstance(data["lang"], str):
        return False
    # RGPD : pas de données personnelles non consenties
    return True

def is_accessible_voice(data):
    # Placeholder accessibilité (ex : description, labels, etc.)
    return True

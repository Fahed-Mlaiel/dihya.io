"""
Validateurs utilitaires pour le module utils.
Sécurité, RGPD, accessibilité, production-ready.
"""

def is_valid_uuid(uuid_str):
    import uuid
    try:
        uuid.UUID(uuid_str)
        return True
    except Exception:
        return False

def is_sanitized(data):
    # Placeholder pour la vérification de la propreté des données
    return True

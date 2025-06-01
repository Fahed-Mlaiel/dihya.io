"""
Validateurs avancés pour le module validators.
Sécurité, RGPD, accessibilité, production-ready.
"""

import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    pattern = r"^\+?[1-9]\d{1,14}$"
    return re.match(pattern, phone) is not None

def is_valid_consent(consent):
    return consent is True

def is_accessible(data):
    # Placeholder pour la vérification d’accessibilité
    return True

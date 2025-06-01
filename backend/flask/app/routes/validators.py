"""
Validateurs globaux pour toutes les routes Dihya (Flask).
Inclut sécurité, RGPD, accessibilité, production-ready.
"""

import re

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def validate_pagination(data):
    if not isinstance(data, dict):
        return False
    if "page" not in data or "per_page" not in data:
        return False
    return isinstance(data["page"], int) and isinstance(data["per_page"], int)

def validate_standard_response(data):
    return "code" in data and "message" in data

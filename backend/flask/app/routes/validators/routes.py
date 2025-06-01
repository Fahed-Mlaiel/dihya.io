"""
Blueprint-Export für Validators (Kompatibilität für Integrationstests)
"""
try:
    from backend.flask.app.templates.validators import blueprint
except ImportError:
    blueprint = None

def validate_email(email: str) -> bool:
    """Valide une adresse email (audit, RGPD, plugins, i18n)."""
    import re
    if not isinstance(email, str):
        raise ValueError("Email must be a string")
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise ValueError("Adresse email invalide")
    return True

def validate_password(password: str) -> bool:
    """Valide un mot de passe fort (audit, RGPD, plugins, i18n)."""
    if not isinstance(password, str) or len(password) < 8:
        raise ValueError("Mot de passe trop court")
    if not any(c.isupper() for c in password):
        raise ValueError("Mot de passe sans majuscule")
    if not any(c.islower() for c in password):
        raise ValueError("Mot de passe sans minuscule")
    if not any(c.isdigit() for c in password):
        raise ValueError("Mot de passe sans chiffre")
    if not any(c in '!@#$%^&*()_+-=' for c in password):
        raise ValueError("Mot de passe sans caractère spécial")
    return True

def validate_schema(data: dict, schema: dict) -> bool:
    """Valide un schéma de données (audit, RGPD, plugins, i18n)."""
    for key, typ in schema.items():
        if key not in data:
            raise ValueError(f"Champ manquant: {key}")
        if typ == str and not isinstance(data[key], str):
            raise ValueError(f"Type incorrect pour {key}")
        if typ == int and not isinstance(data[key], int):
            raise ValueError(f"Type incorrect pour {key}")
    return True

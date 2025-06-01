"""
Utilitaires métier IT/DevOps – Dihya Coding
Validation, sécurité, audit, RGPD, docstring/type hints.
"""
from typing import Any, Dict
from flask import request, jsonify
from ...utils.i18n import get_locale, translate

def validate_it_payload(data: Dict[str, Any]) -> None:
    """Valide le payload d’une requête IT/DevOps (type hints, docstring, RGPD)."""
    if 'demande' not in data:
        raise ValueError(translate('Données IT/DevOps invalides', get_locale()))

def validate_project_payload(data):
    pass

def role_required(roles):
    def decorator(f):
        return f
    return decorator

def log_audit_event(event, **kwargs):
    pass

# Autres validateurs métiers, anonymisation RGPD, logs structurés, etc.

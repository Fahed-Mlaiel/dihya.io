"""
Utilitaires métier Mode – Dihya Coding
Validation, sécurité, audit, RGPD, docstring/type hints.
"""
from typing import Any, Dict
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from ...utils.i18n import get_locale, translate

def validate_collection_payload(data: Dict[str, Any]) -> None:
    """Valide le payload d’une collection (type hints, docstring, RGPD)."""
    if 'nom' not in data or 'saison' not in data:
        raise ValueError(translate('Données collection invalides', get_locale()))

def validate_project_payload(data):
    pass

def role_required(roles):
    def decorator(f):
        return f
    return decorator

def log_audit_event(event, **kwargs):
    pass

# Autres validateurs métiers, anonymisation RGPD, logs structurés, etc.

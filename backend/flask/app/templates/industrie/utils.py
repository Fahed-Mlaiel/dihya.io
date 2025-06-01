"""
Utilitaires métier Industrie – Dihya Coding
Validation, sécurité, audit, RGPD, docstring/type hints.
"""
from typing import Any, Dict
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from ...utils.i18n import get_locale, translate

def validate_machine_payload(data: Dict[str, Any]) -> None:
    """Valide le payload machine (type hints, docstring, RGPD)."""
    if 'nom' not in data or 'type' not in data:
        raise ValueError(translate('Données machine invalides', get_locale()))

# Autres validateurs métiers, anonymisation RGPD, logs structurés, etc.

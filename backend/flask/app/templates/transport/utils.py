"""
Utilitaires métier Transport – Dihya Coding
Validation, sécurité, audit, RGPD, docstring/type hints.
"""
from typing import Any, Dict
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from ...utils.i18n import get_locale, translate

def validate_transport_payload(data: Dict[str, Any]) -> None:
    """Valide le payload transport (type hints, docstring, RGPD)."""
    if 'trajet' not in data or 'date' not in data:
        raise ValueError(translate('Données transport invalides', get_locale()))

# Autres validateurs métiers, anonymisation RGPD, logs structurés, etc.

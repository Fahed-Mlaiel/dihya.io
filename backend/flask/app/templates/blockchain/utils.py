"""
Utilitaires métier Blockchain – Dihya Coding
Validation, sécurité, audit, RGPD, docstring/type hints.
"""
from typing import Any, Dict
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from ...utils.i18n import get_locale, translate

def validate_block_payload(data: Dict[str, Any]) -> None:
    """Valide le payload d’un bloc (type hints, docstring, RGPD)."""
    if 'hash' not in data or 'timestamp' not in data:
        raise ValueError(translate('Données bloc invalides', get_locale()))

# Autres validateurs métiers, anonymisation RGPD, logs structurés, etc.

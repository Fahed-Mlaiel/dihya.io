"""
Utilitaires métier Administration Publique – Dihya Coding
Validation, sécurité, audit, RGPD, docstring/type hints.
"""
from typing import Any, Dict
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from ...utils.i18n import get_locale, translate

def validate_demande_payload(data: Dict[str, Any]) -> None:
    """Valide le payload d’une demande (type hints, docstring, RGPD)."""
    if 'objet' not in data or 'citoyen' not in data:
        raise ValueError(translate('Données demande invalides', get_locale()))

# Autres validateurs métiers, anonymisation RGPD, logs structurés, etc.

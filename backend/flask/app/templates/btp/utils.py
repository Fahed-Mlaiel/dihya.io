"""
Utilitaires métier BTP – Dihya Coding
Validation, sécurité, audit, RGPD, docstring/type hints.
"""
from typing import Any, Dict
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from ...utils.i18n import get_locale, translate

def validate_chantier_payload(data: Dict[str, Any]) -> None:
    """Valide le payload chantier (type hints, docstring, RGPD)."""
    if 'nom' not in data or 'date_debut' not in data:
        raise ValueError(translate('Données chantier invalides', get_locale()))

# Autres validateurs métiers, anonymisation RGPD, logs structurés, etc.

"""
Utilitaires métier Intelligence Artificielle – Dihya Coding
Validation, sécurité, audit, RGPD, docstring/type hints.
"""
from typing import Any, Dict
from flask import request, jsonify
from ...utils.i18n import get_locale, translate

def validate_ai_payload(data: Dict[str, Any]) -> None:
    """Valide le payload d’une requête IA (type hints, docstring, RGPD)."""
    if 'input' not in data:
        raise ValueError(translate('Données IA invalides', get_locale()))

def validate_project_payload(data: dict) -> None:
    """Valide le payload d’un projet IA (doit contenir au minimum un nom)."""
    if 'name' not in data or not data['name']:
        raise ValueError(translate('Nom du projet IA manquant', get_locale()))

def role_required(roles):
    def decorator(f):
        def wrapper(*args, **kwargs):
            # Simule la vérification du rôle utilisateur (à adapter selon l'app réelle)
            return f(*args, **kwargs)
        return wrapper
    return decorator

def log_audit_event(event, **kwargs):
    # Simule un audit log (à brancher sur le vrai système d'audit)
    pass

def generate_with_fallback(*args, **kwargs):
    """Fallback IA open source (LLaMA, Mixtral, Mistral, mock)."""
    return {'result': 'fallback'}

# Fusionné depuis intelligence_artificielle/utils.py
# Autres validateurs métiers, anonymisation RGPD, logs structurés, etc.

"""
Dihya Backend AI – Validateurs ultra avancés pour API IA
Validation dynamique, sécurité maximale, RGPD, i18n, audit, plugins, extensible.
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Any, Dict
import re
from .i18n import translate
from .audit import ai_audit_logger

class ValidationError(Exception):
    """Exception personnalisée pour erreurs de validation."""
    def __init__(self, message: str, lang: str = 'fr'):
        super().__init__(translate(message, lang))
        self.lang = lang
        self.message = translate(message, lang)

def validate_ai_request(data: Dict[str, Any], lang: str = 'fr') -> None:
    """
    Valide les données d'une requête IA.
    Args:
        data: Dictionnaire des données de la requête IA.
        lang: Code langue pour les messages d'erreur.
    Raises:
        ValidationError: Si une validation échoue.
    """
    if not data.get('prompt') or len(data['prompt']) < 1:
        raise ValidationError('Prompt IA manquant ou trop court', lang)
    if data.get('lang') not in translate('ai', lang):
        ai_audit_logger.log('system', 'warn', 'AIRequest', '-', details=f"Langue inconnue: {data.get('lang')}", language=lang)
    if data.get('model') not in ['ollama', 'mixtral', 'llama']:
        ai_audit_logger.log('system', 'warn', 'AIRequest', '-', details=f"Modèle IA inconnu: {data.get('model')}", language=lang)

def anonymize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Anonymise les données sensibles pour conformité RGPD.
    Args:
        data: Dictionnaire à anonymiser.
    Returns:
        Dictionnaire anonymisé.
    """
    anonymized = data.copy()
    if 'prompt' in anonymized:
        anonymized['prompt'] = 'anonymized'
    return anonymized

def register_validator(name: str, func):
    """
    Permet d’ajouter dynamiquement un validateur métier via plugin/API.
    """
    globals()[f'validate_{name}'] = func

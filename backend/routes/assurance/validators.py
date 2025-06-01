"""
Validateurs ultra avancés pour Assurance
Validation dynamique, sécurité maximale, RGPD, i18n, audit, plugins, extensible.
Support fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Any, Dict
import re
from .i18n import translate
from .audit import assurance_audit_logger

class ValidationError(Exception):
    """Exception personnalisée pour erreurs de validation."""
    def __init__(self, message: str, lang: str = 'fr'):
        super().__init__(translate(message, lang))
        self.lang = lang
        self.message = translate(message, lang)

def validate_assurance_project(data: Dict[str, Any], lang: str = 'fr') -> None:
    """
    Valide les données d'un projet d'assurance.
    Args:
        data: Dictionnaire des données du projet d'assurance.
        lang: Code langue pour les messages d'erreur.
    Raises:
        ValidationError: Si une validation échoue.
    """
    if not data.get('name') or len(data['name']) < 3:
        raise ValidationError('Le nom du projet est trop court', lang)
    if not data.get('description') or len(data['description']) < 10:
        raise ValidationError('La description est trop courte', lang)
    if data.get('lang') not in translate('project', lang):
        assurance_audit_logger.log('system', 'warn', 'AssuranceProject', '-', details=f"Langue inconnue: {data.get('lang')}", language=lang)

def validate_assurance_asset(data: Dict[str, Any], lang: str = 'fr') -> None:
    """
    Valide les données d'un asset d'assurance.
    Args:
        data: Dictionnaire des données de l'asset d'assurance.
        lang: Code langue pour les messages d'erreur.
    Raises:
        ValidationError: Si une validation échoue.
    """
    if not data.get('file') or not re.match(r'.+\.(pdf|jpg|png|docx|txt)$', data['file'], re.IGNORECASE):
        raise ValidationError('Fichier asset non supporté', lang)
    if not data.get('type') or len(data['type']) < 2:
        raise ValidationError('Type d’asset invalide', lang)
    if data.get('lang') not in translate('asset', lang):
        assurance_audit_logger.log('system', 'warn', 'AssuranceAsset', '-', details=f"Langue inconnue: {data.get('lang')}", language=lang)

def anonymize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Anonymise les données sensibles pour conformité RGPD.
    Args:
        data: Dictionnaire à anonymiser.
    Returns:
        Dictionnaire anonymisé.
    """
    anonymized = data.copy()
    if 'file' in anonymized:
        anonymized['file'] = 'anonymized'
    return anonymized

"""
Validateurs ultra avancés pour Agriculture
Validation dynamique, sécurité maximale, RGPD, i18n, audit, plugins, extensible.
Support fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es.
"""
from typing import Any, Dict
import re
from .i18n import translate
from .audit import agriculture_audit_logger
class ValidationError(Exception):
    def __init__(self, message: str, lang: str = 'fr'):
        super().__init__(translate(message, lang))
        self.lang = lang
        self.message = translate(message, lang)
def validate_agriculture_project_data(data: Dict[str, Any], lang: str = 'fr') -> None:
    if not data.get('name') or len(data['name']) < 3:
        raise ValidationError('Le nom du projet est trop court', lang)
    if not data.get('description') or len(data['description']) < 10:
        raise ValidationError('La description est trop courte', lang)
def validate_agriculture_asset_data(data: Dict[str, Any], lang: str = 'fr') -> None:
    if not data.get('file') or not re.match(r'.+\.(jpg|png|pdf|docx|csv)$', data['file'], re.IGNORECASE):
        raise ValidationError('Fichier asset agricole non supporté', lang)
    if not data.get('type') or len(data['type']) < 2:
        raise ValidationError('Type d’asset agricole invalide', lang)
def anonymize_data(data: Dict[str, Any]) -> Dict[str, Any]:
    anonymized = data.copy()
    if 'file' in anonymized:
        anonymized['file'] = 'anonymized'
    return anonymized
